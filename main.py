#!/usr/bin/env python3

"""

Main entry point for AppleCrack_NG as a Python package.

"""



import sys

import os



# Add the current directory to Python path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))



from applecrack_ng.core.ui_manager import UIManager

from applecrack_ng.utils.logger import setup_logger

from PyQt5.QtWidgets import QApplication



def main():

    """Launch the GUI application."""

    # Setup logging

    setup_logger()



    # Create Qt application

    app = QApplication(sys.argv)



    # Create and show the main window

    ui_manager = UIManager()

    ui_manager.show()



    # Print success message

    print("AppleCrack_NG started successfully!")



    # Start the Qt event loop

    sys.exit(app.exec_())



if __name__ == "__main__":

    main()
