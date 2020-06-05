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


@app.route("/ont/<stage>/<status>")
def ont_samples_filters(stage, status):
    # TODO: change front- or back-end to have consistent names
    xref = {
        'import_from_ena': 'ena_import',
        'pipeline_analysis': 'pipeline_analysis',
        'export_to_ena': 'ena_export'
    }

    # Getting access to MongoDB
    client = MongoClient('mongodb://samples-logs-db-svc')
    db = client.samples

    results = list()
    for sample in db.samples.find({'pipeline_name': 'ONT'}, {'_id': 0}):
        item = sample[stage]['status']
        xref_status = xref[stage]
        if get_status(item, xref_status) == status:
            results.append(sample)
    return {'results': results}


def get_status(item, key):
    statuses = {
        'ena_import': {
            'success': 'download finished',
            'failed': 'download failed'
        },
        'pipeline_analysis': {
            'success': 'pipeline_finished',
            'started': 'pipeline_started'
        },
        'ena_export': {
            'success': 'export_finished',
            'started': 'export_started'
        }
    }
    if key == 'ena_import':
        if statuses[key]['success'] in item:
            return 'Success'
        elif statuses[key]['failed'] in item:
            return 'Failed'
        else:
            return 'Undefined'
    else:
        if statuses[key]['success'] in item:
            return 'Success'
        elif statuses[key]['started'] in item:
            all_indices = [el for el in item if el == statuses[key]['started']]
            if len(all_indices) >= 6:
                return 'Failed'
            else:
                return 'Processing'
        else:
            return 'Undefined'


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
