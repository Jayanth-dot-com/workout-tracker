import requests
from datetime import datetime

API_ID = "<YOUR_NUTRITIONIX_ID>"
API_Key = "<YOUR_NUTRITIONIX_API_KEY>"

user_input = input("Tell me which exercises you did: ")

headers_nutritionix = {
    "Content-Type": "application/json",
    "x-app-id": API_ID,
    "x-app-key": API_Key
}
payload_nutritionix = {
    "query": user_input
}
response1 = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers_nutritionix, json=payload_nutritionix)
response1.raise_for_status()
result = response1.json()

sheet_header = {
    "Authorization": "Basic <YOUR_BASIC_CODE>"
}
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

sheet_response = requests.post(url="<YOUR_GOOGLE_SHEET_URL>", json=sheet_inputs, headers=sheet_header)
print("Your Workout is recorded successfully")