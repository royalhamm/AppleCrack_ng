import subprocess

import logging



class IPAManager:

    """Manage IPA file installation and management."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def install_ipa(self, ipa_path: str) -> bool:

        """

        Install an IPA file on connected device.



        Args:

            ipa_path (str): Path to the .ipa file



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info(f"Installing IPA from {ipa_path}")



            # Check if ideviceinstaller is available and device is connected

            result = subprocess.run(

                ['idevice_id', '-l'],

                capture_output=True,

                text=True,

                check=False

            )



            if not result.stdout.strip():

                raise Exception("No iOS device connected")



            # Use ideviceinstaller to install IPA with proper error handling

            cmd = ['ideviceinstaller', '-i', ipa_path]



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info(f"Successfully installed IPA: {ipa_path}")

                return True

            else:

                self.logger.error(f"Failed to install IPA: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error installing IPA: {e}")

            raise
