import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TOGGLE_SWITCH = 23
BUTTON = 24
LED = 25

isArmed = False

GPIO.setup(TOGGLE_SWITCH, GPIO.IN)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def arm():
  isArmed = True
  print("Box is now armed.")

def disarm():
  isArmed = False
  print("Box is now disarmed.")

def order():
  print("Order button was pressed.")
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

debounce = 300 # ms span to debounce switches

GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.RISING, callback = arm, bouncetime = debounce)
GPIO.add_event_detect(TOGGLE_SWITCH, GPIO.FALLING, callback = disarm, bouncetime = debounce)
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback = order, bouncetime = debounce)

while True:
  # do whatever you want to do repeatedly
  if isArmed:
    print("Box is currently armed.")
  else:
    print("Box is currently disarmed.")
