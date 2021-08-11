class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while not command == "Stop":
    command = command.split()
    info_sender = command[0]
    info_receiver = command[1]
    info_message = command[2]

    mail = Email(info_sender, info_receiver, info_message)
    emails.append(mail)

    command = input()

sent_mails = list(map(int, input().split(", ")))

for i in sent_mails:
    emails[i].send()

for mail in emails:
    print(mail.get_info())
