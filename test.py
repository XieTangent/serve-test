import requests

# 设置请求的URL
url = 'http://127.0.0.1:5000/compile'

# 设置Verilog代码
verilog_code = """
module test;
  reg clk;
  initial begin
    clk = 0;
    forever #5 clk = ~clk;
  end
endmodule
"""

# 构建请求数据
data = {'code': verilog_code}

# 发送POST请求
response = requests.post(url, json=data)

# 输出响应内容
print(response.json())
