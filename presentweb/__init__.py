from flask import Flask

app = Flask(__name__)

@app.route("/")
def presentweb():
    return "Server running"