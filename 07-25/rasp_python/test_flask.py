 from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello My World'


@app.route('/sub1')
def sub1():
    return 'Hello My App'


if __name__ == '__main__':
    app.run(debug= True, host='192.168.137.119', port= 5000)