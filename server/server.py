from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/temp/demo')
def temp_demo():
    return render_template('demo.temp.html')


if __name__ == "__main__":
    app.run(debug=True)
