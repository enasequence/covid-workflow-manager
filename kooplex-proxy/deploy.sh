#!/bin/bash

if docker images | grep -q kooplex-proxy; then
    echo "Deleting existing Docker image"
    docker rmi kooplex-proxy
fi

echo "Building Docker image"
docker build -t kooplex-proxy --no-cache .

echo "Tagging Docker image"
IMAGE_ID=$(docker images -q kooplex-proxy)
echo "Tagging Docker image with ID ${IMAGE_ID}"
docker tag ${IMAGE_ID} milm/kooplex-proxy:latest

echo "Pushing Docker image to Docker Hub"
docker push milm/kooplex-proxy:latest

echo "Deploying new Pod"
kubectl --kubeconfig $KUBECONFIG delete --namespace=kooplex-veo -f ./kooplex_svc+deployment.yml
kubectl --kubeconfig $KUBECONFIG apply --namespace=kooplex-veo -f kooplex_svc+deployment.yml
