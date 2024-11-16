import os
import random
import time
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Azure Event Hub Configuration
EVENT_HUB_CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

def generate_fake_data(city):
    """
    Generates a payload of fake data for a specified city.
    """
    data = {
        "city": city,
        "device_id": f"device_{random.randint(1000, 9999)}",
        "asset_tag": f"asset_{random.randint(1000, 9999)}",
        "connection_status": random.choice(["connected", "disconnected"]),
        "error_code": random.choice(["E001", "E002", "E003", "E004", "E005"]),
        "timestamp": time.time()
    }
    return data

def send_to_event_hub(data):
    """
    Sends data to Azure Event Hub.
    """
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STRING,
            eventhub_name=EVENT_HUB_NAME
        )
        event_data_batch = producer.create_batch()
        event_data_batch.add(EventData(str(data)))
        producer.send_batch(event_data_batch)
        print(f"Data sent to Event Hub: {data}")
    except Exception as e:
        print(f"Error sending data to Event Hub: {e}")

@app.route('/data')
def get_data():
    """
    Generates and sends data for Edmonton.
    """
    data = generate_fake_data("Edmonton")
    send_to_event_hub(data)
    return jsonify(data)

@app.route('/<city>')
def city_route(city):
    """
    Generates and sends data for a specified city.
    """
    data = generate_fake_data(city)
    send_to_event_hub(data)
    return render_template(f'{city.lower()}.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
