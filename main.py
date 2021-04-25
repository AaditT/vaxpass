from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=["POST", "GET"])
def add():
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)