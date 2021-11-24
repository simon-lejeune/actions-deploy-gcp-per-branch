from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "fb1"


@app.route("/test")
def test():
    return "fb1
