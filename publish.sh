#!/bin/bash

set -e

# Get version from pyproject.toml
VERSION=$(grep "^version = " pyproject.toml | cut -d'"' -f2)

echo "Publishing FastComments Python SDK v$VERSION..."

# Clean up old builds
echo "Cleaning up old builds..."
rm -rf dist/ build/ *.egg-info

# Build the package
echo "Building the package..."
#python3 -m pip install --upgrade build twine
python3 -m build

# Check the package
echo "Checking the package..."
python3 -m twine check dist/*

echo ""
echo "Package built successfully!"
echo ""

# Publish to PyPI
echo "Publishing to PyPI..."
python3 -m twine upload dist/*

echo ""
echo "✓ Published to PyPI!"
echo "Users can install it with:"
echo "  pip install fastcomments"
