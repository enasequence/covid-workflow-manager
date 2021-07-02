FROM staphb/auspice
RUN cd /home/node/auspice && \
    npx browserslist@latest --update-db
USER root
RUN mkdir /data/datasets
RUN curl http://data.nextstrain.org/ncov.json \
    --compressed -o /data/datasets/ncov.json
