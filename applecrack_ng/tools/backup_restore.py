import subprocess

import logging

import os

from pathlib import Path

from typing import Optional



class BackupRestoreManager:

    """Manage device backups and restores."""



    def __init__(self):

        self.logger = logging.getLogger(__name__)



    def create_backup(self, backup_name: str, backup_path: Optional[str] = None) -> bool:

        """

        Create a backup of the connected device.



        Args:

            backup_name (str): Name for the backup

            backup_path (str, optional): Path to store backup. Defaults to ~/applecrack_backups



        Returns:

            bool: True if successful

        """

        try:

            self.logger.info(f"Creating backup: {backup_name}")



            # Check if device is connected

            result = subprocess.run(

                ['idevice_id', '-l'],

                capture_output=True,

                text=True,

                check=False

            )



            if not result.stdout.strip():

                raise Exception("No iOS device connected")



            # Set default backup path if not provided

            if backup_path is None:

                backup_path = os.path.expanduser("~/applecrack_backups")



            # Create backup directory

            backup_dir = Path(backup_path) / backup_name

            backup_dir.mkdir(parents=True, exist_ok=True)



            # Use idevicebackup2 to create backup

            self.logger.info("Starting device backup...")

            backup_result = subprocess.run(

                ['idevicebackup2', 'backup', str(backup_dir)],

                capture_output=True,

                text=True,

                check=False

            )



            if backup_result.returncode == 0:

                self.logger.info(f"Backup '{backup_name}' created successfully at {backup_dir}")

                return True

            else:

                self.logger.error(f"Backup failed: {backup_result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error creating backup: {e}")

            return False



    def restore_backup(self, backup_path: str) -> bool:

        """

        Restore device from backup.



        Args:

            backup_path (str): Path to backup directory



        Returns:

            bool: True if successful

        """

        try:

            self.logger.info(f"Restoring from backup: {backup_path}")



            # Check if device is connected

            result = subprocess.run(

                ['idevice_id', '-l'],

                capture_output=True,

                text=True,

                check=False

            )



            if not result.stdout.strip():

                raise Exception("No iOS device connected")



            # Verify backup path exists

            backup_dir = Path(backup_path)

            if not backup_dir.exists():

                raise FileNotFoundError(f"Backup directory not found: {backup_path}")



            # Use idevicebackup2 to restore

            self.logger.info("Starting device restore...")

            restore_result = subprocess.run(

                ['idevicebackup2', 'restore', str(backup_dir)],

                capture_output=True,

                text=True,

                check=False

            )



            if restore_result.returncode == 0:

                self.logger.info("Device restore completed successfully!")

                return True

            else:

                self.logger.error(f"Restore failed: {restore_result.stderr}")

                return False



        except Exception as e:

            self.logger.error(f"Error restoring backup: {e}")

            return False



    def list_backups(self, backup_path: Optional[str] = None) -> list:

        """

        List available backups.



        Args:

            backup_path (str, optional): Path to backups directory. Defaults to ~/applecrack_backups



        Returns:

            list: List of backup names

        """

        try:

            # Set default backup path if not provided

            if backup_path is None:

                backup_path = os.path.expanduser("~/applecrack_backups")



            backup_dir = Path(backup_path)

            if not backup_dir.exists():

                return []



            # List directories in backup path

            backups = [item.name for item in backup_dir.iterdir() if item.is_dir()]

            return backups



        except Exception as e:

            self.logger.error(f"Error listing backups: {e}")

            return []
