#!/usr/bin/env python3
"""Device management commands for CLI."""

from applecrack_ng.core.device_manager import DeviceManager

def list_devices():
    """List connected devices."""
    manager = DeviceManager()
    devices = manager.get_connected_devices()

    print(f"Connected devices: {len(devices)}")
    for i, udid in enumerate(devices):
        info = manager.get_device_info(udid)
        print(f"  Device {i+1}: {udid}")

def connect_device(udid):
    """Connect to specific device."""
    manager = DeviceManager()

    # In a real implementation we'd actually attempt connection
    print(f"Connecting to device: {udid}")
    if manager.is_device_connected():
        print("Device is connected")
    else:
        print("Device not found or not connected")
