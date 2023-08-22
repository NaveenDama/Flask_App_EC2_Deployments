from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1> Flask App Version 1 Home.</h1>"


if __name__ == "__main__":
    # If you are using gunicorn socket binding the host and port config will be overided by gunicorn default port which is 8000
    app.run(host="0.0.0.0", port=80, debug=True)
