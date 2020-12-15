FROM node:15.3.0-alpine3.10 AS builder

WORKDIR /opt/src/
COPY package*.json ./
RUN npm install

ENV PATH="./node_modules/.bin:$PATH"

COPY . ./
RUN ng build --prod

FROM nginx:1.19-alpine

COPY --from=builder /opt/src/dist/samples-logs/ /usr/share/nginx/html/
