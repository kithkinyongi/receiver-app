from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Receiver is running. POST to /data", 200

@app.route('/data', methods=['POST'])
def receive_data():
    content = request.get_data(as_text=True)
    print(f"[{datetime.utcnow().isoformat()}] Received:\n{content}\n{'-'*40}")
    with open("received.log", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.utcnow().isoformat()}]\n{content}\n{'-'*40}\n")
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
