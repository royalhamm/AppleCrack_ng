import sys
import os

# Allow running directly by adding parent project to path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from applecrack_ng.cli.main_cli import main

if __name__ == '__main__':
    sys.exit(main())
