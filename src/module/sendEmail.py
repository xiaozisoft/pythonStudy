import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(email_list, content, subject="酱紫安"):
    msg = MIMEText(content, 'html', 'utf-8')
    # msg['From'] = formataddr(["酱",'502312648@qq.com'])
    msg['From'] = formataddr(["酱", '502312648@qq.com'])
    msg['Subject'] = subject
#     # SMTP服务
    try:
        # server = smtplib.SMTP("smtp.qq.com", 25)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.set_debuglevel(1)
        server.starttls()
        # server.login('502312648@qq.com', 'mjbsoieypuspbhdg')
        server.login('502312648@qq.com', 'test')
        server.sendmail('502312648@qq.com', email_list, msg.as_string())
        server.quit()
    except:
        print("error")


# email_list = ['502312648@qq.com', '3589307418@qq.com']
email_list = ['502312648@qq.com']
content = '<h1>hello</h1> <a href="http://baidu.com">百度一下，你就知道</a>'
email(email_list, content)
