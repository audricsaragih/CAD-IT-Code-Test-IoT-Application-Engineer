import json
import time
import matplotlib.pyplot as plt

# Load data from internal json file
with open('sensor_data.json') as f:
    sensor_data = json.load(f)

sensor_value = [
    {
        'temperature': 0,
        'humidity': 0
    }
]
count = 0

while (True):
    for i in sensor_data['array']:
        count = count + 1
        for j in range(1):
            print(i['temperature'], i['humidity'])
            if (count == 1):
                sensor_value[j]['temperature'] = i['temperature']
                sensor_value[j]['humidity'] = i['humidity']
            else:
                sensor_value.append({'temperature': i['temperature'], 'humidity': i['humidity']})

            # Push rate = 2 minutes
            if (count % 5 == 0):
                # Writing sensor data to endpoint
                with open('stream_sensor_data.json', 'w') as outfile:
                    json.dump(sensor_value, outfile, indent = 2)
                time.sleep(2*60)

# Data visualization
