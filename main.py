import requests
import schedule
import time

# Your Trello API Key and Token
API_KEY = 'your_api_key'
TOKEN = 'your_api_token'

# Your Trello Board ID
BOARD_ID = 'your_board_id'

# Function to create a task on Trello
def create_task(task_name):
    url = f'https://api.trello.com/1/cards?key={API_KEY}&token={TOKEN}&idList={BOARD_ID}&name={task_name}'
    response = requests.post(url)
    if response.status_code == 200:
        print(f"Task '{task_name}' added successfully.")
    else:
        print(f"Failed to add task '{task_name}'.")

# Schedule the task creation once a day
schedule.every().day.at("09:00").do(create_task, task_name="Your Daily Task")

while True:
    schedule.run_pending()
    time.sleep(1)
