from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # 使用 requests 获取页面内容
    url = "https://sso.douyin.com/?service=https://webcast.amemv.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers, allow_redirects=True)

    # 将响应内容返回给客户端
    return Response(response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(debug=True)