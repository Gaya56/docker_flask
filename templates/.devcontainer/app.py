from flask import Flask, render_template
import random
import time
from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Azure Event Hub configuration
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


@app.route('/')
def index():
    """
    Home route rendering the landing page.
    """
    return render_template('index.html', title='GitHub Codespaces ♥️ Flask')


@app.route('/calgary')
def calgary():
    """
    Route for Calgary, generating fake data and sending it to Event Hub.
    """
    data = generate_fake_data('Calgary')
    send_to_event_hub(data)
    return render_template('base.html', city_name='Calgary', city_data=data)


@app.route('/edmonton')
def edmonton():
    """
    Route for Edmonton, generating fake data and sending it to Event Hub.
    """
    data = generate_fake_data('Edmonton')
    send_to_event_hub(data)
    return render_template('base.html', city_name='Edmonton', city_data=data)


@app.route('/hamilton')
def hamilton():
    """
    Route for Hamilton, generating fake data and sending it to Event Hub.
    """
    data = generate_fake_data('Hamilton')
    send_to_event_hub(data)
    return render_template('base.html', city_name='Hamilton', city_data=data)


@app.route('/london')
def london():
    """
    Route for London, generating fake data and sending it to Event Hub.
    """
    data = generate_fake_data('London')
    send_to_event_hub(data)
    return render_template('base.html', city_name='London', city_data=data)


@app.route('/montreal')
def montreal():
    """
    Route for Montreal, generating fake data and sending it to Event Hub.
    """
    data = generate_fake_data('Montreal')
    send_to_event_hub(data)
    return render_template('base.html', city_name='Montreal', city_data=data)


@app.route('/vancouver')
def vancouver():
    """
    Route for Vancouver, generating fake data and sending it to Event Hub.
    """
    data = generate_fake_data('Vancouver')
    send_to_event_hub(data)
    return render_template('base.html', city_name='Vancouver', city_data=data)


if __name__ == "__main__":
    app.run(debug=True, port=5001)


