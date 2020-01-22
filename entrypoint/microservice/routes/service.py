# Embedding Route
# Routes related to creating text embeddings

import sys
import requests
from flask import (
    Blueprint, flash, g, redirect, request, session, url_for, jsonify, current_app as app
)
from werkzeug.exceptions import abort


#################################################
# Initialize the models
#################################################

# TODO: include the model initialization function

#################################################
# Setup the embeddings blueprint
#################################################

# TODO: provide an appropriate route name and prefix
bp = Blueprint('service', __name__, url_prefix='/api/v1/service')


@bp.route('/', methods=['GET'])
def index():
    # TODO: provide an appropriate output
    return abort(501)


@bp.route('/embedding', methods=['POST'])
def get_embedding():
    # This is only hardcoded test:

    text = request.json.get('query')
    HOST = app.config.get('TEXT_EMBEDDING_HOST', 'localhost')
    PORT = app.config.get('TEXT_EMBEDDING_PORT', '4000')
    data = {
        "query": text,
    }
    r = requests.post(f"http://{HOST}:{PORT}/api/v1/embeddings/expand", json=data)
    return jsonify(r.json())


# TODO: add an appropriate route name
@bp.route('/second', methods=['GET', 'POST'])
def second():
    # TODO: assign the appropriate variables
    variable = None
    if request.method == 'GET':
        # retrieve the correct query parameters
        variable = request.args.get('variable', default='', type=str)
    elif request.method == 'POST':
        # retrieve the text posted to the route
        variable = request.json['variable']
    else:
        # TODO: log exception
        return abort(405)

    try:
        # TODO: add the main functionality with the model and variable
        finish = True
    except Exception as e:
        # TODO: log exception
        # something went wrong with the request
        return abort(400, str(e))
    else:
        # TODO: return the response
        return jsonify({
            "finish": finish
        })
