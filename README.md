# AppleCrack_NG - Next Generation iOS Device Management Tool

AppleCrack_NG is a comprehensive security auditing tool designed for managing and exploiting iOS/macOS devices in authorized penetration testing environments.

## 📋 Features

- **Device Management**: Connect, identify, and manage connected iOS devices
- **MDM Bypass**: Remove Mobile Device Management restrictions from devices
- **Activation Lock Bypass**: Remove iCloud activation locks 
- **Jailbreaking Tools Integration**:
  - Checkra1n jailbreak tool
  - Palera1n jailbreak tool  
  - Odysseyra1n jailbreak tool
- **Firmware Management**: Install and update device firmware
- **Backup/Restore**: Create backups and restore devices from previous states
- **Filesystem Explorer**: Browse connected device filesystems with root access
- **SSH Integration**: Secure shell connectivity to iOS devices
- **Command Line Interface**: Full CLI support for automation
- **GUI Interface**: User-friendly PyQt5-based graphical interface

## 🛠️ Requirements

AppleCrack_NG requires:
- BlackArch Linux (with Chaotic-AUR Repository)
- KDE Plasma Desktop Environment  
- Intel Processor
- USB access for iOS device connections  
- Required packages from Arch, BlackArch, and Chaotic-AUR repositories

## 📦 Installation

### System Requirements:
```bash
sudo pacman -Syyu --needed --noconfirm

# Basic system tools and Python components compatible with BlackArch Linux
pacman -S --needed --noconfirm \
    python-pip python-setuptools python-wheel \
    qt5-base qt5-tools qt5-declarative pyqt5 \
    libimobiledevice libusbmuxd \
    libusb usbutils \
    openssh openssl \
    git curl wget unzip tar gzip bzip2 \
    python-requests python-click python-tqdm python-colorama \
    python-pyusb python-pillow metasploit

# Install from Chaotic-AUR repository if available
    yay -S --needed --noconfirm checkra1n palera1n odysseyra1n \
        ios-deploy frida-tools mitmproxy burpsuite \
        john-the-ripper impacket pwntools cve-search nmap \
        python-frida python-lldb python-iokit-utils \
        python-armor python-fouldecrypt \
        ideviceinstaller libideviceactivation

# Install Apple_Crack_NG On Your System: Open A Terminal From The Apple_Crack_NG Project Root Directory.
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

# To Run Apple_Crack_NG Once The Installation Is Completed
  python apple_crack_ng.py
# Or
  apple_crack_ng --gui


# AppleCrack_NG CLI Interface

# Available commands:
  device list                    List connected devices
  device connect                 Connect to a specific device
  bypass-mdm                     Bypass MDM settings
  bypass-activation-lock         Bypass activation lock
  jailbreak checkra1n            Run checkra1n jailbreak tool
  jailbreak palera1n             Run palera1n jailbreak tool
  firmware install               Install firmware from file
  backup create                  Create device backup
  restore                        Restore device from backup

# Options:
  -h, --help                     Show this help message
  -v, --verbose                 Enable verbose output

# Examples:
  applecrack_ng device list
  applecrack_ng bypass-mdm
  applecrack_ng jailbreak checkra1n


