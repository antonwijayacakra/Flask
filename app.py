from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2> Hello world! </h2>'

@app.route('/about')
def about():
    return 'Tentang kami'


if __name__ == '__main__':
    app.run(debug=True)

