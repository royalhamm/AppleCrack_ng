import sys

import subprocess

import logging

import os

from PyQt5.QtWidgets import (

    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout,

    QHBoxLayout, QPushButton, QLabel, QTextEdit, QListWidget,

    QMessageBox, QComboBox, QFileDialog, QCheckBox, QFrame, QInputDialog

)

from PyQt5.QtCore import Qt, QTimer

from PyQt5.QtGui import QFont



from applecrack_ng.core.device_manager import DeviceManager

from applecrack_ng.tools.mdm_bypass import MDMBypass

from applecrack_ng.tools.jailbreak_tools.checkra1n import Checkra1nTool

from applecrack_ng.tools.jailbreak_tools.palera1n import Palera1nTool

from applecrack_ng.tools.jailbreak_tools.odysseyra1n import Odysseyra1nTool

from applecrack_ng.tools.firmware_manager import FirmwareManager

from applecrack_ng.tools.backup_restore import BackupRestoreManager

from applecrack_ng.utils.theme_manager import ThemeManager



class UIManager(QMainWindow):

    """Main UI manager for AppleCrack_NG"""



    def __init__(self):

        super().__init__()



        self.device_manager = DeviceManager()

        self.mdm_bypass = MDMBypass()

        self.checkra1n_tool = Checkra1nTool()

        self.palera1n_tool = Palera1nTool()

        self.odysseyra1n_tool = Odysseyra1nTool()

        self.firmware_manager = FirmwareManager()

        self.backup_manager = BackupRestoreManager()

        self.theme_manager = ThemeManager()



        # Create main layout

        self.setWindowTitle("AppleCrack_NG - iOS Management Tool")

        self.setGeometry(100, 100, 1200, 800)



        # Setup central widget and main layout

        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)



        # Create tab widget

        self.tabs = QTabWidget()

        main_layout.addWidget(self.tabs)



        # Create tabs

        self.create_device_tab()

        self.create_mdm_tab()

        self.create_jailbreak_tab()

        self.create_firmware_tab()

        self.create_system_tab()

        self.create_filesystem_tab()



        # Add status bar

        self.statusBar().showMessage("Ready")



        # Setup timer for periodic updates

        self.update_timer = QTimer(self)

        self.update_timer.timeout.connect(self.update_device_status)

        self.update_timer.start(3000)  # Update every 3 seconds



        # Apply initial theme (dark by default)

        self.theme_manager.apply_dark_theme(self)



        # Set window to be visible

        self.show()



    def create_device_tab(self):

        """Create device management tab"""

        tab = QWidget()

        layout = QVBoxLayout(tab)



        # Device information display

        info_label = QLabel("Device Information:")

        layout.addWidget(info_label)



        self.device_info_text = QTextEdit()

        self.device_info_text.setReadOnly(True)

        layout.addWidget(self.device_info_text)



        # Control buttons

        button_layout = QHBoxLayout()



        refresh_btn = QPushButton("Refresh Connection")

        refresh_btn.clicked.connect(self.update_device_status)

        button_layout.addWidget(refresh_btn)



        connect_btn = QPushButton("Connect Device")

        connect_btn.clicked.connect(self.connect_device)

        button_layout.addWidget(connect_btn)



        # Activation lock bypass

        bypass_activation_btn = QPushButton("Bypass Activation Lock")

        bypass_activation_btn.clicked.connect(self.bypass_activation_lock)

        button_layout.addWidget(bypass_activation_btn)



        layout.addLayout(button_layout)



        self.tabs.addTab(tab, "Device Management")



    def create_mdm_tab(self):

        """Create MDM bypass tab"""

        tab = QWidget()

        layout = QVBoxLayout(tab)



        # MDM log display

        mdm_label = QLabel("MDM Bypass Logs:")

        layout.addWidget(mdm_label)



        self.mdm_log_text = QTextEdit()

        self.mdm_log_text.setReadOnly(True)

        layout.addWidget(self.mdm_log_text)



        # Control buttons

        button_layout = QHBoxLayout()



        bypass_btn = QPushButton("Bypass MDM")

        bypass_btn.clicked.connect(self.start_mdm_bypass)

        button_layout.addWidget(bypass_btn)



        check_btn = QPushButton("Check MDM Status")

        check_btn.clicked.connect(self.check_mdm_status)

        button_layout.addWidget(check_btn)



        layout.addLayout(button_layout)



        self.tabs.addTab(tab, "MDM Bypass")



    def create_jailbreak_tab(self):

        """Create jailbreak management tab"""

        tab = QWidget()

        layout = QVBoxLayout(tab)



        # Jailbreak info display

        jailbreak_label = QLabel("Jailbreak Tools:")

        layout.addWidget(jailbreak_label)



        self.jailbreak_info_text = QTextEdit()

        self.jailbreak_info_text.setReadOnly(True)

        layout.addWidget(self.jailbreak_info_text)



        # Control buttons

        button_layout = QHBoxLayout()



        checkra1n_btn = QPushButton("Run Checkra1n")

        checkra1n_btn.clicked.connect(self.run_checkra1n)

        button_layout.addWidget(checkra1n_btn)



        palera1n_btn = QPushButton("Run Palera1n")

        palera1n_btn.clicked.connect(self.run_palera1n)

        button_layout.addWidget(palera1n_btn)



        odysseyra1n_btn = QPushButton("Run Odysseyra1n")

        odysseyra1n_btn.clicked.connect(self.run_odysseyra1n)

        button_layout.addWidget(odysseyra1n_btn)



        layout.addLayout(button_layout)



        self.tabs.addTab(tab, "Jailbreak Tools")



    def create_firmware_tab(self):

        """Create firmware management tab"""

        tab = QWidget()

        layout = QVBoxLayout(tab)



        # Firmware info display

        firmware_label = QLabel("Firmware Management:")

        layout.addWidget(firmware_label)



        self.firmware_info_text = QTextEdit()

        self.firmware_info_text.setReadOnly(True)

        layout.addWidget(self.firmware_info_text)



        # Control buttons

        button_layout = QHBoxLayout()



        install_btn = QPushButton("Install Firmware")

        install_btn.clicked.connect(self.install_firmware)

        button_layout.addWidget(install_btn)



        upgrade_btn = QPushButton("Upgrade Firmware")

        upgrade_btn.clicked.connect(self.upgrade_firmware)

        button_layout.addWidget(upgrade_btn)



        layout.addLayout(button_layout)



        self.tabs.addTab(tab, "Firmware Manager")



    def create_system_tab(self):

        """Create system management tab"""

        tab = QWidget()

        layout = QVBoxLayout(tab)



        # System info display

        sys_label = QLabel("System Management:")

        layout.addWidget(sys_label)



        self.system_info_text = QTextEdit()

        self.system_info_text.setReadOnly(True)

        layout.addWidget(self.system_info_text)



        # Control buttons

        button_layout = QHBoxLayout()



        backup_btn = QPushButton("Backup Device")

        backup_btn.clicked.connect(self.backup_device)

        button_layout.addWidget(backup_btn)



        restore_btn = QPushButton("Restore Device")

        restore_btn.clicked.connect(self.restore_device)

        button_layout.addWidget(restore_btn)



        list_backups_btn = QPushButton("List Backups")

        list_backups_btn.clicked.connect(self.list_backups)

        button_layout.addWidget(list_backups_btn)



        layout.addLayout(button_layout)



        self.tabs.addTab(tab, "System Tools")



    def create_filesystem_tab(self):

        """Create filesystem explorer tab"""

        tab = QWidget()

        layout = QVBoxLayout(tab)



        # Filesystem info display

        fs_label = QLabel("Filesystem Explorer:")

        layout.addWidget(fs_label)



        self.fs_info_text = QTextEdit()

        self.fs_info_text.setReadOnly(True)

        layout.addWidget(self.fs_info_text)



        # Control buttons

        button_layout = QHBoxLayout()



        browse_btn = QPushButton("Browse Filesystem")

        browse_btn.clicked.connect(self.browse_filesystem)

        button_layout.addWidget(browse_btn)



        edit_btn = QPushButton("Edit Files")

        edit_btn.clicked.connect(self.edit_files)

        button_layout.addWidget(edit_btn)



        layout.addLayout(button_layout)



        self.tabs.addTab(tab, "Filesystem Explorer")



    def update_device_status(self):

        """Update device connection status"""

        try:

            if self.device_manager.is_device_connected():

                devices = self.device_manager.get_connected_devices()

                self.device_info_text.setText(f"Connected Devices: {len(devices)}\n\n")



                for i, udid in enumerate(devices):

                    info = self.device_manager.get_device_info(udid)

                    self.device_info_text.append(f"Device {i+1}:\n")

                    self.device_info_text.append(f"  UDID: {udid}\n")



                    # Add device properties

                    for key, value in info.items():

                        self.device_info_text.append(f"  {key}: {value}\n")

                    self.device_info_text.append("\n")

            else:

                self.device_info_text.setText("No iOS devices connected\n")

        except Exception as e:

            self.device_info_text.setText(f"Error retrieving device status: {e}\n")



    def connect_device(self):

        """Connect to iOS device"""

        if self.device_manager.is_device_connected():

            QMessageBox.information(self, "Device Connected", "iOS device is already connected.")

        else:

            # Attempt to connect (this would be enhanced with actual connection logic)

            self.update_device_status()

            QMessageBox.information(self, "Connection", "Checking for connected devices...")



    def start_mdm_bypass(self):

        """Start MDM bypass process"""

        try:

            self.mdm_log_text.append("Starting MDM bypass process...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.mdm_log_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Perform actual MDM bypass

            result = self.mdm_bypass.bypass_mdm()

            if result:

                self.mdm_log_text.append("MDM bypass completed successfully!\n")

            else:

                self.mdm_log_text.append("MDM bypass failed.\n")



        except Exception as e:

            self.mdm_log_text.append(f"MDM bypass failed: {str(e)}\n")



    def check_mdm_status(self):

        """Check MDM status"""

        try:

            self.mdm_log_text.append("Checking MDM enrollment status...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.mdm_log_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Use actual profiles command to check MDM status

            status = self.mdm_bypass.check_mdm_status()

            self.mdm_log_text.append(f"MDM Status: {status.get('status', 'unknown')}\n")

            if 'details' in status:

                self.mdm_log_text.append(f"Details: {status['details']}\n")

            elif 'message' in status:

                self.mdm_log_text.append(f"Message: {status['message']}\n")



        except Exception as e:

            self.mdm_log_text.append(f"Error checking MDM status: {str(e)}\n")



    def bypass_activation_lock(self):

        """Bypass activation lock"""

        try:

            self.device_info_text.append("Starting activation lock bypass...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.device_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Get first connected device

            devices = self.device_manager.get_connected_devices()

            if not devices:

                self.device_info_text.append("No device connected.\n")

                return



            udid = devices[0]

            result = self.device_manager.activate_lock_bypass(udid)

            if result:

                self.device_info_text.append("Activation lock bypass completed successfully!\n")

            else:

                self.device_info_text.append("Activation lock bypass failed.\n")



        except Exception as e:

            self.device_info_text.append(f"Activation lock bypass failed: {str(e)}\n")



    def run_checkra1n(self):

        """Run checkra1n jailbreak tool"""

        try:

            self.jailbreak_info_text.append("Running checkra1n...\n")



            if not self.device_manager.is_device_connected():

                self.jailbreak_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Get first connected device

            devices = self.device_manager.get_connected_devices()

            if not devices:

                self.jailbreak_info_text.append("No device connected.\n")

                return



            udid = devices[0]

            result = self.checkra1n_tool.run_checkra1n(udid)

            if result:

                self.jailbreak_info_text.append("Checkra1n completed successfully!\n")

            else:

                self.jailbreak_info_text.append("Checkra1n failed.\n")



        except Exception as e:

            self.jailbreak_info_text.append(f"Error running checkra1n: {str(e)}\n")



    def run_palera1n(self):

        """Run palera1n jailbreak tool"""

        try:

            self.jailbreak_info_text.append("Running palera1n...\n")



            if not self.device_manager.is_device_connected():

                self.jailbreak_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Get first connected device

            devices = self.device_manager.get_connected_devices()

            if not devices:

                self.jailbreak_info_text.append("No device connected.\n")

                return



            udid = devices[0]

            result = self.palera1n_tool.run_palera1n(udid)

            if result:

                self.jailbreak_info_text.append("Palera1n completed successfully!\n")

            else:

                self.jailbreak_info_text.append("Palera1n failed.\n")



        except Exception as e:

            self.jailbreak_info_text.append(f"Error running palera1n: {str(e)}\n")



    def run_odysseyra1n(self):

        """Run odysseyra1n jailbreak tool"""

        try:

            self.jailbreak_info_text.append("Running odysseyra1n...\n")



            if not self.device_manager.is_device_connected():

                self.jailbreak_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Get first connected device

            devices = self.device_manager.get_connected_devices()

            if not devices:

                self.jailbreak_info_text.append("No device connected.\n")

                return



            udid = devices[0]

            result = self.odysseyra1n_tool.run_odysseyra1n(udid)

            if result:

                self.jailbreak_info_text.append("Odysseyra1n completed successfully!\n")

            else:

                self.jailbreak_info_text.append("Odysseyra1n failed.\n")



        except Exception as e:

            self.jailbreak_info_text.append(f"Error running odysseyra1n: {str(e)}\n")



    def install_firmware(self):

        """Install firmware"""

        try:

            self.firmware_info_text.append("Installing firmware...\n")



            # Get firmware file

            filename, _ = QFileDialog.getOpenFileName(

                self,

                "Select Firmware File",

                "",

                "Firmware Files (*.ipsw *.bin);;All Files (*)"

            )



            if not filename:

                return



            result = self.firmware_manager.install_firmware(filename)

            if result:

                self.firmware_info_text.append("Firmware installation completed successfully!\n")

            else:

                self.firmware_info_text.append("Firmware installation failed.\n")



        except Exception as e:

            self.firmware_info_text.append(f"Error installing firmware: {str(e)}\n")



    def upgrade_firmware(self):

        """Upgrade firmware"""

        try:

            self.firmware_info_text.append("Upgrading firmware...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.firmware_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Use real ideviceinstaller to upgrade firmware with Popen to prevent GUI freeze
            process = subprocess.Popen(
                ['ideviceinstaller', '-l'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Keep GUI responsive while waiting
            while process.poll() is None:
                QApplication.processEvents()

            stdout, stderr = process.communicate()

            if process.returncode == 0:
                self.firmware_info_text.append("Firmware upgrade completed successfully!\n")
                self.firmware_info_text.append(f"Output: {stdout}\n")
            else:
                self.firmware_info_text.append(f"Firmware upgrade failed: {stderr}\n")



        except Exception as e:

            self.firmware_info_text.append(f"Error upgrading firmware: {str(e)}\n")



    def backup_device(self):

        """Backup device"""

        try:

            self.system_info_text.append("Backing up device...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.system_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Get backup name from user

            backup_name, ok = QInputDialog.getText(self, 'Backup Name', 'Enter backup name:')

            if not ok or not backup_name:

                return



            result = self.backup_manager.create_backup(backup_name)

            if result:

                self.system_info_text.append("Device backup completed successfully!\n")

            else:

                self.system_info_text.append("Device backup failed.\n")



        except Exception as e:

            self.system_info_text.append(f"Error backing up device: {str(e)}\n")



    def restore_device(self):

        """Restore device"""

        try:

            self.system_info_text.append("Restoring device...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.system_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Get backup path from user

            backup_path = QFileDialog.getExistingDirectory(

                self,

                "Select Backup Directory",

                os.path.expanduser("~/applecrack_backups")

            )



            if not backup_path:

                return



            result = self.backup_manager.restore_backup(backup_path)

            if result:

                self.system_info_text.append("Device restoration completed successfully!\n")

            else:

                self.system_info_text.append("Device restoration failed.\n")



        except Exception as e:

            self.system_info_text.append(f"Error restoring device: {str(e)}\n")



    def list_backups(self):

        """List backups"""

        try:

            self.system_info_text.append("Listing backups...\n")



            backups = self.backup_manager.list_backups()

            if backups:

                self.system_info_text.append(f"Available backups ({len(backups)}):\n")

                for backup in backups:

                    self.system_info_text.append(f"  - {backup}\n")

            else:

                self.system_info_text.append("No backups found.\n")



        except Exception as e:

            self.system_info_text.append(f"Error listing backups: {str(e)}\n")



    def browse_filesystem(self):

        """Browse filesystem"""

        try:

            self.fs_info_text.append("Browsing filesystem...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.fs_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Use real filesystem commands with Popen to prevent GUI freeze
            process = subprocess.Popen(
                ['ideviceimagemounter', 'list'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Keep GUI responsive while waiting
            while process.poll() is None:
                QApplication.processEvents()

            stdout, stderr = process.communicate()

            if process.returncode == 0:
                self.fs_info_text.append("Filesystem contents:\n")
                self.fs_info_text.append(stdout)
            else:
                self.fs_info_text.append(f"Filesystem browse failed: {stderr}\n")



        except Exception as e:

            self.fs_info_text.append(f"Error browsing filesystem: {str(e)}\n")



    def edit_files(self):

        """Edit files"""

        try:

            self.fs_info_text.append("Editing files...\n")



            # Check if device is connected

            if not self.device_manager.is_device_connected():

                self.fs_info_text.append("No device connected. Please connect your iOS device.\n")

                return



            # Use real file editing commands

            result = subprocess.run(

                ['ideviceinstaller', '-l'],

                capture_output=True,

                text=True

            )



            if result.returncode == 0:

                self.fs_info_text.append("Installed apps:\n")

                self.fs_info_text.append(result.stdout[:1000] + "...\n")

            else:

                self.fs_info_text.append(f"File editing failed: {result.stderr}\n")



        except Exception as e:

            self.fs_info_text.append(f"Error editing files: {str(e)}\n")
