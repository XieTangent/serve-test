import requests

url = 'http://127.0.0.1:5000/receive_email'
data = {
    'sender': 'xietangent300@gmail.com',
    'subject': 'Test Subject',
    'content': 'Test Content'
}
response = requests.post(url, json=data)
print(response.text)
