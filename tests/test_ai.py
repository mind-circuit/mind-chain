"""
test_ai.py

Unit tests for the AI module in mind_chain.ai
"""
import unittest
from mind_chain.ai.ai_agent import MindChainAIAgent

class TestAIAgent(unittest.TestCase):

    def setUp(self):
        self.agent = MindChainAIAgent()

    def test_analyze_data(self):
        data = {"transaction_value": 1000, "user": "test_user"}
        result = self.agent.analyze_data(data)
        self.assertIn("severity_score", result)
        self.assertIn("recommendation", result)

    def test_generate_report(self):
        analysis = {
            "agent_name": "UnitTestAI",
            "severity_score": 0.4,
            "recommendation": "approve",
            "notes": "Test analysis"
        }
        report = self.agent.generate_report(analysis)
        self.assertIn("AI Analysis Report", report)
        self.assertIn("approve", report)

    def test_advanced_model_simulation(self):
        features = {"some_feature": 42}
        output = self.agent.advanced_model_simulation(features, "UnitTestModel")
        self.assertIn("model", output)
        self.assertIn("confidence", output)
        self.assertIn("prediction", output)

if __name__ == '__main__':
    unittest.main()
