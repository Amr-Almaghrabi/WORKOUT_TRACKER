import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

API_KEY = "API_KEY"
APP_ID = "APP_ID"
SHEETY_ENDPOINT = """ENTER YOUR SHEETY ENDPOINT URL"""
WORKOUT_ENDPOINT = """ ENTER YOUR NUTRITIONX URL ENDPOINT"""

GENDER = "male"
AGE = 21
WEIGHT = 78
HEIGHT = 173

bearer_token = {
    "Authorization": "Bearer Your_Token"
}


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

QUERY = input("Tell me what exercises you did today? ")

parameters_workout = {
 "query": QUERY,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE,
}

response = requests.post(url=WORKOUT_ENDPOINT, headers= headers, json= parameters_workout)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response2 = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs)
print(response2.text)
