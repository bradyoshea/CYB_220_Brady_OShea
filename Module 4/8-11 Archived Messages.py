message_list = [
    "Hello John",
    "Hey Bill",
    "Are you free Friday?",
    "Yes, I am available"
]

sent_messages = []

def send_messages(messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

send_messages(message_list[:])
print(message_list)
print(sent_messages)