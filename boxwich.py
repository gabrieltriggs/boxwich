import RPi.GPIO as GPIO
import time, datetime
GPIO.setmode(GPIO.BCM)

TOGGLE_SWITCH = 23
BUTTON = 24
LED = 25
isArmed = False

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
  else:
    print("Failed to place sandwich order. Box is currently disarmed.")

def setStatusLightOff():
  GPIO.output(LED, False)
  print("Status light is now off.")

def setStatusLightOn():
  GPIO.output(LED, True)
  print("Status light is now on.")
  
debounce = 200 # ms span to debounce switches
# GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.RISING, callback = arm, bouncetime = debounce)
# GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.FALLING, callback = disarm, bouncetime = debounce)
GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.BOTH, callback = toggle, bouncetime = 50)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback = order, bouncetime = debounce)

while True:
  # do whatever you want to do repeatedly
  # this is absolutley just a placeholder
  timestamp = time.time()
  formattedTimestamp = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
  print formattedTimestamp
  time.sleep(5)
