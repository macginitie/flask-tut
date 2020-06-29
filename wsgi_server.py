import os
from gevent.pywsgi import WSGIServer

if __name__ == "__main__":

    from tutorial_app import app
    port = int(os.getenv('PORT', 8081))
    print('port is {}'.format(port))
    http_server = WSGIServer(('0.0.0.0', port), app)
    http_server.serve_forever()
