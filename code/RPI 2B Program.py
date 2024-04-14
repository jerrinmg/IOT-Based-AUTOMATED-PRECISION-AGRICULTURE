import os
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep
from picamera import PiCamera
import pyrebase
import Adafruit_DHT

# Firebase configuration
firebaseConfig = {
    'apiKey': "XXXXX",
    'authDomain': "XXXXX",
    'databaseURL': "XXXXX",
    'projectId': "XXXXX",
    'storageBucket': "XXXXX",
    'messagingSenderId': "XXXXX",
    'appId': "XXXXX",
    'measurementId': "XXXXX"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

# GPIO setup for the button
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Sensor and pin configuration
sensor = Adafruit_DHT.DHT11
sensor_pin = 4

# Initialize camera
camera = PiCamera()

while True:
    # Read from DHT11 sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading from DHT11. Try again!')

    # Check if button is pressed
    if GPIO.input(10) == GPIO.HIGH:
        print("Button pushed")
        now = datetime.now()
        timestamp = now.strftime("%d%m%Y%H:%M:%S")
        filename = timestamp + ".jpg"
        
        # Capture image
        camera.capture(filename)
        print(filename + " saved")
        
        # Try to upload the image to Firebase
        try:
            storage.child(filename).put(filename)
            print("Image uploaded to Firebase")
            os.remove(filename)  # Remove the file locally after upload
            print("Local file removed")
        except Exception as firebase_error:
            print("Firebase upload error:", str(firebase_error))

        sleep(2)  # Sleep for 2 seconds to debounce the button

# Clean up resources
camera.close()
GPIO.cleanup()
