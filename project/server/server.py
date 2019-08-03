from flask import Flask, render_template
import serial
import threading

ser = serial.Serial(
   port='COM11',
   baudrate=9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1)

app = Flask(__name__)


def receive_data():
    while True:
        rxdata = ser.readline().decode('utf-8')
        if rxdata:
            print(rxdata)
            return rxdata


@app.route('/')
def index():
    data = receive_data()
    return data


@app.route('/main')
def main():
    data = receive_data()
    temp = data[2:7]
    humid = data[9:14]
    return render_template('main.html', temp=temp, humid=humid)


if __name__ == '__main__':
    app.run(host='10.156.147.138', port=5000)