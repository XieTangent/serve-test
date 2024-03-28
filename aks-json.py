from pyngrok import ngrok
from datetime import datetime
import subprocess
import os
from flask import Flask, request, jsonify

ngrok.set_auth_token('2eDyjBG5ZCqmkkjSY7mZ0yJmeca_LkQWYUdQw6rneRjtrrpn')

app = Flask(__name__)


counte = 0

def get_number():
    global counte
    counte += 1
    return counte

def create_folders():
    if not os.path.exists('verilog_files'):
        os.makedirs('verilog_files')
    

@app.route('/')
def index():
    return 'Server is running'

@app.route('/compile', methods=['POST'])
def compile_verilog():
    verilog_code = request.json['verilog_code']

    num = get_number()
    current_time = datetime.now().strftime("%Hh%Mm%Ss%Y%m%d")
    verilog_file_name = f"verilog_files/verilog_{current_time}_{num}.v"
    compile_file_name = f"verilog_files/compile_{current_time}_{num}.vpp"


    with open(verilog_file_name, 'w') as f:
        f.write(verilog_code)

    result = subprocess.run(['iverilog', '-o',compile_file_name, verilog_file_name], capture_output=True, text=True)

    if result.returncode == 0:
        with open(compile_file_name,'r') as vpp_file:
            vpp_message = vpp_file.read()

        compilation_result = {
            "VVP Message" : vpp_message
        }
    else:
        compilation_result = {
            "Error Message"  : result.stderr
        }
    
    return jsonify(compilation_result)

if __name__ == '__main__':
    create_folders()
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))
    
    app.run(host='127.0.0.1', port=5000)
