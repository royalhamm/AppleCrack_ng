import subprocess

import logging



class Odysseyra1nTool:

    """Integration with odysseyra1n jailbreak tool."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def run_odysseyra1n(self, device_udid: str = None) -> bool:

        """

        Run odysseyra1n on connected device.



        Args:

            device_udid (str): Optional device UDID to target specific device



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info("Starting odysseyra1n...")



            # Build command - this is a placeholder as odysseyra1n might need different parameters

            cmd = ['odysseyra1n', '-c']  # Continuous mode



            if device_udid:

                cmd.extend(['-u', device_udid])



            result = subprocess.run(

                cmd,

                capture_output=True,

                text=True,

                check=False

            )



            if result.returncode == 0:

                self.logger.info("odysseyra1n completed successfully!")

                return True

            else:

                self.logger.error(f"odysseyra1n failed: {result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error running odysseyra1n: {e}")

            raise
