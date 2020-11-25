#  todo: basic flask app api setup (библиотеки подключи бля ежжи, братОК!)
#  UPD: сука, пока писал это, ко мне в пиво муха залетела, суккккааааа
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Kick Pashu'


if __name__ == "__main__":
    app.run()
