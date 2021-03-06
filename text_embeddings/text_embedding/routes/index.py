# Embedding Route
# Routes related to creatiung text embeddings

import os

from flask import (
    Blueprint, flash, g, request, jsonify, current_app as app, render_template, url_for
)
from werkzeug.exceptions import abort

#################################################
# Setup the index blueprint
#################################################

bp = Blueprint('index', __name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@bp.route('/', methods=['GET'])
def index():
    # get the documentation information
    MODEL_PATH = app.config['MODEL_PATH']
    MODEL_LANGUAGE = app.config['MODEL_LANGUAGE']
    HOST = app.config['HOST'] if 'HOST' in app.config else '127.0.0.1'
    PORT = app.config['PORT'] if 'PORT' in app.config else '5000'

    result = {
        "model_path": MODEL_PATH,
        "model_language": MODEL_LANGUAGE,
        "host": HOST,
        "port": PORT
    }

    # render the documentation
    return render_template('index.html', result=result)