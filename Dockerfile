# Dockerfile for Mind Chain
FROM python:3.9-slim

# Create and set the working directory
WORKDIR /app

# Copy only the requirements first (for dependency caching)
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /app

# By default, run the CLI
CMD ["python", "-m", "mind_chain.cli.mindchain_cli", "--operation", "cross-chain"]
