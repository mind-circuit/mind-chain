"""
test_bridge.py

Unit tests for the bridging logic in mind_chain.bridge.
"""
import unittest
from mind_chain.bridge.bridge_manager import BridgeManager

class TestBridgeManager(unittest.TestCase):

    def setUp(self):
        self.manager = BridgeManager("http://sui.local", "http://poa.local")

    def test_cross_chain_operation(self):
        result = self.manager.cross_chain_operation("mock_sui_contract", "mock_validator")
        self.assertIn("sui_state", result)
        self.assertIn("aggregated_data", result)
        self.assertIn("ai_insights", result)
        self.assertIn("cosmos_result", result)

    def test_check_cosmos_validator(self):
        status = self.manager.check_cosmos_validator("validator_1")
        self.assertIn("validator_status", status)
        self.assertIn("analysis", status)

    def test_advanced_cross_chain_sync(self):
        sync_result = self.manager.advanced_cross_chain_sync("mock_sui_contract")
        self.assertIn("sui_state", sync_result)
        self.assertIn("aggregator_result", sync_result)
        self.assertIn("ai_output", sync_result)

if __name__ == '__main__':
    unittest.main()
