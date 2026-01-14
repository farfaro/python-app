
from flask import Flask, jsonify
import datetime
import socket



app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now(),
        'hostname': socket.gethostname(),
        'saludo': 'hola como andas?'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'up'
    }), 200

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")

#'/api/v1/details'
#'/api/v1/healthz'