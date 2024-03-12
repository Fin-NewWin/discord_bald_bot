def handle_response(message) -> str:
    message = message.lower()
    if message == "hello":
        return "Hi there!"
    return ""
