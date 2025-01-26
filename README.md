# Mind Chain

**Mind Chain** is an advanced bridging framework that integrates Sui (Move-based) smart contracts 
with a Cosmos-based PoA (Proof of Authority) system. It includes:

- **AI-based insights** for on-chain decisions
- **Aggregator endpoints** to gather data from multiple sources
- **Configuration** via environment variables or config files
- **Docker-based** deployment for easy setup

## Project Overview

- **Sui Integration**: Sui-based Move contracts can invoke logic on Mind Chain to leverage AI agents and aggregator services.
- **Cosmos/PoA Integration**: The Cosmos-based PoA chain runs validators that handle AI or aggregator logic, bridging data and transaction flows.
- **AI & Aggregator**: Our specialized AI module provides on-chain intelligence or aggregator endpoints.
- **Cross-Chain Orchestration**: DeFi workflows, data validation, or specialized computations can run across both the Sui and Cosmos networks.
- **Docker-Ready**: A `Dockerfile` is included for container-based deployment.

## Repository Structure

```
mind_chain/
├── ai/
│   ├── __init__.py
│   └── ai_agent.py
├── aggregator/
│   ├── __init__.py
│   ├── aggregator_service.py
│   └── aggregator_manager.py
├── bridge/
│   ├── __init__.py
│   ├── cosmos_connector.py
│   ├── sui_connector.py
│   └── bridge_manager.py
├── cli/
│   ├── __init__.py
│   └── mindchain_cli.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── contracts/
│   ├── move/
│   │   └── sui_example.move
│   └── cosmos_poa_demo.md
├── scripts/
│   └── deploy_demo.sh
├── tests/
│   ├── __init__.py
│   ├── test_bridge.py
│   └── test_ai.py
├── utils/
│   ├── __init__.py
│   └── logging_utils.py
├── Dockerfile
├── __init__.py
├── requirements.txt
└── setup.py
```

## Getting Started

1. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run** the CLI:
   ```bash
   python -m mind_chain.cli.mindchain_cli
   ```
3. **Test** the project:
   ```bash
   pytest mind_chain/tests
   ```
4. **Build** the Docker image (optional):
   ```bash
   docker build -t mind_chain:latest .
   ```

## Interoperability Approach

Mind Chain uses:
- **Sui `Move` contracts**: Call external endpoints via aggregator or AI modules.
- **Cosmos-based PoA**: Uses `cosmos_connector.py` to reach a PoA node and relay transactions.
- **AI & Aggregator**: Provide data processing and AI-based decision-making.
- **`BridgeManager`**: Orchestrates cross-chain calls, aggregator usage, and AI analysis.

### Example Flow

1. A Sui contract sends a request to the aggregator endpoint.
2. The aggregator fetches data from external or on-chain sources.
3. The AI module processes the data, returning insights or decisions.
4. The Cosmos PoA chain may store or validate the result, returning confirmations.
5. The aggregator responds to the Sui contract with final data or triggers a follow-up transaction.

## Configuration

- **Environment Variables**: `.env` or set in your environment. Access via `mind_chain.config.settings`.
- **Logging**: Configured in `mind_chain.utils.logging_utils`.

## License

MIT License - For demonstration purposes only.
