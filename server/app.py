#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''<h1>The host of this page is {host}
                <h2> The nam eof thos application is {appname} </h2>
                <h3> The path of this application on the users's device is {g.path}</h3>
    '''
    status_code = 200
    headers = {}
    
    return make_response(response_body, status_code, headers)
                

if __name__ == '__main__':
    app.run(port=5555, debug=True)
