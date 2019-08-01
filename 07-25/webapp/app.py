  import RPi.GPIO as GPIO
from flask import Flask, render_template
import serial
import threading

curTemp = 0.0
curHumi = 0.0
curCds = 0

ser = serial.Serial(port='/dev/ttyACM0',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)


def led_on():
	GPIO.output(26, 1)
	return

def led_off():
	GPIO.output(26, 0)
	return

@app.route('/')
def index():
	led_off()
	return render_template('index.html', state='OFF')
	
@app.route('/on/')
def on():
	led_on()
	print ('Switch On')
	return render_template('index.html', state='ON')

@app.route('/off/')
def off():
	led_off()
	print ('Switch Off')
	return render_template('index.html', state='OFF')
		
@app.route('/sensor/')
def sensor():
	prevdata = '';
	rxdata = ser.readline().decode('utf-8')
	while (rxdata):
		prevdata = rxdata
		rxdata = ser.readline().decode('utf-8')
		
	if prevdata:
		return render_template('index.html', temp=float(prevdata[1:6]), humi=float(prevdata[7:12]), cds=int(prevdata[13:16]))
	return render_template('index.html')

if __name__=='__main__':
	print('Web Server Starts')

	app.run(debug=True, host='192.168.137.76', port=8000)
	print('Web Server Ends')
	ser.close()


GPIO.cleanup()
print('Program Ends')

