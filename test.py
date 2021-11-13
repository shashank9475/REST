import requests

base = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 10000},
        {"likes": 34, "name": "harry", "views": 200},
        {"likes": 56, "name": "milli", "views": 500}]

for i in range(len(data)):
    response = requests.put(base + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(base + "video/1")
print(response.json())
