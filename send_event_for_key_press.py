from pynput import keyboard
import requests

BEARER_TOKEN = 'Ram pam pam'

# Send webhook function
def send_event(webhook_id):
    url = f'http://localhost:8123/api/webhook/{webhook_id}'
    requests.post(url, headers={
        'Authorization': f'Bearer {BEARER_TOKEN}'
    })

# Function to handle key press events
def on_press(key):
    try:
        if key.vk == 269025095:  # F17 key
            send_event("f16_keypress")
        elif key.vk == 269025096:  # F16 key
            send_event("f17_keypress")
        elif key.vk == 269025097:  # F18 key
            send_event("f18_keypress")
    except AttributeError:
        pass

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
