#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
from time import time, sleep
from RPi import GPIO
from flask import Flask, request, send_from_directory
import subprocess
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from urllib2 import Request, urlopen
import robot
from sys import argv

# GPIO Define
_DIST_L_TRIG_P = 5
_DIST_L_ECHO_P = 6
_DIST_R_TRIG_P = 7
_DIST_R_ECHO_P = 8
_INFR_P =        9
_RELAY_P =       10
_BUZ_P =         11

GPIO.setmode(GPIO.BCM)
GPIO.setup(_DIST_L_TRIG_P, GPIO.OUT)
GPIO.setup(_DIST_L_ECHO_P, GPIO.IN)
GPIO.setup(_DIST_R_TRIG_P, GPIO.OUT)
GPIO.setup(_DIST_R_ECHO_P, GPIO.IN)

class Inp():
	def __init__(self, pin):
		self.pin = pin
		self.value = False
		GPIO.setup(self.pin, GPIO.IN)
	def val(self):
		self.value = GPIO.input(self.pin)
		return self.value

class Outp():
	def __init__(self, pin):
		self.pin = pin
		self.value = False
		GPIO.setup(self.pin, GPIO.OUT)
	def val(self, v):
		self.value = v
		GPIO.output(self.pin, self.value)
		return self.value

# I2C Define
class Camera_Servo():
	def __init__(self, pwm = 1, pin = 0):
		self.pin = pin
		if pwm == 1:
			self.pwm = robot.pwm
		elif pwm == 2:
			self.pwm = robot.pwm2
		self.pulse = robot.servoDef
	def reset(self):
		self.pulse = robot.servoDef
		self.pwm.setPWM(0, 0, robot.servoDef)
	def act(self, act = 0):
		self.pulse += act
		if self.pulse < robot.servoMin:
			self.pulse = robot.servoMin
		elif self.pulse > robot.servoMax:
			self.pulse = robot.servoMax
		self.pwm.setPWM(0, 0, self.pulse)

inf = Inp(_INFR_P)
rly = Outp(_RELAY_P)
buz = Outp(_BUZ_P)
act = robot.Robot()
cam = Camera_Servo()

# Web Define
def getip():
	ifconfig = subprocess.check_output(['ifconfig']).decode().split('\n')
	ip = [i.split()[1].split(':')[1] for i in ifconfig if "inet addr:" in i]
	ip.remove('127.0.0.1')
	return ip[0]

if __name__ == '__main__':
#	CLOUD_IP = '192.168.2.58'
#	CLOUD_IP = '172.20.10.3'
	CLOUD_IP = argv[1]
	HOST_IP = getip()
	WEB_PORT = 80
	CAM_PORT = 8080
	WEB_DBG = False

	app = Flask(__name__)

	@app.route("/")
	def index_html():
		with open("../www/index.html") as f:
			s = f.read()
		s = s.replace("CLOUD_IP", CLOUD_IP)
		s = s.replace("HOST_IP", HOST_IP)
		s = s.replace("WEB_PORT", str(WEB_PORT))
		s = s.replace("CAM_PORT", str(CAM_PORT))
		return s

	@app.route("/file/<path:filename>")
	def send_my_file(filename):
		return send_from_directory('../www', filename)

	@app.route("/pan_<arg>")
	def camera_pan(arg):
		if arg == 'r':
			cam.act(-50)
		elif arg == 'l':
			cam.act(50)
		sleep(1)
		return ""

	@app.route("/act_<arg>")
	def movement_act(arg):
		if arg == 'rl':
			act.TurnLeft(1)
		elif arg == 'rr':
			act.TurnRight(1)
		elif arg == 'f':
			act.Forward(1)
		elif arg == 'b':
			act.Back(1)
		elif arg == 'l':
			act.ShiftLeft(1)
		elif arg == 'r':
			act.ShiftRight(1)
		elif arg == 'a':
			act.Attention()
		return ""

	distance_l = distance_r = 0.0
	same_dist = 0
	same_dist_t = time()
	@app.route("/sw_<arg>")
	def movement_actsw(arg):
		if arg == 'm':
			if inf.val() == 1:
				com = "wget http://%s:8080/?action=snapshot -O output.jpg" % HOST_IP
				subprocess.Popen(com, shell = True, stdout = subprocess.PIPE)
				buz.val(1)
				sleep(1)
				buz.val(0)
				register_openers()
				datagen, headers = multipart_encode({"image1": open("output.jpg", 'rb')})
				request = Request("http://%s/server.php" % CLOUD_IP, datagen, headers)
				print urlopen(request).read()
				sleep(1)
			return ""
		elif arg == 'a':
			global distance_l, distance_r, same_dist, same_dist_t
			if distance_l < 30.0 and distance_r < 30.0:
				t = time()
				b1 = bool(t - same_dist_t > 10000)
				b2 = bool(same_dist % 2 == 0)
				if b1 != b2:
					act.TurnLeft(1)
				else:
					act.TurnRight(1)
				if b1:
					same_dist = 1 - same_dist
				same_dist_t = t
			elif distance_l < 30.0:
				act.TurnLeft(1)
			elif distance_r < 30.0:
				act.TurnRight(1)
			else:
				act.Forward(1)
			return ""

	@app.route("/jp_<arg>")
	def movement_link(arg):
		if arg == 'c':
			pass
		elif arg == 'd':
			com = "wget http://%s:8080/?action=snapshot -O output.jpg" % HOST_IP
			subprocess.Popen(com, shell = True, stdout = subprocess.PIPE)
		return ""

	def send_trigger_pulse(trigger_pin):
		GPIO.output(trigger_pin, True)
		sleep(0.001)
		GPIO.output(trigger_pin, False)
	def wait_for_echo(echo_pin, value, timeout):
		count = timeout
		while GPIO.input(echo_pin) != value and count > 0:
			count = count - 1

	@app.route("/dist")
	def distance():
		global distance_l, distance_r
		send_trigger_pulse(_DIST_L_TRIG_P)
		wait_for_echo(_DIST_L_ECHO_P, True, 5000)
		start = time()
		wait_for_echo(_DIST_L_ECHO_P, False, 5000)
		finish = time()
		pulse_len = finish - start
		distance_l = pulse_len * 17000
		send_trigger_pulse(_DIST_R_TRIG_P)
		wait_for_echo(_DIST_R_ECHO_P, True, 5000)
		start = time()
		wait_for_echo(_DIST_R_ECHO_P, False, 5000)
		finish = time()
		pulse_len = finish - start
		distance_r = pulse_len * 17000
		return str(distance_l) + ',' + str(distance_r)

	@app.route("/upload")
	def upload():
		register_openers()
		datagen, headers = multipart_encode({"image1": open("output.jpg", 'rb')})
		request = Request("http://%s/server.php" % CLOUD_IP, datagen, headers)
		print urlopen(request).read()

	app.run(host = '0.0.0.0', port = WEB_PORT, debug = WEB_DBG)

