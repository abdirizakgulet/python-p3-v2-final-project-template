# chatbot/debug.py

def debug_message(message):
    print(f"DEBUG: {message}")

def log_error(error):
    with open('error.log', 'a') as f:
        f.write(f"ERROR: {error}\n")
