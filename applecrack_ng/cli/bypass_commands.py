#!/usr/bin/env python3

"""Bypass commands for CLI."""



from applecrack_ng.tools.mdm_bypass import MDMBypass

import logging



# Setup basic logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)



def bypass_mdm():

    """Perform MDM bypass."""

    bypass = MDMBypass()

    logger.info("Starting MDM bypass...")

    try:

        result = bypass.bypass_mdm()

        if result:

            logger.info("MDM bypass completed successfully!")

        else:

            logger.error("MDM bypass failed.")

    except Exception as e:

        logger.error(f"Error during MDM bypass: {e}")



def check_mdm_status():

    """Check MDM status."""

    bypass = MDMBypass()

    logger.info("Checking MDM status...")

    try:

        status = bypass.check_mdm_status()

        logger.info(f"MDM Status: {status}")

    except Exception as e:

        logger.error(f"Error checking MDM status: {e}")
