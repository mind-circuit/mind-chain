"""
aggregator_service.py

Fetches data from multiple sources and merges/validates the results.
"""

import time
import logging
import random

logger = logging.getLogger(__name__)

class AggregatorService:
    """
    Merges data from multiple sources (APIs, on-chain data, or oracles) and returns results.
    """

    def __init__(self):
        self.name = "MindChainAggregator"
        logger.debug(f"AggregatorService '{self.name}' initialized")

    def gather_data(self, sources: list) -> dict:
        """
        Gather data from multiple sources.

        :param sources: A list of identifiers (e.g. oracles, APIs).
        :return: A dict with source -> simulated data.
        """
        data_collected = {}
        for src in sources:
            simulated_data = f"Simulated data from {src}"
            data_collected[src] = simulated_data
            logger.debug(f"Gathered data from {src}")
        return data_collected

    def combine_and_validate(self, data_dict: dict) -> dict:
        """
        Combine the collected data and mark it as valid/invalid at random.

        :param data_dict: Source -> data dictionary.
        :return: A dict with a combined string, timestamp, and validation status.
        """
        combined = " | ".join(data_dict.values())
        valid = "valid" if random.random() > 0.1 else "invalid"
        result = {
            "combined_data": combined,
            "timestamp": time.time(),
            "status": valid
        }
        logger.info(f"Combined data result: {result}")
        return result

    def advanced_aggregation_routine(self, data_dict: dict, threshold: float = 0.5) -> dict:
        """
        Demonstrates a more involved aggregation routine with threshold-based logic.

        :param data_dict: Data to aggregate.
        :param threshold: A threshold for additional validation or transformation.
        :return: A dictionary with results of advanced aggregation.
        """
        logger.debug(f"Running advanced aggregation with threshold={threshold}")
        total_length = sum(len(v) for v in data_dict.values())
        evaluation = "EXCEEDS_THRESHOLD" if total_length > threshold * 100 else "BELOW_THRESHOLD"
        advanced_result = {
            "aggregated_length": total_length,
            "evaluation": evaluation,
            "original_data": data_dict
        }
        logger.info(f"Advanced aggregation result: {advanced_result}")
        return advanced_result

if __name__ == "__main__":
    import sys
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    aggregator = AggregatorService()
    data = aggregator.gather_data(["OracleA", "OracleB"])
    combined = aggregator.combine_and_validate(data)
    print("Combined data:", combined)
    adv_agg = aggregator.advanced_aggregation_routine(data, threshold=0.7)
    print("Advanced aggregation:", adv_agg)
