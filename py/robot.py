#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
if __name__ == '__main__':
    from sys import argv
    from getopt import getopt, GetoptError

pwm = PWM(0x41)
pwm2 = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x41, debug=True)
#pwm2 = PWM(0x40,debug=True)

#########
#0x41
#########
_A1 = 7
_A2 = 6
_A3 = 5
_B1 = 11
_B2 = 10
_B3 = 9
_C1 = 15
_C2 = 14
_C3 = 13
#########
#0x40
#########
_D1 = 8
_D2 = 9
_D3 = 10
_E1 = 4
_E2 = 5
_E3 = 6
_F1 = 0
_F2 = 1
_F3 = 2

'''
#this value is for GO-TEEk SG9018
servoMin = 170 # Min pulse length out of 4096
servoDef = 332 # Middle pulse length out of 4096
servoMax = 500 # Max pulse length out of 4096
servoRight = 248
servoLeft  = 40.55 
servoRigh  = 276
servoLef   = 388 
'''
# this valus is for Tower-Pro SG90S
servoMin = 230 # Min pulse length out of 4096
servoDef = 350 # Middle pulse length out of 4096
servoMax = 470 # Max pulse length out of 4096

servoRight = 260
servoLeft  = 440 

servoRigh  = 290
servoLef   = 410 

pwm.setPWMFreq(50)  # Set frequency to 50 Hz
pwm2.setPWMFreq(50) # Set frequency to 50 Hz

class Robot:
	help_msg = '''
    Robot[option]
    option:
	C [CMD File]
	A [Attention]
	F [Forward]
	B [Back]
	L [TurnLeft]]
	R [TurnRight]
	l [ShiftLeft]
	r [ShiftRight]
	
	command :
	T:(sec) --> delay time
	
	ex:
	    'A T2 F3 T0.3 T2 B3 T0.3 L3'
    '''

	def Attention(self):
		print("Attention")
		pwm.setAllPWM(0,servoDef)
		pwm2.setAllPWM(0,servoDef)
		time.sleep(1)
  	
	def Forward(self, cnt=1):
		cnt=int(cnt)
		print "Forward %d" % cnt
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#STEP1			
		#pwm.setPWM(_A3,0,servoDef)
		#pwm.setPWM(_C3,0,servoDef)
		#pwm2.setPWM(_E3,0,servoDef)
		#pwm.setPWM(_B3,0,servoDef)
		#pwm2.setPWM(_D3,0,servoDef)
		#pwm2.setPWM(_F3,0,servoDef)
		#STEP2
		pwm.setPWM(_A2,0,servoLeft)
		pwm.setPWM(_C2,0,servoLeft)
		pwm2.setPWM(_E2,0,servoRight)
		#time.sleep(1)
		pwm.setPWM(_A1,0,servoRight)
		pwm.setPWM(_C1,0,servoRight)
		pwm2.setPWM(_E1,0,servoLeft)
		time.sleep(0.3)
		while(cnt>0):
			#STEP3
			pwm.setPWM(_A2,0,servoDef)
			pwm.setPWM(_C2,0,servoDef)
			pwm2.setPWM(_E2,0,servoDef)
			time.sleep(0.3)
			pwm.setPWM(_A1,0,servoDef)
			pwm.setPWM(_C1,0,servoDef)
			pwm2.setPWM(_E1,0,servoDef)
			time.sleep(0.3)
			#STEP4
			pwm.setPWM(_B2,0,servoLeft)
			pwm2.setPWM(_D2,0,servoRight)
			pwm2.setPWM(_F2,0,servoRight)
			#time.sleep(1)
			pwm.setPWM(_B1,0,servoRigh)
			pwm2.setPWM(_D1,0,servoLeft)
			pwm2.setPWM(_F1,0,servoLeft)
			time.sleep(0.3)
			#STEP5
			pwm.setPWM(_B2,0,servoDef)
			pwm2.setPWM(_D2,0,servoDef)
			pwm2.setPWM(_F2,0,servoDef)
			time.sleep(0.3)
			pwm.setPWM(_B1,0,servoDef)
			pwm2.setPWM(_D1,0,servoDef)
			pwm2.setPWM(_F1,0,servoDef)
			time.sleep(0.3)
			#STEP6
			pwm.setPWM(_A2,0,servoLeft)
			pwm.setPWM(_C2,0,servoLeft)
			pwm2.setPWM(_E2,0,servoRight)
			#time.sleep(1)
			pwm.setPWM(_A1,0,servoRight)
			pwm.setPWM(_C1,0,servoRight)
			pwm2.setPWM(_E1,0,servoLeft)
			time.sleep(0.3)
			cnt -= 1
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#time.sleep(1)
		
	def Back(self, cnt=1):
		cnt=int(cnt)
		print "Back %d" % cnt
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#STEP1
		pwm.setPWM(_A3,0,servoDef)
		pwm.setPWM(_C3,0,servoDef)
		pwm2.setPWM(_E3,0,servoDef)
		pwm.setPWM(_B3,0,servoDef)
		pwm2.setPWM(_D3,0,servoDef)
		pwm2.setPWM(_F3,0,servoDef)
		#STEP2
		pwm.setPWM(_A2,0,servoLeft)
		pwm.setPWM(_C2,0,servoLeft)
		pwm2.setPWM(_E2,0,servoRight)
		#time.sleep(1)
		pwm.setPWM(_A1,0,servoLeft)
		pwm.setPWM(_C1,0,servoLeft)
		pwm2.setPWM(_E1,0,servoRight)
		time.sleep(0.3)
		while(cnt>0):
			#STEP3
			pwm.setPWM(_A2,0,servoDef)
			pwm.setPWM(_C2,0,servoDef)
			pwm2.setPWM(_E2,0,servoDef)
			time.sleep(0.3)
			pwm.setPWM(_A1,0,servoDef)
			pwm.setPWM(_C1,0,servoDef)
			pwm2.setPWM(_E1,0,servoDef)
			time.sleep(0.3)
			#STEP4
			pwm.setPWM(_B2,0,servoLeft)
			pwm2.setPWM(_D2,0,servoRight)
			pwm2.setPWM(_F2,0,servoRight)
			#time.sleep(1)
			pwm.setPWM(_B1,0,servoLeft)
			pwm2.setPWM(_D1,0,servoRight)
			pwm2.setPWM(_F1,0,servoRight)
			time.sleep(0.3)
			#STEP5
			pwm.setPWM(_B2,0,servoDef)
			pwm2.setPWM(_D2,0,servoDef)
			pwm2.setPWM(_F2,0,servoDef)
			time.sleep(0.3)
			pwm.setPWM(_B1,0,servoDef)
			pwm2.setPWM(_D1,0,servoDef)
			pwm2.setPWM(_F1,0,servoDef)
			time.sleep(0.3)
			#STEP6
			pwm.setPWM(_A2,0,servoLeft)
			pwm.setPWM(_C2,0,servoLeft)
			pwm2.setPWM(_E2,0,servoRight)
			#time.sleep(1)
			pwm.setPWM(_A1,0,servoLeft)
			pwm.setPWM(_C1,0,servoLeft)
			pwm2.setPWM(_E1,0,servoRight)
			time.sleep(0.3)
			cnt -= 1
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#time.sleep(1)
	
	def TurnLeft(self, cnt=1):
		cnt=int(cnt)
		print "TurnLeft %d" % cnt
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		time.sleep(1)
		while(cnt>0):
			pwm.setPWM(_A3,0,servoDef)
			pwm.setPWM(_C3,0,servoDef)
			pwm2.setPWM(_E3,0,servoDef)
			pwm.setPWM(_A2,0,servoLef)
			pwm.setPWM(_C2,0,servoLef)
			pwm2.setPWM(_E2,0,servoRigh)
			#time.sleep(1)
			pwm.setPWM(_A1,0,servoLef)
			pwm.setPWM(_C1,0,servoLef)
			pwm2.setPWM(_E1,0,servoLef)
			pwm.setPWM(_B1,0,servoRigh)
			pwm2.setPWM(_D1,0,servoRigh)
			pwm2.setPWM(_F1,0,servoRigh)
			time.sleep(1)
			pwm.setPWM(_A2,0,servoDef)
			pwm.setPWM(_C2,0,servoDef)
			pwm2.setPWM(_E2,0,servoDef)
			time.sleep(1)
			pwm.setPWM(_B3,0,servoDef)
			pwm2.setPWM(_D3,0,servoDef)
			pwm2.setPWM(_F3,0,servoDef)
			pwm.setPWM(_B2,0,servoLef)
			pwm2.setPWM(_D2,0,servoRigh)
			pwm2.setPWM(_F2,0,servoRigh)
			#time.sleep(1)
			pwm.setPWM(_B1,0,servoLef)
			pwm2.setPWM(_D1,0,servoLef)
			pwm2.setPWM(_F1,0,servoLef)
			pwm.setPWM(_A1,0,servoRigh)
			pwm.setPWM(_C1,0,servoRigh)
			pwm2.setPWM(_E1,0,servoRigh)
			time.sleep(1)
			pwm.setPWM(_B2,0,servoDef)
			pwm2.setPWM(_D2,0,servoDef)
			pwm2.setPWM(_F2,0,servoDef)
			time.sleep(1)
			cnt -= 1
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#time.sleep(1)
	
	def TurnRight(self, cnt=1):
		cnt=int(cnt)
		print "TurnRight %d" % cnt
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		time.sleep(1)
		while(cnt>0):
			pwm.setPWM(_A3,0,servoDef)
			pwm.setPWM(_C3,0,servoDef)
			pwm2.setPWM(_E3,0,servoDef)
			pwm.setPWM(_A2,0,servoLeft)
			pwm.setPWM(_C2,0,servoLeft)
			pwm2.setPWM(_E2,0,servoRight)
			#time.sleep(1)
			pwm.setPWM(_A1,0,servoRigh)
			pwm.setPWM(_C1,0,servoRigh)
			pwm2.setPWM(_E1,0,servoRigh)
			pwm.setPWM(_B1,0,servoLef)
			pwm2.setPWM(_D1,0,servoLef)
			pwm2.setPWM(_F1,0,servoLef)
			time.sleep(1)
			pwm.setPWM(_A2,0,servoDef)
			pwm.setPWM(_C2,0,servoDef)
			pwm2.setPWM(_E2,0,servoDef)
			time.sleep(1)
			pwm.setPWM(_B3,0,servoDef)
			pwm2.setPWM(_D3,0,servoDef)
			pwm2.setPWM(_F3,0,servoDef)
			pwm.setPWM(_B2,0,servoLeft)
			pwm2.setPWM(_D2,0,servoRight)
			pwm2.setPWM(_F2,0,servoRight)
			#time.sleep(1)
			pwm.setPWM(_B1,0,servoRigh)
			pwm2.setPWM(_D1,0,servoLef)
			pwm2.setPWM(_F1,0,servoLef)
			pwm.setPWM(_A1,0,servoLef)
			pwm.setPWM(_C1,0,servoLef)
			pwm2.setPWM(_E1,0,servoLef)
			time.sleep(1)
			pwm.setPWM(_B2,0,servoDef)
			pwm2.setPWM(_D2,0,servoDef)
			pwm2.setPWM(_F2,0,servoDef)
			time.sleep(1)
			cnt -= 1
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#time.sleep(1)
	
	def ShiftLeft(self, cnt=1):
		cnt=int(cnt)
		print "ShiftLeft %d" % cnt
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		time.sleep(1) 
			
		pwm.setPWM(_A1,0,servoMax-0)
		pwm.setPWM(_C1,0,servoMin+0)
		pwm2.setPWM(_D1,0,servoMin+0)
		pwm2.setPWM(_F1,0,servoMax-0)
		
		pwm.setPWM(_B1,0,servoDef-0)
		pwm2.setPWM(_E1,0,servoDef)
		time.sleep(1)
		
		while(cnt>0):
			
			#############################
			pwm.setPWM(_A2,0,servoLeft)
			pwm.setPWM(_C2,0,servoLeft+50)
			pwm2.setPWM(_E2,0,servoRight)
			pwm.setPWM(_A3,0,servoDef)
			pwm.setPWM(_C3,0,servoDef)
			pwm2.setPWM(_E3,0,servoDef)
			time.sleep(1)
			pwm.setPWM(_B3,0,servoLef)
			pwm2.setPWM(_D3,0,servoLef)
			pwm2.setPWM(_F3,0,servoLef)
			#time.sleep(1)
			pwm.setPWM(_A2,0,servoDef)
			pwm.setPWM(_C2,0,servoDef)
			pwm2.setPWM(_E2,0,servoDef)
			time.sleep(1)
			##############################
			pwm.setPWM(_B2,0,servoLeft)
			pwm2.setPWM(_D2,0,servoRight)
			pwm2.setPWM(_F2,0,servoRight)
			pwm.setPWM(_B3,0,servoDef)
			pwm2.setPWM(_D3,0,servoDef)
			pwm2.setPWM(_F3,0,servoDef)
			time.sleep(1)
			pwm.setPWM(_A3,0,servoLef)
			pwm.setPWM(_C3,0,servoLef)
			pwm2.setPWM(_E3,0,servoLef)
			#time.sleep(1)
			pwm.setPWM(_B2,0,servoDef)
			pwm2.setPWM(_D2,0,servoDef)
			pwm2.setPWM(_F2,0,servoDef)
			time.sleep(1)
			cnt -= 1
			
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#time.sleep(1)
			
	def ShiftRight(self, cnt=1):
		cnt=int(cnt)
		print"ShiftRight %d" % cnt
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		time.sleep(1)
		
		pwm.setPWM(_A1,0,servoMax-0)
		pwm.setPWM(_C1,0,servoMin+0)
		pwm2.setPWM(_D1,0,servoMin+0)
		pwm2.setPWM(_F1,0,servoMax-0)
		
		pwm.setPWM(_B1,0,servoDef-0)
		pwm2.setPWM(_E1,0,servoDef)
		time.sleep(1)
		
		while(cnt>0):
			
			#############################
			pwm.setPWM(_A2,0,servoLeft)
			pwm.setPWM(_C2,0,servoLeft+50)
			pwm2.setPWM(_E2,0,servoRight)
			pwm.setPWM(_A3,0,servoDef)
			pwm.setPWM(_C3,0,servoDef)
			pwm2.setPWM(_E3,0,servoDef)
			time.sleep(1)
			pwm.setPWM(_B3,0,servoRigh)
			pwm2.setPWM(_D3,0,servoRigh)
			pwm2.setPWM(_F3,0,servoRight-50)
			#time.sleep(1)
			pwm.setPWM(_A2,0,servoDef)
			pwm.setPWM(_C2,0,servoDef)
			pwm2.setPWM(_E2,0,servoDef)
			time.sleep(1)
			##############################
			pwm.setPWM(_B2,0,servoLeft)
			pwm2.setPWM(_D2,0,servoRight)
			pwm2.setPWM(_F2,0,servoRight)
			pwm.setPWM(_B3,0,servoDef)
			pwm2.setPWM(_D3,0,servoDef)
			pwm2.setPWM(_F3,0,servoDef)
			time.sleep(1)
			pwm.setPWM(_A3,0,servoRigh+30)
			pwm.setPWM(_C3,0,servoRigh)
			pwm2.setPWM(_E3,0,servoRigh)
			#time.sleep(1)
			pwm.setPWM(_B2,0,servoDef)
			pwm2.setPWM(_D2,0,servoDef)
			pwm2.setPWM(_F2,0,servoDef)
			time.sleep(1)
			cnt -= 1
			
		#pwm.setAllPWM(0,servoDef)
		#pwm2.setAllPWM(0,servoDef)
		#time.sleep(1)

	def setByCommand(self,cmd):
		delay_time_us = 0
		count_dic = {}
		reset_flag = 0
		for i in cmd.split():
			#_ch = -1
			_count = -1
				
			if (i[0] == 'T'):
				_count = float(i[1:])
				print"wait %.2f sec" % _count 
				time.sleep(_count)
			
			elif (i[0] == 'A'):
				self.Attention()
			#reset_flag = 0.5
				
			elif (i[0] == 'F'):
				#_ch = int(_line[0][0.5:])
				_count = int(i[1:])
				self.Forward(_count)
				
			elif (i[0] == 'B'):
				#_ch = int(_line[0][0.5:])
				_count = int(i[1:])
				self.Back(_count)
				
			elif (i[0] == 'L'):
				#_ch = int(_line[0][0.5:])
				_count = int(i[1:])
				self.TurnLeft(_count)
					
			elif (i[0] == 'R'):
				#_ch = int(_line[0][0.5:])
				_count = int(i[1:])
				self.TurnRight(_count)
				
			elif (i[0] == 'l'):
				#_ch = int(_line[0][0.5:])
				_count = int(i[1:])
				self.ShiftLeft(_count)
			
			elif (i[0] == 'r'):
				#_ch = int(_line[0][0.5:])
				_count = int(i[1:])
				self.ShiftRight(_count)
		
		time.sleep(delay_time_us/1000000.0)
		#self.setByCountDic(count_dic)

	def setByCMDList(self, cmd_list):
		for i in cmd_list:
			self.setByCommand(i)
'''
	def Climb(self):
		print "Climb"
		pwm.setPWM(_A1,0,servoMax-0)
		pwm2.setPWM(_D1,0,servoMin+0)
		time.sleep(0.3)
		pwm.setPWM(_B2,0,servoMax)
		pwm2.setPWM(_E2,0,servoMin)
		time.sleep(0.3)
		pwm.setPWM(_B1,0,servoRigh)
		pwm2.setPWM(_E1,0,servoLef)
		time.sleep(0.3)
		pwm.setPWM(_B2,0,servoDef)
		pwm2.setPWM(_E2,0,servoDef)
		pwm.setPWM(_C1,0,servoLeft)
		pwm2.setPWM(_F1,0,servoRight)
		time.sleep(0.3)
		pwm.setPWM(_A2,0,servoMax+30)
		pwm2.setPWM(_D2,0,servoMin-30)
		time.sleep(0.3)
		pwm.setPWM(_A1,0,servoMin+60)
		pwm2.setPWM(_D1,0,servoMax-60)
		time.sleep(0.3)
		pwm.setPWM(_C2,0,servoRigh)
		pwm2.setPWM(_F2,0,servoLef)
		time.sleep(0.3)
		pwm.setPWM(_B1,0,servoDef)
		pwm2.setPWM(_E1,0,servoDef)
		pwm.setPWM(_C3,0,servoRight)
		pwm2.setPWM(_F3,0,servoLeft)
		time.sleep(0.3)
		time.sleep(5)
'''

if __name__ == '__main__':
	action = Robot()
	pwm.setAllPWM(0,servoDef)
	pwm2.setAllPWM(0,servoDef)
	time.sleep(1)
	try:
		opts, args = getopt(argv[1:], "HCAF:B:R:L:r:l:", 
		 ["Help", "CMD Line", "Attention", "Forward=", "Back=", "TurnRight=", "TurnLeft=", "ShiftRight=", "ShiftLeft="])
	except GetoptError as err:
		print str(err)
		print action.help_msg
		exit()
	if not opts:
		print action.help_msg
		exit()
	for o, a in opts:
			if o in ("-H", "--Help"):
				print action.help_msg
			elif o in ("-A", "--Attention"):
				action.Attention()
			elif o in ("-F", "--Forward"):
				action.Forward(a)
			elif o in ("-B", "--Back"):
				action.Back(a)
			elif o in ("-R", "--TurnRight"):
				action.TurnRight(a)
			elif o in ("-L", "--TurnLeft"):
				action.TurnLeft(a)
			elif o in ("-r", "--ShiftRight"):
				action.ShiftRight(a)
			elif o in ("-l", "--ShiftLeft"):
				action.ShiftLeft(a)
			elif o in ("-C", "--setByCMDList"):
				ff = open(argv[2], 'r')
				cmd_lines = ff.readlines()
				ff.close()
				action.setByCMDList(cmd_lines)
	
	pwm.setAllPWM(0,servoDef)
	pwm2.setAllPWM(0,servoDef)
