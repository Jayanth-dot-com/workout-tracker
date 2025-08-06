# Workout Tracker
Effortlessly track your daily workouts and have your data automatically stored in a Google Sheet using Nutritionix API and Sheety integration
# Features
1. Track your workouts and automatically log details to Google Sheets
2. Integrates Nutritionix API for detailed exercise information
3. No manual spreadsheet entry required—fully automated!
4. Secure and private: Use your own Google account and Sheety project
# Installatition
1. Clone My Repository using this link https://github.com/Jayanth-dot-com/Workout-Tracker.git
2. Get Your API Keys
	*Nutritionix API:
		1. Sign up at Nutritionix API
		2. Save your Application ID and API Key
	*Google Sheet:
		1. Create a new Google Sheet
		2. Click File > Copy link to get the URL
3. Set Up Sheety
	*Go to Sheety, log in using the same Google account as your spreadsheet
	*Create a Sheety project and link it to your Google Sheet
	*(Optional) In Sheety, set up Basic Authentication for security
	*Copy the generated authentication header and add it to your code (see below)
4. Configure the Script
Open the main Python file in your editor and add your API keys and (if used) authentication header in the appropriate variables
# How to Use
1. Download and edit the script with your credentials.
2. Enter your workout details as prompted.
3. Each entry goes straight to your Google Sheet for easy tracking!
# Main Libraries Used
1. requests
2. datetime
# License
MIT License