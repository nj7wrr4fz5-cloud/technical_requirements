import requests

TOKEN = '6706048508:AAF-8INmBKwP1x7DA-_ET8D282c5pp0Rn2Y'
API_URL = f'https://api.telegram.org/bot{TOKEN}/'

# Function to handle commands

def handle_command(command):
    if command == '/start':
        return 'Welcome to the bot!'
    elif command == '/help':
        return 'Available commands: /start, /help'
    return 'Unknown command'

# Example function to listen for updates

def listen_for_updates():
    response = requests.get(API_URL + 'getUpdates')
    updates = response.json()

    for update in updates['result']:
        command = update['message']['text']
        chat_id = update['message']['chat']['id']
        response_message = handle_command(command)
        # Here you would send a response back using send_message(chat_id, response_message)

# Placeholder for a function to send messages

def send_message(chat_id, text):
    requests.post(API_URL + 'sendMessage', json={'chat_id': chat_id, 'text': text})

# Entry point
if __name__ == '__main__':
    listen_for_updates()