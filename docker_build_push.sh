#!/bin/bash

# Set the insecure registry address
INSECURE_REGISTRY="95.217.9.183:5000"

# Configure Docker to use the insecure registry
echo "Configuring Docker to use the insecure registry..."
echo "{\"insecure-registries\": [\"$INSECURE_REGISTRY\"]}" | sudo tee /etc/docker/daemon.json > /dev/null
sudo systemctl restart docker

# Log in to the insecure registry (replace with your credentials if needed)
echo "Logging in to the insecure registry..."
docker login $INSECURE_REGISTRY

# Navigate to the directory containing your Dockerfile and code
cd /path/to/your/docker/project

# Build the Docker image
echo "Building the Docker image..."
docker build -t $INSECURE_REGISTRY/joker:latest .

# Push the Docker image to the insecure registry
echo "Pushing the Docker image to the insecure registry..."
docker push $INSECURE_REGISTRY/joker:latest

echo "Image successfully pushed to the insecure registry."

# Optionally, remove the insecure registry configuration (if needed)
# sudo rm /etc/docker/daemon.json
# sudo systemctl restart docker
