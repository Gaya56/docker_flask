from flask import Flask, jsonify
import time
import random
import json

app = Flask(__name__)

def generate_fake_data():
    data = {
        "city": "Edmonton",
        "device_id": f"device_{random.randint(1000, 9999)}",
        "asset_tag": f"asset_{random.randint(1000, 9999)}",
        "connection_status": random.choice(["connected", "disconnected"]),
        "error_code": random.choice(["E001", "E002", "E003", "E004", "E005"]),
        "timestamp": time.time()
    }
    return data

@app.route('/data')
def get_data():
    data = generate_fake_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/calgary')
def calgary():
    data = generate_fake_data()
    data['city'] = 'Calgary'
    return jsonify(data)

@app.route('/edmonton')
def edmonton():
    data = generate_fake_data()
    data['city'] = 'Edmonton'
    return jsonify(data)

@app.route('/vancouver')
def vancouver():
    data = generate_fake_data()
    data['city'] = 'Vancouver'
    return jsonify(data)

@app.route('/montreal')
def montreal():
    data = generate_fake_data()
    data['city'] = 'Montreal'
    return jsonify(data)

@app.route('/ottawa')
def ottawa():
    data = generate_fake_data()
    data['city'] = 'Ottawa'
    return jsonify(data)

@app.route('/hamilton')
def hamilton():
    data = generate_fake_data()
    data['city'] = 'Hamilton'
    return jsonify(data)

@app.route('/london')
def london():
    data = generate_fake_data()
    data['city'] = 'London'
    return jsonify(data)
