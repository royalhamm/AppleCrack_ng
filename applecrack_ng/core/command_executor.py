import subprocess
import logging
from typing import Dict, Any

class CommandExecutor:
    """Execute system commands with proper error handling and logging."""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def execute_command(self, command: list, cwd: str = None) -> Dict[str, Any]:
        """
        Execute a shell command.

        Args:
            command (list): Command as list of arguments
            cwd (str): Working directory for the command

        Returns:
            dict: Dictionary containing status, output and errors
        """
        try:
            self.logger.info(f"Executing command: {' '.join(command)}")

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                cwd=cwd
            )

            return {
                'success': result.returncode == 0,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode,
                'command': ' '.join(command)
            }

        except Exception as e:
            self.logger.error(f"Command execution failed: {e}")
            return {
                'success': False,
                'stdout': '',
                'stderr': str(e),
                'returncode': -1,
                'command': ' '.join(command)
            }

    def execute_with_sudo(self, command: list) -> Dict[str, Any]:
        """
        Execute a command with sudo privileges.

        Args:
            command (list): Command as list of arguments

        Returns:
            dict: Dictionary containing status, output and errors
        """
        # Prepend 'sudo' to the command
        sudo_command = ['sudo'] + command

        return self.execute_command(sudo_command)
