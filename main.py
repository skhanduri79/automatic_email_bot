import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_mail(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('****@gmail.com', '***')   # sender's email address

    email = EmailMessage()
    email['From'] = '****@gmail.com'  # sender's email
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {                   # list of emails 
    'apple': 'ooooooo@gmail.com',
    'orange': '999999@gmail.com',
    'chiku': '777777@gmail.com',
    'banana': '8888888@gmail.com'
}


def get_email_info():
    talk('To whom you want to send email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of the email?')
    subject = get_info()
    talk('Tell me the text for your email.')
    message = get_info()
    send_mail(receiver, subject, message)
    talk('Hey, your email is successfully sent! if you want to send more mails ? Yes or no ?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    elif 'no' in send_more:
        print('Thankyou for using this automated tool. See you again :)')

get_email_info()
