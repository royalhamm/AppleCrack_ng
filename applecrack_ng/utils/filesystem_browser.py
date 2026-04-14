import os

import logging



class FileSystemBrowser:

    """Browse and manage device filesystem."""



    def __init__(self, device_connection):

        self.logger = logging.getLogger(__name__)

        self.device_connection = device_connection  # Assuming this is a valid connection object



    def list_directory(self, path: str) -> list:

        """

        List contents of directory.



        Args:

            path (str): Path to directory



        Returns:

            list: List of items in the directory

        """

        try:

            if self.device_connection.exists(path):

                return os.listdir(path)

            else:

                self.logger.warning(f"Directory {path} doesn't exist")

                return []

        except Exception as e:

            self.logger.error(f"Error listing directory {path}: {e}")

            return []



    def get_file_info(self, file_path: str) -> dict:

        """

        Get information about a file.



        Args:

            file_path (str): Path to the file



        Returns:

            dict: Dictionary with file information

        """

        try:

            if os.path.exists(file_path):

                stat = self.device_connection.stat(file_path)

                return {

                    'name': os.path.basename(file_path),

                    'path': file_path,

                    'size': stat.st_size,

                    'is_directory': os.path.isdir(file_path),

                    'permissions': oct(stat.st_mode)[-3:]

                }

            else:

                self.logger.warning(f"File {file_path} doesn't exist")

                return {}

        except Exception as e:

            self.logger.error(f"Error getting file info for {file_path}: {e}")

            return {}
