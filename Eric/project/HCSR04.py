import RPi.GPIO as GPIO
import time


class Sensor:
    def __init__(self, TRIG_PIN = 23, ECHO_PIN = 24):
        GPIO.setmode(GPIO.BCM)

        self.TRIG = TRIG_PIN
        self.ECHO = ECHO_PIN

        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)

        GPIO.output(self.TRIG, False)
        time.sleep(2)

    def getDis(self):
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO)==0:
            pass
        pulse_start = time.time()

        while GPIO.input(self.ECHO)==1:
            pass
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150 #34300 = 2*d/t
        return int(distance)

    def __del__(self):
        GPIO.cleanup()
