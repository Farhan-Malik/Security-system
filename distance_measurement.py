import RPi.GPIO as GPIO
import time

def Distance(TRIG=23, ECHO=24):
    '''
    arguments:
    
    TRIG: pin at which ultrasonic sensor's trigger is connected, by default value is 23
    ECHO: pin at which ultrasonic sensor's echo is connected, by default value is 24
    '''
    GPIO.setmode(GPIO.BCM)
    
    # Initialization in case sensor won't work 
    start = time.time()
    end = time.time()
    
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.0002)

    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.000001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        end = time.time()

    sig_time = end - start

    distance = sig_time / 0.000058
    GPIO.cleanup((TRIG, ECHO))
    
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = Distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
