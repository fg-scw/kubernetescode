from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Scaleway Test CI/CD, with Github webhook !!!'
