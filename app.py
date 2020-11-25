#  todo: basic flask app api setup (библиотеки подключи бля ежжи, братОК!)
#  UPD: сука, пока писал это, ко мне в пиво муха залетела, суккккааааа
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(port=15000)
