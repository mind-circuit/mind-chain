"""
sui_connector.py

Simulates interactions with the Sui blockchain.
"""

import logging

logger = logging.getLogger(__name__)

class SuiConnector:
    """
    Simulates methods to interact with a Sui-based blockchain.
    """

    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        logger.debug(f"SuiConnector initialized with endpoint: {self.endpoint}")

    def send_transaction(self, payload: dict) -> dict:
        """
        Sends a transaction to the Sui network (simulated).

        :param payload: Transaction data.
        :return: A mock response.
        """
        logger.info(f"Sending transaction to Sui at {self.endpoint} with {payload}")
        return {
            "status": "success",
            "transaction_hash": "mock_sui_tx_abc",
            "payload": payload
        }

    def query_contract_state(self, contract_id: str) -> dict:
        """
        Queries a Move contract state on Sui (simulated).

        :param contract_id: The contract identifier.
        :return: A mock contract state dictionary.
        """
        logger.debug(f"Querying Sui contract state for: {contract_id}")
        return {
            "contract_id": contract_id,
            "balance": 1000,
            "owner": "0xSUIOwner"
        }
