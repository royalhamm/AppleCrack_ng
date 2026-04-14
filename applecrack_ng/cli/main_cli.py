#!/usr/bin/env python3

"""

Command-line interface for AppleCrack_NG.

"""



import argparse

import sys

import os

from applecrack_ng.core.device_manager import DeviceManager

from applecrack_ng.tools.mdm_bypass import MDMBypass

from applecrack_ng.tools.backup_restore import BackupRestoreManager

from applecrack_ng.tools.firmware_manager import FirmwareManager



def print_help():

    """Print help information."""

    help_text = """

AppleCrack_NG CLI Interface



Available commands:

  device list                    List connected devices

  device connect <udid>          Connect to a specific device

  bypass-mdm                     Bypass MDM settings

  bypass-activation-lock         Bypass activation lock

  jailbreak checkra1n            Run checkra1n jailbreak tool

  jailbreak palera1n             Run palera1n jailbreak tool

  jailbreak odysseyra1n          Run odysseyra1n jailbreak tool

  firmware install <file>        Install firmware from file

  backup create <name>           Create device backup

  backup list                    List available backups

  restore <backup_path>          Restore device from backup



Options:

  -h, --help                     Show this help message

  -v, --verbose                  Enable verbose output



Examples:

  applecrack_ng device list

  applecrack_ng bypass-mdm

  applecrack_ng jailbreak checkra1n

  applecrack_ng backup create my_backup



"""

    print(help_text)



def main():

    """Main CLI function."""



    parser = argparse.ArgumentParser(description='AppleCrack_NG - iOS Management Tool')
    parser.add_argument('command', nargs='*', help='Command to execute')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--gui', action='store_true', help='Launch the graphical user interface')

    args = parser.parse_args()

    if args.gui:
        import subprocess
        # Get path to main.py at the project root
        main_script = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'main.py'))
        if os.path.exists(main_script):
            subprocess.Popen([sys.executable, main_script])
        else:
            print(f"Error: GUI component not found at {main_script}")
        return




    # If no command specified, show help

    if not args.command:

        print_help()

        return



    device_manager = DeviceManager()

    mdm_bypass = MDMBypass()

    backup_manager = BackupRestoreManager()

    firmware_manager = FirmwareManager()



    try:

        command = args.command[0]



        if command == 'device' and len(args.command) > 1:

            subcommand = args.command[1]



            if subcommand == 'list':

                devices = device_manager.get_connected_devices()

                print(f"Connected devices: {len(devices)}")

                for i, udid in enumerate(devices):

                    info = device_manager.get_device_info(udid)

                    print(f"  Device {i+1}: {udid}")

                    # Print key properties

                    for k, v in list(info.items())[:3]:  # Show first 3 properties

                        print(f"    {k}: {v}")



            elif subcommand == 'connect':

                if len(args.command) > 2:

                    device_udid = args.command[2]

                    print(f"Connecting to device: {device_udid}")

                    # Implementation would go here

                    print("Connection logic completed")

                else:

                    print("Please specify a device UDID to connect.")



        elif command == 'bypass-mdm':

            print("Initiating MDM bypass...")

            if not device_manager.is_device_connected():

                print("Error: No device connected")

                return

            result = mdm_bypass.bypass_mdm()

            if result:

                print("MDM bypass completed successfully!")

            else:

                print("MDM bypass failed.")



        elif command == 'bypass-activation-lock':

            print("Bypassing activation lock...")

            if not device_manager.is_device_connected():

                print("Error: No device connected")

                return

            # Use actual implementation

            devices = device_manager.get_connected_devices()

            if devices:

                result = device_manager.activate_lock_bypass(devices[0])

                if result:

                    print("Activation lock bypass completed successfully!")

                else:

                    print("Activation lock bypass failed.")

            else:

                print("No devices found")



        elif command == 'jailbreak' and len(args.command) > 1:

            tool = args.command[1]

            if not device_manager.is_device_connected():

                print("Error: No device connected")

                return



            if tool == 'checkra1n':

                print("Running checkra1n tool...")

                from applecrack_ng.tools.jailbreak_tools.checkra1n import Checkra1nTool

                checkra1n = Checkra1nTool()

                devices = device_manager.get_connected_devices()

                if devices:

                    result = checkra1n.run_checkra1n(devices[0])

                    if result:

                        print("Checkra1n completed successfully!")

                    else:

                        print("Checkra1n failed.")

                else:

                    print("No devices found")

            elif tool == 'palera1n':

                print("Running palera1n tool...")

                from applecrack_ng.tools.jailbreak_tools.palera1n import Palera1nTool

                palera1n = Palera1nTool()

                devices = device_manager.get_connected_devices()

                if devices:

                    result = palera1n.run_palera1n(devices[0])

                    if result:

                        print("Palera1n completed successfully!")

                    else:

                        print("Palera1n failed.")

                else:

                    print("No devices found")

            elif tool == 'odysseyra1n':

                print("Running odysseyra1n tool...")

                from applecrack_ng.tools.jailbreak_tools.odysseyra1n import Odysseyra1nTool

                odysseyra1n = Odysseyra1nTool()

                devices = device_manager.get_connected_devices()

                if devices:

                    result = odysseyra1n.run_odysseyra1n(devices[0])

                    if result:

                        print("Odysseyra1n completed successfully!")

                    else:

                        print("Odysseyra1n failed.")

                else:

                    print("No devices found")



        elif command == 'firmware' and len(args.command) > 1:

            subcommand = args.command[1]



            if subcommand == 'install':

                if len(args.command) > 2:

                    firmware_file = args.command[2]

                    if not os.path.exists(firmware_file):

                        print(f"Error: Firmware file not found: {firmware_file}")

                        return

                    print(f"Installing firmware from: {firmware_file}")

                    result = firmware_manager.install_firmware(firmware_file)

                    if result:

                        print("Firmware installation completed successfully!")

                    else:

                        print("Firmware installation failed.")

                else:

                    print("Please specify firmware file to install.")



        elif command == 'backup' and len(args.command) > 1:

            subcommand = args.command[1]



            if subcommand == 'create':

                if len(args.command) > 2:

                    backup_name = args.command[2]

                    print(f"Creating backup named: {backup_name}")

                    result = backup_manager.create_backup(backup_name)

                    if result:

                        print("Backup creation completed successfully!")

                    else:

                        print("Backup creation failed.")

                else:

                    print("Please specify backup name.")



            elif subcommand == 'list':

                print("Listing backups...")

                backups = backup_manager.list_backups()

                if backups:

                    print(f"Available backups ({len(backups)}):")

                    for backup in backups:

                        print(f"  - {backup}")

                else:

                    print("No backups found.")



        elif command == 'restore' and len(args.command) > 1:

            backup_path = args.command[1]

            if not os.path.exists(backup_path):

                print(f"Error: Backup path not found: {backup_path}")

                return

            print(f"Restoring from backup: {backup_path}")

            result = backup_manager.restore_backup(backup_path)

            if result:

                print("Restore completed successfully!")

            else:

                print("Restore failed.")



        else:

            print_help()



    except Exception as e:

        print(f"Error executing command: {e}")

        if args.verbose:

            import traceback

            traceback.print_exc()



if __name__ == '__main__':

    main()
