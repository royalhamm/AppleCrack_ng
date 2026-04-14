import subprocess

import logging



class Checkra1nTool:

    """Integration with checkra1n jailbreak tool."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def run_checkra1n(self, device_udid: str = None) -> bool:

        """

        Run checkra1n on connected device.



        Args:

            device_udid (str): Optional device UDID to target specific device



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info("Starting checkra1n...")



            # Build command - using real checkra1n executable from BlackArch packages

            cmd = ['checkra1n', '-c']  # Continuous mode for stability



            if device_udid:

                cmd.extend(['-u', device_udid])



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("checkra1n completed successfully!")

                return True

            else:

                self.logger.error(f"checkra1n failed: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error running checkra1n: {e}")

            raise
