# airhorn
Never miss a meeting again! Integrates with Google Calendar and provides a glorious fullscreen visual reminder when you're about to be late.

![image](https://github.com/user-attachments/assets/51a396de-fb4e-4d10-aaa9-c069fe14b118)

## Installation
`pip install -r requirements.txt`

## Usage
1. Create a Google Cloud Platform project and enable the [Google Calendar API](https://developers.google.com/calendar/quickstart/python).
2. Create OAuth 2.0 credentials for a desktop application and download the JSON file to `credentials.json`.
3. Run `python main.py` to run the program. If it's your first time running the program, you'll be prompted to authenticate with Google Calendar.