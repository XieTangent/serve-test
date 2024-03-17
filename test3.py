from flask import Flask

# 创建一个 Flask 应用程序实例
app = Flask(__name__)

# 定义一个路由，指定 URL 和处理函数
@app.route('/')
def hello():
    return 'Hello, World!'

# 运行应用程序，并将主机地址设置为 '0.0.0.0'，允许外部访问
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
