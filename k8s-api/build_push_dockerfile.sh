pigar
docker build --pull --rm -f "Dockerfile" -t ctr26/k8s-example:latest "."
docker push ctr26/k8s-example:latest
