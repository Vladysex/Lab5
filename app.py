from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

APP_VERSION = "1.0.0"


@app.route("/")
def index():
    return f"""
    <html>
    <head><title>CI/CD Demo App</title></head>
    <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
        <h1>Присяжнюк В. В. Іа-з31!</h1>
	<h2>Додаємо текст для демонстрації автоматичного оновлення сторінки</h2>
        <p>Версія застосунку: <b>{APP_VERSION}</b></p>
        <p>Hostname контейнера: <b>{socket.gethostname()}</b></p>
        <p>Поточний час на сервері: {datetime.datetime.now()}</p>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="ok", version=APP_VERSION)


@app.route("/api/info")
def info():
    return jsonify(
        app="CI/CD Demo",
        version=APP_VERSION,
        hostname=socket.gethostname(),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
