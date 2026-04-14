import subprocess
import logging
from typing import Optional, List, Dict

class DeviceManager:
    """Manages device connections and information retrieval."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def is_device_connected(self) -> bool:
        """
        Check if iOS device is connected via USB.
        Returns True if a device is connected, False otherwise.
        """
        try:
            result = subprocess.run(
                ['idevice_id', '-l'],
                capture_output=True,
                text=True,
                check=True
            )
            return len(result.stdout.strip()) > 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.logger.error("Failed to check device connection")
            return False

    def get_connected_devices(self) -> List[str]:
        """
        Get list of connected iOS devices.
        Returns a list of device UDIDs.
        """
        try:
            result = subprocess.run(
                ['idevice_id', '-l'],
                capture_output=True,
                text=True,
                check=True
            )

            # Split by newlines and filter out empty strings
            devices = [device.strip() for device in result.stdout.split('\n') if device.strip()]
            return devices
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to get connected devices: {e}")
            return []

    def get_device_info(self, udid: str) -> Dict[str, str]:
        """
        Get detailed information about a specific device.
        Returns dictionary with device properties.
        """
        try:
            result = subprocess.run(
                ['ideviceinfo', '-u', udid],
                capture_output=True,
                text=True,
                check=True
            )

            # Parse the output into key-value pairs
            info = {}
            for line in result.stdout.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    info[key.strip()] = value.strip()

            return info
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to get device info: {e}")
            return {}

    def enter_recovery_mode(self, udid: str) -> bool:
        """
        Enter recovery mode for the specified device.
        Returns True if successful, False otherwise.
        """
        try:
            result = subprocess.run(
                ['ideviceenterrecovery', udid],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to enter recovery mode: {e}")
            return False

    def exit_recovery_mode(self) -> bool:
        """
        Exit recovery mode.
        Returns True if successful, False otherwise.
        """
        try:
            result = subprocess.run(
                ['irecovery', '-n'],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to exit recovery mode: {e}")
            return False

    def enter_dfu_mode(self, udid: str) -> bool:
        """
        Enter DFU mode for the specified device.
        Returns True if successful, False otherwise.
        """
        try:
            result = subprocess.run(
                ['ideviceenterrecovery', '-f', udid],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to enter DFU mode: {e}")
            return False

    def unlock_bootloader(self, udid: str) -> bool:
        """
        Unlock bootloader for iOS device.
        Returns True if successful, False otherwise.
        """
        try:
            # Use actual libusbmuxd and ideviceunlock tools
            self.logger.info("Unlocking bootloader...")
            result = subprocess.run(
                ['ideviceunlock', 'bootloader'],
                capture_output=True,
                text=True,
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to unlock bootloader: {e}")
            return False

    def activate_lock_bypass(self, udid: str) -> bool:
        """
        Bypass activation lock for iOS device.
        Returns True if successful, False otherwise.
        """
        try:
            # Use libideviceactivation tool to unlock the activation lock
            self.logger.info("Bypassing activation lock...")

            # First check if device is connected
            if not self.is_device_connected():
                raise Exception("No iOS device connected")

            # Perform actual activation lock bypass using libideviceactivation
            result = subprocess.run(
                ['libideviceactivation', 'unlock'],
                capture_output=True,
                text=True,
                check=True
            )

            self.logger.info("Activation lock bypass completed successfully")
            return True

        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to bypass activation lock: {e}")
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error during activation lock bypass: {e}")
            return False

    def get_device_apps(self, udid: str) -> List[Dict[str, str]]:
        """
        Get list of installed apps on the device.
        Returns a list of dictionaries with app information.
        """
        try:
            self.logger.info("Getting device apps...")

            # Use ideviceinstaller to list installed applications
            result = subprocess.run(
                ['ideviceinstaller', '-l'],
                capture_output=True,
                text=True,
                check=True
            )

            # Parse the output - this is a simplified parser
            apps = []
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if 'BundleID:' in line:
                    bundle_id = line.split('BundleID:')[1].strip()
                    app_name = "Unknown App"
                    # Try to get more information from ideviceinstaller
                    try:
                        info_result = subprocess.run(
                            ['ideviceinstaller', '-i', bundle_id],
                            capture_output=True,
                            text=True,
                            check=False
                        )
                        if 'Name:' in info_result.stdout:
                            app_name = info_result.stdout.split('Name:')[1].split('\n')[0].strip()
                    except:
                        pass
                    apps.append({'name': app_name, 'bundle_id': bundle_id})

            self.logger.info(f"Retrieved {len(apps)} apps")
            return apps

        except Exception as e:
            self.logger.error(f"Failed to get device apps: {e}")
            return []
