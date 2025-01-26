"""
bridge_manager.py

Orchestrates interactions between SuiConnector, CosmosPoAConnector, and aggregator/AI modules.
"""

import logging
from mind_chain.bridge.sui_connector import SuiConnector
from mind_chain.bridge.cosmos_connector import CosmosPoAConnector
from mind_chain.aggregator.aggregator_service import AggregatorService
from mind_chain.ai.ai_agent import MindChainAIAgent

logger = logging.getLogger(__name__)

class BridgeManager:
    """
    Provides a high-level API for cross-chain operations linking Sui and Cosmos-based PoA networks,
    while integrating aggregator and AI logic.
    """

    def __init__(self, sui_endpoint: str, cosmos_rpc: str):
        self.sui = SuiConnector(sui_endpoint)
        self.cosmos = CosmosPoAConnector(cosmos_rpc)
        self.aggregator = AggregatorService()
        self.ai_agent = MindChainAIAgent()
        logger.debug("BridgeManager initialized with Sui and Cosmos connectors")

    def cross_chain_operation(self, sui_contract_id: str, cosmos_validator_id: str) -> dict:
        """
        Demonstrates an example cross-chain flow:
        1. Query Sui contract state
        2. Aggregate data
        3. Run AI analysis
        4. Broadcast a transaction on Cosmos
        5. Return a combined result
        """
        logger.info("Starting cross-chain operation...")
        # Query Sui
        sui_state = self.sui.query_contract_state(sui_contract_id)

        # Aggregation
        sources = ["OracleA", "OracleB", "OracleC"]
        aggregated_data = self.aggregator.gather_data(sources)
        combined_result = self.aggregator.combine_and_validate(aggregated_data)

        # AI analysis
        ai_insights = self.ai_agent.analyze_data({
            "sui_state": sui_state,
            "aggregated_data": combined_result
        })

        # Broadcast to Cosmos
        cosmos_result = self.cosmos.broadcast_transaction({
            "validator_id": cosmos_validator_id,
            "analysis": ai_insights
        })

        final_output = {
            "sui_state": sui_state,
            "aggregated_data": combined_result,
            "ai_insights": ai_insights,
            "cosmos_result": cosmos_result
        }
        logger.info("Cross-chain operation completed.")
        return final_output

    def check_cosmos_validator(self, validator_id: str) -> dict:
        """
        Checks the status of a given Cosmos validator, optionally runs AI analysis on it.
        """
        logger.info(f"Checking validator: {validator_id}")
        validator_status = self.cosmos.query_validator_status(validator_id)
        ai_evaluation = self.ai_agent.analyze_data(validator_status)
        response = {
            "validator_status": validator_status,
            "analysis": ai_evaluation
        }
        logger.debug(f"Validator check response: {response}")
        return response

    def advanced_cross_chain_sync(self, sui_contract_id: str) -> dict:
        """
        A more advanced cross-chain routine:
        - Retrieve Sui state
        - Perform advanced aggregator logic
        - Use AI for final evaluation
        - Return a summary
        """
        logger.info("Performing advanced cross-chain sync.")
        sui_state = self.sui.query_contract_state(sui_contract_id)
        aggregator_result = self.aggregator.advanced_aggregation_routine(sui_state, threshold=0.8)
        ai_output = self.ai_agent.advanced_model_simulation(aggregator_result, model_name="SyncModel")
        summary = {
            "sui_state": sui_state,
            "aggregator_result": aggregator_result,
            "ai_output": ai_output
        }
        logger.info("Advanced cross-chain sync complete.")
        return summary

if __name__ == "__main__":
    import sys
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    manager = BridgeManager("http://sui.local", "http://poa.local")

    result_op = manager.cross_chain_operation("sui_contract_123", "validator_ABC")
    print("Cross-chain operation result:", result_op)

    sync_result = manager.advanced_cross_chain_sync("sui_contract_456")
    print("Advanced sync result:", sync_result)
