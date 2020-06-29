from flask import Flask, jsonify, Response
import os
import json

APP_NAME = 'example-flask-app'
APP_VERSION = '1.0.0'

app = Flask(__name__)
app.url_map.strict_slashes = False

is_local = False

BUILD_INFO_FILE = 'build_info.json'


def this_dir_plus_path(relative_path):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(this_dir, relative_path))


@app.route('/')
def index_page():
    print('main page')
    return Response('Hello Friend', mimetype = 'text/plain')


@app.route('/info')
def info_json():
    print('route /info - return app & build info')

    build_info_path = this_dir_plus_path(BUILD_INFO_FILE)
    try:
        with open(build_info_path, 'r', encoding = 'utf-8') as f:
            build_info = json.load(f)
    except Exception as e:
        build_info = {
            "error": "failed loading %s" % build_info_path,
            "exception": '%s: %s' % (e.__class__.__name__, e)
        }

    response_dict = {
        'app_name': APP_NAME,
        'app_version': APP_VERSION,
        'description': 'tutorial',
        'routes': {
            '/': 'say Howdy',
            '/info': 'return app & build info',
        },
        'build_info': build_info
    }

    # return indented response for easier reading
    return Response(json.dumps(response_dict, indent=4), mimetype='application/json')
