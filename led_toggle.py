from gpiozero import LED, Button
from signal import pause

# Setup the LED on GPIO 17 and Button on GPIO 2
led = LED(17)
button = Button(2)

# When the button is pressed, toggle the LED state
button.when_pressed = led.toggle

print("Program running. Press the button to toggle the LED. Press Ctrl+C to exit.")

# Keep the program running
pause()
