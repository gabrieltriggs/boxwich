# boxwich.py
#
# Triggs, Gabriel
# 2014-10-26
# Developed for HackNC with Jon Johnson and Taylor King

import RPi.GPIO as GPIO
import time, datetime
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TOGGLE_SWITCH = 23
BUTTON = 24
LED = 25

GPIO.setup(TOGGLE_SWITCH, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

isArmed = False
hasOrderedSandwich = False

def arm():
  print "arm()"
  global isArmed
  isArmed = True
  print "Box has been armed."

def disarm():
  print "disarm()"
  global isArmed
  isArmed = False
  print "Box has been disarmed."
  global hasOrderedSandwich
  hasOrderedSandwich = False
  setStatusLightOn()

def toggle(channel):
  print "toggle()"
  if GPIO.input(TOGGLE_SWITCH):
    disarm()
  else:
    arm()

def order(channel):
  print "order()"
  global isArmed
  global hasOrderedSandwich
  if isArmed and not hasOrderedSandwich:
    print "Sending HTTP request to order sandwich."
    requests.post("http://example.com:8080")
    global hasOrderedSandwich
    hasOrderedSandwich = True
    print "Sandwich has been ordered."
    showConfirmationBlinks()
  elif isArmed and hasOrderedSandwich:
    print "Box has not been properly re-armed since last sandwich order." 
    print "Please disarm, arm, and try again."
  else:
    print "Box is not armed. Flip the safety switch and try again."

def setStatusLightOff():
  print "setStatusLightOff()"
  GPIO.output(LED, False)

def setStatusLightOn():
  print "setStatusLightOn()"
  GPIO.output(LED, True)

def showConfirmationBlinks():
  print "showConfirmationBlinks()"
  for i in range (0, 3):
    setStatusLightOn()
    time.sleep(0.75)
    setStatusLightOff()
    time.sleep(0.75)

toggleSwitchDebounce = 50 # ms
buttonDebounce = 200 # ms
GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.BOTH, callback = toggle, bouncetime = toggleSwitchDebounce)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback = order, bouncetime = buttonDebounce)

setStatusLightOn()
while True:
  timestamp = time.time()
  formattedTimestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
  print formattedTimestamp
  time.sleep(10)  
