from flask import Flask, request

app = Flask(__name__)

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

        # 在此处可以进行进一步的处理，例如保存到数据库、发送通知等

        return 'Email received successfully!', 200
    else:
        return 'Invalid email data format!', 400

if __name__ == '__main__':
    app.run(debug=True)
