import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins connected to the servo motors
left_leg_servo_pin = 17  # Change this to the actual GPIO pin number
right_leg_servo_pin = 18  # Change this to the actual GPIO pin number

# Set up the servo motors
GPIO.setup(left_leg_servo_pin, GPIO.OUT)
GPIO.setup(right_leg_servo_pin, GPIO.OUT)

# Create PWM instances for the servo motors
left_leg_servo = GPIO.PWM(left_leg_servo_pin, 50)  # 50 Hz frequency
right_leg_servo = GPIO.PWM(right_leg_servo_pin, 50)  # 50 Hz frequency

# Start PWM for both servo motors
left_leg_servo.start(0)  # 0% duty cycle
right_leg_servo.start(0)  # 0% duty cycle

# Function to move the robot's legs
def move_legs(left_angle, right_angle):
    left_duty_cycle = (left_angle / 18) + 2
    right_duty_cycle = (right_angle / 18) + 2

    left_leg_servo.ChangeDutyCycle(left_duty_cycle)
    right_leg_servo.ChangeDutyCycle(right_duty_cycle)

# Move the robot's legs
try:
    while True:
        # Move the left leg forward and the right leg backward
        move_legs(90, 0)
        time.sleep(1)
        
        # Move the right leg forward and the left leg backward
        move_legs(0, 90)
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up GPIO
left_leg_servo.stop()
right_leg_servo.stop()
GPIO.cleanup()
