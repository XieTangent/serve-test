from flask import Flask, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(receiver_email, subject, message):
    # 邮件服务器配置
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # 默认端口号为587
    sender_email = 'xietangent300@gmail.com'
    sender_password = 'ylsh0813'

    # 创建邮件内容
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # 连接到邮件服务器并发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败:", e)

@app.route('/receive_email', methods=['POST'])
def receive_email():
    # 获取对方发送的电子邮件内容
    email_data = request.get_json()

    # 在此处处理电子邮件内容
    # 这里只是一个简单的示例，你可以根据实际需求进行处理
    if 'sender' in email_data and 'subject' in email_data and 'content' in email_data:
        sender = email_data['sender']
        subject = email_data['subject']
        content = email_data['content']

        # 发送邮件通知
        receiver_email = sender  # 假设将通知发送给邮件的发送者
        subject = '邮件接收成功通知'
        message = '你成功了！'
        send_email(receiver_email, subject, message)

        return 'Email received successfully!', 200
    else:
        return 'Invalid email data format!', 400

if __name__ == '__main__':
    app.run(debug=True)
