import requests
from flask import Flask, jsonify

app = Flask(__name__)


# 创建一个简单的 GET 请求处理器
@app.route("/")
def hello_world():
    return "Hello, World!"


# 创建一个返回 JSON 数据的接口
@app.route("/api/data", methods=["GET"])
def get_data():
    data = {"name": "John", "age": 30, "city": "New York"}
    return jsonify(data)


# 创建天气查询接口
@app.route("/api/w/<city>", methods=["GET"])
def get_weather(city):
    api_key = "91a709ebda96b152133fd14fc1c58661"  # 请将 your_api_key 替换为您在 OpenWeatherMap 上获取的 API 密钥
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Failed to retrieve weather data"})


if __name__ == "__main__":
    app.run(debug=True)
