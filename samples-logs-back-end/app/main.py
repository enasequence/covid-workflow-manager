from pymongo import MongoClient

from flask import Flask
app = Flask(__name__)


@app.route("/")
def samples():
    # Getting access to MongoDB
    client = MongoClient('mongodb://samples-logs-db-svc')
    db = client.samples

    results = list()
    for sample in db.samples.find({}, {'_id': 0}):
        results.append(sample)
    return {'results': results}


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
