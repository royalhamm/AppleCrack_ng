import logging

import os



def setup_logger():

    """Setup centralized logger for the application."""



    # Create logs directory if it doesn't exist
    log_dir = os.path.expanduser('~/.config/applecrack_ng/logs')
    os.makedirs(log_dir, exist_ok=True)



    # Setup logging configuration

    logging.basicConfig(

        level=logging.INFO,

        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

        handlers=[

            logging.FileHandler(os.path.join(log_dir, 'app.log')),

            logging.StreamHandler()

        ]

    )



    return logging.getLogger(__name__)



# Also export the logger

logger = setup_logger()
