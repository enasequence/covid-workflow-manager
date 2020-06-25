pigar
docker build --pull --rm -f "Dockerfile" -t ctr26/samples-cleanup-cron:latest "."
docker push ctr26/samples-cleanup-cron:latest