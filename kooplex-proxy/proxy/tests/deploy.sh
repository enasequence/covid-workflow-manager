#!/bin/bash

export KUBECONFIG=/Users/mansurova/k8s_configs/config.txt

if docker images | grep -q kooplex-proxy; then
    echo "Deleting existing Docker image"
    docker rmi kooplex-proxy
fi

IMAGES=$(docker images --format '{{.Repository}}:{{.Tag}}' | grep '^milm/')

if [ -n "$IMAGES" ]; then
  for IMAGE in $IMAGES; do
    docker rmi $IMAGE
  done
  echo "All milm/ images have been removed"
else
  echo "No milm/ images found"
fi

dir="$(dirname "$(pwd)")"
parent="$(dirname $dir)"

echo "Building Docker image"
docker build -t kooplex-proxy $parent

echo "Tagging Docker image"
IMAGE_ID=$(docker images -q kooplex-proxy)
echo "Tagging Docker image with ID ${IMAGE_ID}"
docker tag ${IMAGE_ID} milm/kooplex-proxy:latest

echo "Pushing Docker image to Docker Hub"
docker push milm/kooplex-proxy:latest

echo "Deploying new Pod"
echo $parent
kubectl --kubeconfig $KUBECONFIG delete --namespace=kooplex-veo -f $parent/kooplex_svc+deployment.yml
kubectl --kubeconfig $KUBECONFIG apply --namespace=kooplex-veo -f $parent/kooplex_svc+deployment.yml

kubectl --kubeconfig $KUBECONFIG --namespace=kooplex-veo get pods
