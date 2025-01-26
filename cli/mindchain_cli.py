"""
mindchain_cli.py

A CLI for the Mind Chain bridging demo. Uses argparse to illustrate
cross-chain operations from the command line.
"""

import argparse
import logging
import sys
from mind_chain.bridge.bridge_manager import BridgeManager

def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    parser = argparse.ArgumentParser(description="Mind Chain CLI - bridging Sui & Cosmos-based PoA.")
    parser.add_argument("--sui-endpoint", type=str, default="http://sui.local",
                        help="Endpoint for the Sui network.")
    parser.add_argument("--cosmos-rpc", type=str, default="http://poa.local",
                        help="RPC endpoint for the Cosmos-based PoA chain.")
    parser.add_argument("--operation", type=str,
                        choices=["cross-chain", "check-validator", "adv-sync"],
                        default="cross-chain",
                        help="Which operation to perform.")
    parser.add_argument("--sui-contract-id", type=str, default="sui_contract_123",
                        help="Contract ID on Sui to query.")
    parser.add_argument("--validator-id", type=str, default="validator_1",
                        help="Validator ID on the PoA chain to check.")

    args = parser.parse_args()
    manager = BridgeManager(args.sui_endpoint, args.cosmos_rpc)

    if args.operation == "cross-chain":
        result = manager.cross_chain_operation(args.sui_contract_id, args.validator_id)
        print("Cross-chain operation result:", result)
    elif args.operation == "check-validator":
        result = manager.check_cosmos_validator(args.validator_id)
        print("Validator check result:", result)
    elif args.operation == "adv-sync":
        result = manager.advanced_cross_chain_sync(args.sui_contract_id)
        print("Advanced cross-chain sync result:", result)

if __name__ == "__main__":
    main()
