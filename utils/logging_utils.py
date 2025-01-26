"""
logging_utils.py

Configures logging for Mind Chain.
"""

import logging

def setup_logging(level=logging.DEBUG):
    """
    Sets up a basic logging configuration.

    :param level: e.g., logging.DEBUG or logging.INFO
    """
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=level
    )
