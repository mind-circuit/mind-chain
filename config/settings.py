"""
settings.py

Illustrates how to load environment variables or other configuration settings.
"""

import os
import logging

logger = logging.getLogger(__name__)

SUI_ENDPOINT = os.getenv("SUI_ENDPOINT", "http://sui.local")
COSMOS_RPC = os.getenv("COSMOS_RPC", "http://poa.local")
AI_MODEL_NAME = os.getenv("AI_MODEL_NAME", "DefaultModel")

logger.info(
    f"Settings loaded: SUI_ENDPOINT={SUI_ENDPOINT}, COSMOS_RPC={COSMOS_RPC}, AI_MODEL_NAME={AI_MODEL_NAME}"
)
