# Самостоятельно реализуйте графическое приложение для отправки произвольного
# письма клиенту: На форме выводится информация об отправителе, адрес
# получателя, тема и содержание письма вводятся клиентом (см. рис.).
# Изучите и реализуйте возможность загрузки и отправки с письмом прикрепленных
# файлов.

import tkinter

def send_mail(sender, recipient, subject, message, login, password):
    import smtplib
    from email.message import EmailMessage
    
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    
    # with open('attachment.txt', 'r') as f:
    #     attachment = f.read()
        
    # message.set_content(message)
    # message.add_attachment(attachment, maintype='text', subtype='plain', filename='attachment.txt')

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(login, password)
    s.sendmail(sender, recipient, message)
    s.quit()

window = tkinter.Tk()
window.title('Отправка письма')
window.geometry('600x380')
window.resizable(width=False, height=False)

sender = tkinter.Label(window, text='Отправитель')
sender.grid(row=0, column=0, sticky=tkinter.W)
sender_entry = tkinter.Entry(window, width=50)
sender_entry.grid(row=0, column=1, columnspan=2, sticky=tkinter.W)

recipient = tkinter.Label(window, text='Получатель')
recipient.grid(row=1, column=0, sticky=tkinter.W)
recipient_entry = tkinter.Entry(window, width=50)
recipient_entry.grid(row=1, column=1, columnspan=2, sticky=tkinter.W)

subject = tkinter.Label(window, text='Тема')
subject.grid(row=2, column=0, sticky=tkinter.W)
subject_entry = tkinter.Entry(window, width=50)
subject_entry.grid(row=2, column=1, columnspan=2, sticky=tkinter.W)

message = tkinter.Label(window, text='Сообщение')
message.grid(row=3, column=0, sticky=tkinter.W)
message_entry = tkinter.Text(window, width=50, height=10)
message_entry.grid(row=3, column=1, columnspan=2, sticky=tkinter.W)

login_label = tkinter.Label(window, text='Логин')
login_label.grid(row=4, column=0, sticky=tkinter.W)
login_entry = tkinter.Entry(window, width=50)
login_entry.grid(row=4, column=1, columnspan=2, sticky=tkinter.W)

password_label = tkinter.Label(window, text='Пароль')
password_label.grid(row=5, column=0, sticky=tkinter.W)
password_entry = tkinter.Entry(window, width=50)
password_entry.grid(row=5, column=1, columnspan=2, sticky=tkinter.W)

button = tkinter.Button(
    window,
    text='Отправить',
    command=lambda: send_mail(sender_entry.get(), recipient_entry.get(
    ), subject_entry.get(), message_entry.get('1.0', tkinter.END)))
button.grid(row=6, column=1, sticky=tkinter.W)

window.mainloop()