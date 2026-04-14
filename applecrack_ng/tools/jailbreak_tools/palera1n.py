import subprocess

import logging



class Palera1nTool:

    """Integration with palera1n jailbreak tool."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def run_palera1n(self, device_udid: str = None) -> bool:

        """

        Run palera1n on connected device.



        Args:

            device_udid (str): Optional device UDID to target specific device



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info("Starting palera1n...")



            # Build command - using real palera1n executable from BlackArch packages

            cmd = ['./palera1n-macos-universal', '--continue']  # Continue mode



            if device_udid:

                cmd.extend(['-u', device_udid])



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("palera1n completed successfully!")

                return True

            else:

                self.logger.error(f"palera1n failed: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error running palera1n: {e}")

            raise
