import picar_4wd as fc
import time

# Measured on my carpet
LEFT_MULTIPLIER = .96
RIGHT_MULTIPLIER = .86
FORWARD_MULTIPLIER = .036
BACKWARD_MULTIPLIER = .05

# Turn right 90 degrees
def turn_left():
    fc.turn_left(100)
    time.sleep(LEFT_MULTIPLIER)
    fc.stop()

# Turn left 90 degrees
def turn_right():
    fc.turn_right(100)
    time.sleep(RIGHT_MULTIPLIER)
    fc.stop()

def forward():
    fc.forward(100)
    time.sleep(FORWARD_MULTIPLIER)
    fc.stop()

def backward():
    fc.backward(100)
    time.sleep(BACKWARD_MULTIPLIER)
    fc.stop()
