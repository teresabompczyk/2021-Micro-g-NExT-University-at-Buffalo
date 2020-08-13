import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
servoPIN = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)
p.start(0)

def servo(sleep, cycle):
    p.ChangeDutyCycle(cycle)
    time.sleep(sleep)
    return


#print("servo Right")
servo(1, 3)
p.stop()
GPIO.cleanup()
