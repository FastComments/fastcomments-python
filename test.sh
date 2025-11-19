#!/bin/bash

set -e

echo "Running FastComments Python SDK tests..."

# Check required environment variables
if [ -z "$FASTCOMMENTS_API_KEY" ] || [ -z "$FASTCOMMENTS_TENANT_ID" ]; then
  echo "Error: FASTCOMMENTS_API_KEY and FASTCOMMENTS_TENANT_ID environment variables must be set"
  exit 1
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Install dependencies if needed
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
  source venv/bin/activate
  echo "Installing dependencies..."
  pip install -e ".[dev]"
fi

# Run unit tests
echo "Running unit tests..."
pytest tests/test_sso.py -v

echo ""
echo "Running integration tests..."
pytest tests/test_sso_integration.py -v

echo ""
echo "✓ All tests passed!"
