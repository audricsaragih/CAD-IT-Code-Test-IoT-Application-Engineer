import json
import statistics

# Load data from internal json file
with open('sensor_data.json') as f:
    sensor_data = json.load(f)

sensor_value = {
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

for i in sensor_data['array']:
    # Get the minimum data
    if (sensor_value['temperature']['min'] > i['temperature']):
        sensor_value['temperature']['min'] = i['temperature']
    if (sensor_value['humidity']['min'] > i['humidity']):
        sensor_value['humidity']['min'] = i['humidity']
    # print(i)
    
    # Get the maximum data
    if (sensor_value['temperature']['max'] < i['temperature']):
        sensor_value['temperature']['max'] = i['temperature']
    if (sensor_value['humidity']['max'] < i['humidity']):
        sensor_value['humidity']['max'] = i['humidity']

    # Get sum of temperature and humidity
    sum_t = sum_t + i['temperature']
    sum_h = sum_h + i['humidity']

    count = count + 1

list_t = [0]*count
list_h = [0]*count

# Get median of temperature and humidity
for i in sensor_data['array']:
    for j in range(count):
        list_t[j] = i['temperature']
        list_h[j] = i['humidity']

sensor_value['temperature']['med'] = statistics.median(list_t)
sensor_value['humidity']['med'] = statistics.median(list_h)

# Get mean/average of temperature and humidity
sensor_value['temperature']['avg'] = sum_t/count
sensor_value['humidity']['avg'] = sum_h/count

# Writing temperature and humidity data to endpoint
with open('temperature_and_humidity_summary_data.json', 'w') as outfile:
    json.dump(sensor_value, outfile, indent = 2)