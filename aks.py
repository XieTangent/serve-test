import requests

url = 'https://fa54-60-250-225-147.ngrok-free.app/compile'

verilog_file_path = 'test.v'

with open(verilog_file_path, 'r', encoding='utf-8') as file:
    verilog_code = file.read()

files = {'file': (verilog_file_path, verilog_code)}

response = requests.post(url, files=files)

if response.status_code == 200:
    with open('response.v', 'w', encoding='utf-8') as output_file:
        output_file.write(response.text)
    print("File saved successfully.")
else:
    print("Error:", response.text)