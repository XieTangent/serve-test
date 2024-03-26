from pyngrok import ngrok
import subprocess
import os
import zipfile
from flask import Flask, request, jsonify, send_file

ngrok.set_auth_token('2eDyjBG5ZCqmkkjSY7mZ0yJmeca_LkQWYUdQw6rneRjtrrpn')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server is running'

@app.route('/compile', methods=['POST'])
def compile_verilog():

    verilog_file = request.files['file']

    verilog_file_path = 'temp.v'
    verilog_file.save(verilog_file_path)

    result = subprocess.run(['iverilog', '-o', 'temp.out', verilog_file_path], capture_output=True, text=True)

    if result.returncode == 0:
        zip_file_path = 'compiled_files.zip'
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            zipf.write('temp.out')

        return send_file(zip_file_path, as_attachment=True)
    else:
        return jsonify({'success': False, 'message': 'Error compiling Verilog code.', 'stderr': result.stderr})

if __name__ == '__main__':
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:5000\"".format(public_url))
    
    app.run(host='127.0.0.1', port=5000)
