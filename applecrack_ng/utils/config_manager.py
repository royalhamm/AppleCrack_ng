import json

import os

from pathlib import Path



class ConfigManager:

    """Manage application configuration settings."""



    def __init__(self, config_path=None):

        if config_path is None:

            config_path = os.path.expanduser("~/.config/applecrack_ng/config.json")

        self.config_path = Path(config_path)

        self.config = {}

        self.load_config()



    def load_config(self):

        """Load configuration from file."""

        try:

            if self.config_path.exists():

                with open(self.config_path, 'r') as f:

                    self.config = json.load(f)

            else:

                # Create default config

                self.config = self._get_default_config()

                self.save_config()

        except Exception as e:

            print(f"Error loading config: {e}")

            self.config = self._get_default_config()



    def save_config(self):

        """Save configuration to file."""

        try:

            # Create directory if it doesn't exist

            self.config_path.parent.mkdir(parents=True, exist_ok=True)



            with open(self.config_path, 'w') as f:

                json.dump(self.config, f, indent=4)

        except Exception as e:

            print(f"Error saving config: {e}")



    def get(self, key, default=None):

        """Get configuration value."""

        return self.config.get(key, default)



    def set(self, key, value):

        """Set configuration value."""

        self.config[key] = value

        self.save_config()



    def _get_default_config(self):

        """Get default configuration."""

        return {

            "theme": "dark",

            "log_level": "INFO",

            "auto_update": True,

            "jailbreak_tools_path": "/usr/bin",

            "backup_location": os.path.expanduser("~/applecrack_backups")

        }
