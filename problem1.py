import json
import requests

# Fetching data fron jsonplaceholder
response = requests.get("http://jsonplaceholder.typicode.com/users")
users = json.loads(response.text)

# Load data from internal json file
with open('salary_data.json') as f:
    salary_data = json.load(f)

for i in users:
    i["salary in IDR"] = i.pop("website")
    i["salary in USD"] = i.pop("company")

# Convert IDR to USD using currency converter
url = 'https://free.currconv.com/api/v7/convert?apiKey=b0f94113e52b34c8241a&q=USD_IDR&compact=y'
response = requests.get(url)
convertIDRtoUSD = response.json()

for i in users:
    for j in salary_data['array']:
        if (i['id'] == j['id']):
            i["salary in IDR"] = j['salaryInIDR']
            i["salary in USD"] = j['salaryInIDR']/convertIDRtoUSD['USD_IDR']['val']

# Writing complete data to endpoint
with open('complete_salary_data.json', 'w') as outfile:
    json.dump(users, outfile, indent = 8)