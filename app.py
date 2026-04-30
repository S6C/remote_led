from flask import Flask, render_template, redirect, url_for, request
from gpiozero import LED, Button

app = Flask(__name__)

# Hardware Setup
led = LED(17)
button = Button(2)

# Handle physical button press in the background
button.when_pressed = led.toggle

def render_led():
    """Returns only the HTML fragment for the LED and status text."""
    return render_template('led_fragment.html', is_lit=led.is_lit)

@app.route('/')
def index():
    return render_template('index.html', is_lit=led.is_lit)

@app.route('/led_status')
def led_status():
    """Endpoint for HTMX polling."""
    return render_led()

@app.route('/toggle', methods=['POST'])
def toggle():
    led.toggle()
    # If it's an HTMX request, return just the fragment
    if request.headers.get('HX-Request'):
        return render_led()
    # Otherwise redirect (fallback for non-HTMX browsers)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
