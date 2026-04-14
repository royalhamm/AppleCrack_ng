import subprocess

import logging



class RecoveryModeManager:

    """Manage recovery and DFU modes."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def enter_recovery_mode(self, device_udid: str) -> bool:

        """

        Enter recovery mode for specific device.



        Args:

            device_udid (str): Device UDID



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info(f"Entering recovery mode for {device_udid}")



            cmd = ['ideviceenterrecovery', device_udid]



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("Successfully entered recovery mode")

                return True

            else:

                self.logger.error(f"Failed to enter recovery mode: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error entering recovery mode: {e}")

            raise



    def exit_recovery_mode(self) -> bool:

        """

        Exit current recovery mode.



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info("Exiting recovery mode")



            cmd = ['irecovery', '-n']



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("Successfully exited recovery mode")

                return True

            else:

                self.logger.error(f"Failed to exit recovery mode: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error exiting recovery mode: {e}")

            raise



    def enter_dfu_mode(self, device_udid: str) -> bool:

        """

        Enter DFU mode for specific device.



        Args:

            device_udid (str): Device UDID



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info(f"Entering DFU mode for {device_udid}")



            cmd = ['ideviceenterrecovery', '-f', device_udid]



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("Successfully entered DFU mode")

                return True

            else:

                self.logger.error(f"Failed to enter DFU mode: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error entering DFU mode: {e}")

            raise
