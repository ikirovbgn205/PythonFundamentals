class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

while True:

    command = input().split()

    if command[0] == 'Stop':
        break

    sender, receiver, content = command[0], command[1], command[2]

    email = Email(sender, receiver, content)
    emails.append(email)

indices = [int(i) for i in input().split(", ")]

for index in indices:
    emails[index].send()

for email in emails:
    print(email.get_info())
