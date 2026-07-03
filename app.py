from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return (
        "Welcome to my updated Docker app! 🚀 "
        "This is version 2.01! trying volume mountswwwww compose"
    )


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
