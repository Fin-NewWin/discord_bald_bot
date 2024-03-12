def handle_response(msg):
    msg = msg.lower()
    if msg == "hello":
        return "Hi there!"
