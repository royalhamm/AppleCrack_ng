import subprocess

import logging

from pathlib import Path



class FirmwareManager:

    """Manage firmware installation and updates."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def install_firmware(self, firmware_path: str) -> bool:

        """

        Install firmware on connected device.



        Args:

            firmware_path (str): Path to the .ipsw file



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info(f"Installing firmware from {firmware_path}")



            # Validate firmware path

            firmware_file = Path(firmware_path)

            if not firmware_file.exists():

                raise FileNotFoundError(f"Firmware file not found: {firmware_path}")



            # Check if device is connected first

            result = subprocess.run(

                ['idevice_id', '-l'],

                capture_output=True,

                text=True,

                check=False

            )



            if not result.stdout.strip():

                raise Exception("No iOS device connected")



            # Use actual idevicerestore to install firmware

            cmd = ['idevicerestore', '-f', firmware_path]



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("Firmware installation completed successfully!")

                return True

            else:

                self.logger.error(f"Firmware installation failed: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Failed to install firmware: {e}")

            raise
