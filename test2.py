import requests

# Flask 应用程序的 URL
url = 'http://127.0.0.1:5000/compile'

# Verilog 代码作为 JSON 对象
verilog_code = """
module test;
  reg clk;
  always #5 clk = ~clk;
endmodule
"""

# 发送 POST 请求，将 Verilog 代码作为 JSON 对象发送
response = requests.post(url, json={'code': verilog_code})

# 检查响应状态码
if response.status_code == 200:
    print("Verilog 代码已成功发送并编译。")
else:
    print("请求失败，状态码为:", response.status_code)
