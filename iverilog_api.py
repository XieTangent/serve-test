import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_verilog():
    # 从请求中获取 Verilog 代码
    verilog_code = request.json.get('code', '')

    # 将 Verilog 代码写入到临时文件中
    with open('test-temp.v', 'w') as f:
        f.write(verilog_code)

    # 调用 Icarus Verilog 编译 Verilog 代码
    result = subprocess.run(['iverilog', '-o', 'test-temp.out', 'test-temp.v'], capture_output=True)

    # 返回编译结果
    if result.returncode == 0:
        return jsonify({'success': True, 'message': 'Verilog code compiled successfully.', 'output_file': 'test-temp.out'})
    else:
        return jsonify({'success': False, 'message': 'Error compiling Verilog code.', 'stderr': result.stderr.decode()})

if __name__ == '__main__':
    app.run(debug=True)
