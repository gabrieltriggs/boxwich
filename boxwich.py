import RPi.GPIO as GPIO
import time, datetime
import requests
GPIO.setmode(GPIO.BCM)

TOGGLE_SWITCH = 23
BUTTON = 24
LED = 25
isArmed = False
sandwichOrdered = False

GPIO.setup(TOGGLE_SWITCH, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def arm():
  global isArmed
  isArmed = True
  print "isArmed: %r" % (isArmed, )

def disarm():
  global isArmed
  isArmed = False
  print "isArmed: %r" % (isArmed, )

def toggle(channel):
  if GPIO.input(TOGGLE_SWITCH):
    disarm()
  else:
    arm()

def order(channel):
  print("Order button was pressed.")
  print(isArmed)
  if isArmed:
    # place sandwich order
    print("Placing sandwich order.")
    global sandwichOrdered
    sandwichOrdered = True
    requests.post("http://example.com:8080")
  else:
    print("Failed to place sandwich order. Box is currently disarmed.")

def setStatusLightOff():
  GPIO.output(LED, False)
  print("Status light is now off.")

def setStatusLightOn():
  GPIO.output(LED, True)
  print("Status light is now on.")
  
toggleDebounce = 50
buttonDebounce = 200
GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.BOTH, callback = toggle, bouncetime = toggleDebounce)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback = order, bouncetime = buttonDebounce)
setStatusLightOn()

while True:
  # do whatever you want to do repeatedly
  # this is absolutley just a placeholder
  timestamp = time.time()
  formattedTimestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
  print formattedTimestamp
  time.sleep(5)
