#!/bin/bash

set -e

# Get version from pyproject.toml
VERSION=$(grep "^version = " pyproject.toml | cut -d'"' -f2)
TAG="v$VERSION"

echo "Publishing FastComments Python SDK $TAG..."

# Clean up old builds
echo "Cleaning up old builds..."
rm -rf dist/ build/ *.egg-info

# Build the package (wheel + sdist) to attach to the GitHub Release
echo "Building the package..."
#python3 -m pip install --upgrade build
python3 -m build

echo ""
echo "Package built successfully!"
echo ""

# Tag the release (skip if the tag already exists)
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "Tag $TAG already exists, skipping tag creation."
else
    echo "Tagging $TAG..."
    git tag "$TAG"
    git push origin "$TAG"
fi

# Create the GitHub Release with the built artifacts (skip if it already exists)
if gh release view "$TAG" >/dev/null 2>&1; then
    echo "Release $TAG already exists; uploading/clobbering artifacts..."
    gh release upload "$TAG" dist/*.whl dist/*.tar.gz --clobber
else
    echo "Creating GitHub Release $TAG..."
    gh release create "$TAG" dist/*.whl dist/*.tar.gz \
        --title "$TAG" \
        --notes "FastComments Python SDK $TAG"
fi

echo ""
echo "✓ Published GitHub Release $TAG!"
echo "Users can install it with:"
echo "  pip install git+https://github.com/fastcomments/fastcomments-python.git@$TAG"
