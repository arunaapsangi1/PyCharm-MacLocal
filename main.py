# This is a sample Python script.
# create a hello world program
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Hello World")

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

#create a function to caluclate the factorial of a number using different options
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   #recursive call to the function itself  # 5 * 4 * 3 * 2 * 1 = 120



# create a function to send a simple email with the body and subject and it accepts email id as input
# i want to enhance this send_email function to really send an email
# i want to use a third party library to send an email
# 3rd party library is smtplib  # pip install smtplib
# what is the function to send an email?  # smtplib.SMTP.sendmail()
# what is the function to connect to the server?  # smtplib.SMTP.connect()
# create a function send an

def send_email(email_id, subject, body):
    print(f"Sending email to {email_id} with subject {subject} and body {body}")    # Press ⌘F8 to toggle the breakpoint

if __name__ != '__main__':
            pass
# Press the green button in the gutter to run the script.
else:  # See PyCharm help at https://www.jetbrains.com/help/pycharm/
    print_hi('Aruna, Great Move 2024')
    send_email("aruna.apsangi@gmail.com", "Hello", "Hello, How are you?") # why is this not printing the result?
    send_email("aruna.apsangi@cognizant.com", "Hello", "Hello, How are you?")  # why is this not printing the result?



