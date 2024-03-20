from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2> Hello world! </h2>'

@app.route('/about')
def about():
    return ' <h1> Tentang kami </h2>'



if __name__ == '__main__':
    app.run(debug=True)

