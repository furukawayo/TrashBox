from machine import Pin, time_pulse_us, PWM
import utime

led = Pin(25, Pin.OUT)

SERVO_PIN = 0
PWM_FREQ = 50

def pulse_width(val, freq=PWM_FREQ, resol=65535):
    pulse = freq * val * 1e-6 * resol
    return int(pulse)

servo = PWM(Pin(SERVO_PIN))
servo.freq(PWM_FREQ)


TEMP = 20

TRIG_PIN = 15
ECHO_PIN = 14

s_speed = 331.5+0.6*TEMP

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

trig.value(0)
utime.sleep(1)

def measure():
    trig.value(1)
    utime.sleep_us(20)
    trig.value(0)
    
    while (echo.value()==0):
        sigoff = utime.ticks_us()
    while (echo.value()==1):
        sigon = utime.ticks_us()
    dist=(sigon-sigoff)*sspeed/2*(10**-4)
    return dist

while True:
    distance = measure()
    if	distance > 20:
        duty = pulse_width(500)
        servo.duty_u16(duty)
        print("Discance:{:.1f}cm".format(distance))
        utime.sleep(1)
    
    else:
        duty = pulse_width(2500)
        servo.duty_u16(duty)
        utime.sleep(1)













