import wiringpi
import time
import sys
from wiringpi import GPIO

wiringpi.wiringPiSetup()
wiringpi.pinMode(2, GPIO.OUTPUT)


while True:
    try:
        wiringpi.digitalWrite(2, GPIO.HIGH)
        time.sleep(0.3)
        wiringpi.digitalWrite(2, GPIO.LOW)
        time.sleep(0.3)
    except KeyboardInterrupt:
        print("\nexit")
        sys.exit(0)
