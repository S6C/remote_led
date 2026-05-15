# Remote LED Controller

A Raspberry Pi web interface for controlling an LED via GPIO, built with Flask and HTMX.

## Features

- Toggle an LED from a browser with instant UI feedback
- Physical button support — pressing the hardware button also toggles the LED
- Live status polling every 2 seconds via HTMX (no page refresh needed)
- Graceful fallback for non-HTMX browsers

## Hardware

| Component | GPIO Pin |
|-----------|----------|
| LED       | GPIO 17  |
| Button    | GPIO 2   |

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask gpiozero
```

## Run

```bash
python app.py
```

The app listens on `0.0.0.0:5000` — open `http://<pi-ip>:5000` from any device on the network.

## Project Structure

```
app.py                  # Flask app — routes and GPIO setup
led_toggle.py           # Standalone script for button-only control (no web server)
templates/
  index.html            # Page shell
  led_fragment.html     # HTMX-swapped LED indicator and status
static/
  style.css             # Stylesheet
```
