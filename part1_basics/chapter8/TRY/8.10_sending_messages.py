messages = ['Hi', 'lol', 'bye']
sent_messages = []

def send_messages(messages, sent_messages):
    """Show some text messages"""
    while messages:
        current_message = messages.pop()
        print(f"Sending {current_message}")
        sent_messages.append(current_message)



send_messages(messages, sent_messages)

print(messages)
print(sent_messages)