from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

health_status = True

@app.route("/")
def hello_user():
    return f"<p>Hello, user!</p><a href='/healthcheck'>Check Health</a>"


@app.route("/healthcheck")
def healthcheck():
    if health_status:
        resp = jsonify(date=datetime.now(), status="OK")
        resp.status_code = 200
    else:
        resp = jsonify(date=datetime.now(), status="FAIL")
        resp.status_code = 500
    return resp
