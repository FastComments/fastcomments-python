#!/bin/bash

# Install/update dependencies
pip install -q openapi-generator-cli 2>/dev/null || echo "Skipping openapi-generator-cli pip install (using npx)"

# Remove previously generated code
rm -rvf ./client

# Try to download the OpenAPI spec from the running FastComments server
if wget -q http://localhost:3001/js/swagger.json -O ./openapi.json; then
    echo "Downloaded OpenAPI spec from running server"
    SPEC_FILE="./openapi.json"
else
    echo "Server not running, using local OpenAPI spec"
    SPEC_FILE="./openapi.yaml"
fi

# Generate the Python client using openapi-generator
# Using npx to ensure consistent version with JS SDK
npx @openapitools/openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g python \
    -o ./client \
    -c openapi-config.json

# Flatten the nested client/client/ structure
if [ -d "./client/client" ]; then
    mv ./client/client/* ./client/
    rmdir ./client/client
    echo "Flattened nested client directory structure"
fi

echo "Generated Python client in ./client"

# Generate API documentation (optional)
rm -rvf ./docs/api

npx @openapitools/openapi-generator-cli generate \
    -i "$SPEC_FILE" \
    -g markdown \
    -o ./docs/api \
    -c openapi-config.json

echo "Generated API documentation in ./docs/api"
