#!/bin/bash

set -e

if [ -z "$1" ]; then
  echo "Usage: ./bump.sh <new_version>"
  echo "Example: ./bump.sh 0.0.2"
  exit 1
fi

NEW_VERSION=$1

echo "Bumping version to $NEW_VERSION..."

# Update openapi-config.json
jq ".packageVersion = \"$NEW_VERSION\"" openapi-config.json > openapi-config.json.tmp && mv openapi-config.json.tmp openapi-config.json
echo "✓ Updated openapi-config.json packageVersion to $NEW_VERSION"

# Update pyproject.toml
sed -i "s/^version = .*/version = \"$NEW_VERSION\"/" pyproject.toml
echo "✓ Updated pyproject.toml version to $NEW_VERSION"

echo "Done! Version bumped to $NEW_VERSION"
