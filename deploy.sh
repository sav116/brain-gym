#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Reset and update the repository
echo "Resetting changes and updating the repository..."
git reset --hard
git pull

# Docker image name
IMAGE_NAME="brain_gym"

# Build the Docker image
echo "Building Docker image: $IMAGE_NAME..."
docker build -t $IMAGE_NAME .

# Stop and remove the previous container if it exists
if [ "$(docker ps -q -f name=$IMAGE_NAME)" ]; then
    echo "Stopping and removing the previous container: $IMAGE_NAME..."
    docker stop $IMAGE_NAME
    docker rm $IMAGE_NAME
fi

# Run a new container
echo "Starting a new container: $IMAGE_NAME..."
docker run -d \
    --name $IMAGE_NAME \
    --restart always \
    --env-file .env \
    -v $(pwd)/.env:/app/.env \
    --log-opt max-size=10m \
    --log-opt max-file=3 \
    $IMAGE_NAME

# Check status
docker ps -f name=$IMAGE_NAME
