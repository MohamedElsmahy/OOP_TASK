import re

def SendEmail():
    send_from = input('please enter your email')
    send_to = input('please enter the receiver email')
    subject = input('please enter your message')
    name = 'Mohamed'
    email_pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    email_from = re.match(email_pattern, send_from)
    email_to = re.match(email_pattern, send_to)

    try:
        email_file = open("email.txt", "a")
    except:
        print("file not found")
    else:
        email_file.write(
            f'From :{email_from}\nTo :{email_to}\nHI,{name}\nsubject:{subject}\nThanks\n__________________\n')