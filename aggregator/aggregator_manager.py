"""
aggregator_manager.py

Demonstrates managing multiple aggregator services within Mind Chain.
"""

import logging
from mind_chain.aggregator.aggregator_service import AggregatorService

logger = logging.getLogger(__name__)

class AggregatorManager:
    """
    Orchestrates multiple aggregator services, simulating scenarios where different
    aggregator nodes might specialize in different data types or sources.
    """

    def __init__(self, aggregator_count: int = 2):
        self.aggregators = [AggregatorService() for _ in range(aggregator_count)]
        logger.debug(f"Initialized AggregatorManager with {aggregator_count} aggregator(s).")

    def fetch_from_all(self, global_sources: list) -> dict:
        """
        Splits the global sources among the aggregator instances, merges results.

        :param global_sources: A list of all sources we want to query.
        :return: A combined dictionary of aggregator_name -> aggregator result.
        """
        result = {}
        # For demonstration, let's split the sources evenly.
        chunk_size = max(1, len(global_sources) // len(self.aggregators))
        start_idx = 0

        for idx, aggregator in enumerate(self.aggregators):
            chunk = global_sources[start_idx:start_idx+chunk_size]
            start_idx += chunk_size
            partial_data = aggregator.gather_data(chunk)
            combined = aggregator.combine_and_validate(partial_data)
            result[f"aggregator_{idx}"] = combined
            logger.debug(f"Aggregator {idx} processed chunk: {chunk}")

        return result

if __name__ == "__main__":
    import sys
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    manager = AggregatorManager(aggregator_count=3)
    global_sources = ["OracleA", "OracleB", "OracleC", "OracleD", "OracleE"]
    result = manager.fetch_from_all(global_sources)
    print("Aggregator Manager result:", result)
