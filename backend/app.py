from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "you're on the <strong>master</strong> branch with an update"


@app.route("/test")
def test():
    return "you're on the <strong>master</strong> branch with an update"

