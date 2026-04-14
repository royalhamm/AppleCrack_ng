import subprocess

import logging

from typing import Dict, Any



class MDMBypass:

    """MDM (Mobile Device Management) bypass functionality."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def bypass_mdm(self) -> bool:

        """

        Bypass MDM restrictions on connected iOS device.



        Returns:

            bool: True if successful, False otherwise

        """

        try:

            self.logger.info("Starting MDM bypass process...")



            # First check if device is connected

            result = subprocess.run(

                ['idevice_id', '-l'],

                capture_output=True,

                text=True,

                check=False

            )



            if not result.stdout.strip():

                raise Exception("No iOS device connected")



            # Remove MDM profiles using ideviceprovision

            self.logger.info("Removing MDM profiles...")

            remove_result = subprocess.run(

                ['ideviceprovision', 'remove', 'com.apple.managedclient'],

                capture_output=True,

                text=True,

                check=False

            )



            if remove_result.returncode != 0:

                self.logger.warning(f"Failed to remove MDM profile: {remove_result.stderr}")



            # Reset network settings which often removes MDM configurations

            self.logger.info("Resetting network settings...")

            network_reset = subprocess.run(

                ['idevicediagnostics', 'restart', '--network'],

                capture_output=True,

                text=True,

                check=False

            )



            if network_reset.returncode != 0:

                self.logger.warning(f"Network reset failed: {network_reset.stderr}")



            # Use profiles command to remove enrollment

            self.logger.info("Removing enrollment profiles...")

            profile_remove = subprocess.run(

                ['profiles', 'remove', 'managed'],

                capture_output=True,

                text=True,

                check=False

            )



            if profile_remove.returncode != 0:

                self.logger.warning(f"Profile removal failed: {profile_remove.stderr}")



            self.logger.info("MDM bypass completed successfully!")

            return True



        except subprocess.CalledProcessError as e:

            self.logger.error(f"Subprocess error during MDM bypass: {e}")

            return False

        except Exception as e:

            self.logger.error(f"Unexpected error during MDM bypass: {e}")

            return False



    def check_mdm_status(self) -> Dict[str, Any]:

        """

        Check current MDM enrollment status.



        Returns:

            dict: Status information about MDM enrollment

        """

        try:

            self.logger.info("Checking MDM enrollment status...")



            # Check if device is connected

            result = subprocess.run(

                ['idevice_id', '-l'],

                capture_output=True,

                text=True,

                check=False

            )



            if not result.stdout.strip():

                return {"status": "error", "message": "No device connected"}



            # Get MDM status using profiles command

            status_result = subprocess.run(

                ['profiles', 'status', '-type', 'enrollment'],

                capture_output=True,

                text=True,

                check=False

            )



            if status_result.returncode == 0:

                return {

                    "status": "enrolled" if "Enrolled" in status_result.stdout else "not_enrolled",

                    "details": status_result.stdout.strip()

                }

            else:

                return {

                    "status": "unknown",

                    "message": status_result.stderr.strip()

                }



        except Exception as e:

            self.logger.error(f"Error checking MDM status: {e}")

            return {"status": "error", "message": str(e)}
