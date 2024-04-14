import os
import RPi.GPIO as GPIO
from datetime import datetime
from time import sleep, time
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

# Sensor and pin configuration
sensor = Adafruit_DHT.DHT11
sensor_pin = 4

# Initialize camera
camera = PiCamera()

# Timing variables
last_photo_time = 0
photo_interval = 3600  # 1 hour in seconds
last_dht_read_time = 0
dht_read_interval = 300  # 5 minutes in seconds

while True:
    current_time = time()
    
    # Read from DHT11 sensor every 5 minutes
    if (current_time - last_dht_read_time) >= dht_read_interval:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading from DHT11. Try again!')
        last_dht_read_time = current_time

    # Capture and upload an image every hour
    if (current_time - last_photo_time) >= photo_interval:
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
        
        last_photo_time = current_time

    sleep(1)  # Sleep to reduce CPU usage

# Clean up resources
camera.close()
GPIO.cleanup()
