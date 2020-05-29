from pymongo import MongoClient

from flask import Flask
app = Flask(__name__)


@app.route("/jovian")
def jovian_samples():
    # Getting access to MongoDB
    client = MongoClient('mongodb://samples-logs-db-svc')
    db = client.samples

    results = list()
    for sample in db.samples.find({'pipeline_name': 'Jovian'}, {'_id': 0}):
        results.append(sample)
    return {'results': results}


@app.route("/jovian/<run_id>")
def jovian_samples_details(run_id):
    # Getting access to MongoDB
    client = MongoClient('mongodb://samples-logs-db-svc')
    db = client.samples

    return {'results': db.samples.find_one({'id': run_id}, {'_id': 0})}


@app.route("/ont")
def ont_samples():
    # Getting access to MongoDB
    client = MongoClient('mongodb://samples-logs-db-svc')
    db = client.samples

    results = list()
    for sample in db.samples.find({'pipeline_name': 'ONT'}, {'_id': 0}):
        results.append(sample)
    return {'results': results}


@app.route("/ont/<run_id>")
def ont_samples_details(run_id):
    # Getting access to MongoDB
    client = MongoClient('mongodb://samples-logs-db-svc')
    db = client.samples

    return {'results': db.samples.find_one({'id': run_id}, {'_id': 0})}


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
