FROM mongo-express
COPY config.js /node_modules/mongo-express
COPY config.default.js /node_modules/mongo-express
WORKDIR /node_modules/mongo-express
ENTRYPOINT ["node", "app.js", "--admin", "--url", "mongodb://mongodb-svc:27017"]