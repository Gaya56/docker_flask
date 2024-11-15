import random
import time
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def generate_fake_data(city):
    data = {
        "city": city,
        "device_id": f"device_{random.randint(1000, 9999)}",
        "asset_tag": f"asset_{random.randint(1000, 9999)}",
        "connection_status": random.choice(["connected", "disconnected"]),
        "error_code": random.choice(["E001", "E002", "E003", "E004", "E005"]),
        "timestamp": time.time()
    }
    return data

@app.route('/data')
def get_data():
    data = generate_fake_data("Edmonton")
    return jsonify(data)

@app.route('/calgary')
def calgary():
    data = generate_fake_data('Calgary')
    return render_template('calgary.html', data=data)

@app.route('/edmonton')
def edmonton():
    data = generate_fake_data('Edmonton')
    return render_template('edmonton.html', data=data)

@app.route('/vancouver')
def vancouver():
    data = generate_fake_data('Vancouver')
    return render_template('vancouver.html', data=data)

@app.route('/montreal')
def montreal():
    data = generate_fake_data('Montreal')
    return render_template('montreal.html', data=data)

@app.route('/ottawa')
def ottawa():
    data = generate_fake_data('Ottawa')
    return render_template('ottawa.html', data=data)

@app.route('/hamilton')
def hamilton():
    data = generate_fake_data('Hamilton')
    return render_template('hamilton.html', data=data)

@app.route('/london')
def london():
    data = generate_fake_data('London')
    return render_template('london.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)