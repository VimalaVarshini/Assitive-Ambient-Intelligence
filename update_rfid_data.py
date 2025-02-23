import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
def read_rfid():
reader = SimpleMFRC522()
try:
id, data = reader.read()
return id, data
except Exception as e:
return None, str(e)
finally:
GPIO.cleanup()
