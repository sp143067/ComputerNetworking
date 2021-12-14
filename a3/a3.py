import socket

SMTP_server = "berlioz.cs.unh.edu"
SMTP_port = 25
BUFFER_SIZE = 1024


def mailBody(sender, receiver, subject, body):
    """
     This is a string concatenation function where
     I am doing a string concatenation of message body
    """
    mail_header = 'From: ' + sender + '\n'
    mail_header += 'To: ' + receiver + '\n'
    mail_header += 'Subject: ' + subject + '\n'

    return mail_header + body + '\n.\r\n'


def mailFormat(sender, receiver, subject, body):
    """
    This function will return a list, which later
    used in the socketSMTP() as an iterator variable,
    to perform an SMTP conversation.
    """
    mail_domain = sender[sender.index('@') + 1:]
    helo = 'HELO ' + mail_domain + '\r\n'
    mail_from = 'MAIL FROM: ' + sender + '\r\n'
    rcpt_to = 'RCPT TO: ' + receiver + '\r\n'
    data = 'DATA\r\n'
    body = mailBody(sender, receiver, subject, body)

    return [helo, mail_from, rcpt_to, data, body]


def socketSMTP(sender, receiver, subject, body):
    """
    This is a function where I am creating TCP socket
    connection using SMTP server berlioz.cs.unh.edu &
    port 25. Then, I am performing SMTP conversation
    using socket.send & socket.recv method.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SMTP_server, SMTP_port))
        message = client_socket.recv(BUFFER_SIZE)
        message = message.decode("utf-8")
        # print('message: ', message.decode("utf-8"))
        if message[:3] != '220':
            print('SMTP server is not ready')
        else:
            print(message)
        mail_input = mailFormat(sender, receiver, subject, body)

        for cmnd in mail_input:
            print(cmnd)
            client_socket.send(bytes(cmnd, encoding="utf-8"))
            message = client_socket.recv(BUFFER_SIZE)
            message = message.decode("utf-8")
            if cmnd[:4] != 'DATA' and message[:3] != '250':
                print('Requested mail action has not completed!\n')
            elif cmnd[:4] == 'DATA' and message[:3] != '354':
                print('Requested mail action 354 is unresponsive!\n')
            elif message[:3] == '501':
                print('Please cross check the given domain name!\n')
            else:
                print(message)

    except ConnectionRefusedError:
        print("Please check your SMTP Host and port connection!")
        client_socket.close()


# storing the user-specified values of Sender, Recipient, Subject, Body
sender = input("Enter the Sender mail id in correctly formated: ")
receiver = input("Enter a valid Recipient mail id: ")
subject = input("Enter the Subject of your email: ")
body = input("Enter the Message you want to send: ")

# Sending an email by calling socketSMTP function
socketSMTP(sender, receiver, subject, body)

