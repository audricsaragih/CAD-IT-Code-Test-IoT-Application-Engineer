import json
import time
import statistics
# import matplotlib.pyplot as plt

# Load data from internal json file
with open('stream_sensor_data.json') as f:
    stream_sensor_data = json.load(f)

stream_sensor_value = {
    'temperature': {
        'min': 999, 
        'max': 0, 
        'med': 0,
        'avg': 0
    },
    'humidity': {
        'min': 999, 
        'max': 0, 
        'med': 0,
        'avg': 0
    }
}
sum_t = 0
sum_h = 0
count = 0

# Push rate = 15 minutes
time.sleep(15*60)

while(True):
    for i in stream_sensor_data:
        # Get the minimum data
        if (stream_sensor_value['temperature']['min'] > i['temperature']):
            stream_sensor_value['temperature']['min'] = i['temperature']
        if (stream_sensor_value['humidity']['min'] > i['humidity']):
            stream_sensor_value['humidity']['min'] = i['humidity']
        # print(i)
        
        # Get the maximum data
        if (stream_sensor_value['temperature']['max'] < i['temperature']):
            stream_sensor_value['temperature']['max'] = i['temperature']
        if (stream_sensor_value['humidity']['max'] < i['humidity']):
            stream_sensor_value['humidity']['max'] = i['humidity']

        # Get sum of temperature and humidity
        sum_t = sum_t + i['temperature']
        sum_h = sum_h + i['humidity']

        count = count + 1

    list_t = [0]*count
    list_h = [0]*count

    # Get median of temperature and humidity
    for i in stream_sensor_data:
        for j in range(count):
            list_t[j] = i['temperature']
            list_h[j] = i['humidity']

    stream_sensor_value['temperature']['med'] = statistics.median(list_t)
    stream_sensor_value['humidity']['med'] = statistics.median(list_h)

    # Get mean/average of temperature and humidity
    stream_sensor_value['temperature']['avg'] = sum_t/count
    stream_sensor_value['humidity']['avg'] = sum_h/count

    # Display temperature and humidity data
    for key, value in stream_sensor_value.items():
        print(key, ' : ', value)

    # Writing temperature and humidity data to endpoint
    with open('stream_temperature_and_humidity_summary_data.json', 'w') as outfile:
        json.dump(stream_sensor_value, outfile, indent = 2)
    
    # Push rate = 15 minutes
    time.sleep(15*60)
