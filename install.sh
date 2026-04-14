#!/bin/bash

# AppleCrack_NG Installation Script for BlackArch Linux
# This script installs all dependencies and sets up the application.

set -e  # Exit on any error

echo "Installing AppleCrack_NG - Next Generation iOS Management Tool"
echo "================================================================"

# Check if running as root (required for system installations)
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Please use sudo."
   exit 1
fi

# Update package database first
echo "[+] Updating package database..."
pacman -Syu --needed --noconfirm

# Install required packages from BlackArch/CachyOS/Chaotic-AUR repositories
echo "[+] Installing required dependencies..."

# Basic system tools and Python components compatible with BlackArch Linux
pacman -S --needed --noconfirm \
    python-pip python-setuptools python-wheel \
    qt5-base qt5-tools qt5-declarative pyqt5 \
    libimobiledevice libusbmuxd \
    libusb usbutils \
    openssh openssl \
    git curl wget unzip tar gzip bzip2 \
    python-requests python-click python-tqdm python-colorama \
    python-pyusb python-pillow

# Install from Chaotic-AUR repository if available
echo "[+] Installing additional packages from Chaotic-AUR..."
if pacman -Qi chaotic-cachyos-keyring &>/dev/null; then
    yay -S --needed --noconfirm checkra1n palera1n odysseyra1n \
        ios-deploy frida-tools mitmproxy burpsuite \
        john-the-ripper impacket pwntools cve-search nmap \
        python-frida python-lldb python-iokit-utils \
        python-armor python-fouldecrypt \
        ideviceinstaller libideviceactivation
else
    echo "Chaotic-AUR repository not found. Installing basic tools..."
fi

# Install Metasploit Framework
echo "[+] Installing Metasploit Framework..."
pacman -S --needed --noconfirm metasploit

# Create application directory structure
echo "[+] Creating application directories..."

if [ ! -d "/opt/applecrack_ng" ]; then
    mkdir -p /opt/applecrack_ng
fi

# Create system user for AppleCrack_NG (optional but good practice)
if ! id "applecrack" &>/dev/null; then
    echo "[+] Creating applecrack user..."
    useradd -m -s /bin/bash applecrack
else
    echo "[+] applecrack user already exists."
fi

# Copy application files to installation directory
echo "[+] Installing application files..."
cp -R ./* /opt/applecrack_ng/

# We'll install the package using pip
pip3 install --upgrade pip setuptools wheel --break-system-packages || true
cd /opt/applecrack_ng
pip3 install -r requirements.txt --break-system-packages || true
pip3 install -e . --break-system-packages || true

echo "[+] Creating desktop entry..."
mkdir -p /usr/share/applications/
cat > /usr/share/applications/applecrack_ng.desktop << EOF
[Desktop Entry]
Name=AppleCrack_NG
Comment=iOS Device Management Tool
Exec=python3 /opt/applecrack_ng/main.py
Icon=applecrack-ng-icon
Terminal=false
Type=Application
Categories=System;Security;
EOF

# Create main executable script
cat > /usr/bin/applecrack-ng << 'EOF'
#!/bin/bash
export PYTHONPATH="/opt/applecrack_ng:$PYTHONPATH"
cd /opt/applecrack_ng
exec python3 -m applecrack_ng "$@"
EOF

chmod +x /usr/bin/applecrack-ng

# Set permissions for the installation directory
chown -R root:root /opt/applecrack_ng
chmod -R 755 /opt/applecrack_ng

echo "[+] Installation complete!"
echo ""
echo "To use AppleCrack_NG:"
echo "1. Connect your iOS device via USB"
echo "2. Run 'applecrack-ng' or launch from applications menu"
echo "3. Ensure that your user has access to USB devices (add to plugdev group)"
echo ""
echo "Note: You may need to add your user to the 'plugdev' group:"
echo "  sudo gpasswd -a $USER plugdev"
echo ""
echo "To get started with CLI usage, run:"
echo "  applecrack-ng --help"

exit 0
