from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Flask Backend! 🐍"})

@app.route('/api/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)