from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    nama = "Anton Wijaya"
    return render_template('index.html', nama_kirim = nama)


if __name__ == '__main__':
    app.run(debug=True)
