import json
import os
from flask import Flask, jsonify
from flask_cors import CORS
import random
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Generate fake robot data for testing purposes upadate every 5 seconds or not
def generate_robot_data():
    robot = {
        "Robot ID": str(uuid.uuid4()),
        "Online/Offline": random.choice([True, False]),
        "Battery Percentage": random.randint(0, 100),
        "CPU Usage": random.randint(10, 100),
        "RAM Consumption": random.randint(1000, 8000),
        "Last Updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Location Coordinates": [random.uniform(-90, 90), random.uniform(-180, 180)],
    }
    return robot

@app.route('/robots', methods=['GET'])
def get_robots():
    file_path = os.path.join(os.path.dirname(__file__), 'fake_robot_data.json')
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    data.append(generate_robot_data())
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
