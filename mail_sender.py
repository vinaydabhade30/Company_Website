import smtplib
import ssl


def email_sender_app(message):
    user_name = 'vinaydabhadeapp@gmail.com'
    password = 'rvqgzxxvdavqxlft'

    port = 465
    host = 'smtp.gmail.com'
    res_email = 'dsmlai4vinay2020@gmail.com'

    context_info = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context_info) as server:
        server.login(user_name, password)
        server.sendmail(user_name, res_email, message)


if __name__ == '__main__':
    email_sender_app('hello')
