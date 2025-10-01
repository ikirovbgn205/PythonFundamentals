number_of_messages = int(input())
message = ""
for _ in range(number_of_messages):
    message_code = int(input())

    if message_code == 86 :
        message = "How are you?"

    elif message_code == 88 :
        message = "Hello"

    elif message_code < 88 :
        message = "GREAT!"

    elif message_code > 88 :
        message = "Bye."

    print(message)
