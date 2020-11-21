import requests

#Pseudo-code
# 1. Ask the user for city
# Call the API to get the woeid for that city
# call the API to get the weather for that weoid
# Display the weather info from last API call

BASE_URL = "https://www.metaweather.com"

city = input("City?\n> ")

url = f"{BASE_URL}/api/location/search/?query={city}"

response = requests.get(url)
data = response.json()

print(data)
print(len(data))
print(type(data[0]))

woeid = (data[0]["woeid"])
print(woeid)

url =f"{BASE_URL}/api/location/{woeid}/"
response = requests.get(url)
data = response.json()

for day in data["consolidated_weather"]:
    desc = day["weather_state_name"]
    date = day["applicable_date"]
    temp = day["max_temp"]
    print(f"{date}, {desc}, (#{temp} C)")



