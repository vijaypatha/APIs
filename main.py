import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
'''
response code: Is our resquest (get) got a response.
1XX: Hold On
2XX: Here you Go
3XX: Go away
4XX: You made a mistake
5XX: Server screwed up 
'''
print(response.status_code)

response.raise_for_status()
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

position = (longitude, latitude)
print(position)