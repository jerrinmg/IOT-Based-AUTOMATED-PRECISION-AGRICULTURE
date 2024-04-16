int sensorPin = A0;   // Input pin for the potentiometer (soil moisture sensor)
int relayPin = 13;    // Pin connected to the relay
int sensorValue = 0;  // Variable to store the value from the sensor
int moisturePercentage = 0;

void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Read the value from the sensor
  sensorValue = analogRead(sensorPin);
  float voltage = sensorValue * (5.00 / 1023.00);  // Convert sensor reading to voltage

  Serial.print("Voltage: ");
  Serial.print(voltage);
  Serial.print(" V, ");

  // Map voltage to percentage
  moisturePercentage = map(voltage, 5.00, 2.75, 0, 100);
  Serial.print("Moisture: ");
  Serial.print(moisturePercentage);
  Serial.println("%");

  // Control the relay based on moisture percentage
  if (moisturePercentage < 40) {
    digitalWrite(relayPin, HIGH);  // Turn on water pump
    digitalWrite(12, HIGH);
    delay(5000);  // Keep on for 5 seconds
    digitalWrite(12, LOW);
    delay(1000);  // Off for 1 second
  } else {
    digitalWrite(relayPin, LOW);  // Turn off water pump
    digitalWrite(12, LOW);
    delay(10000);  // Delay further readings to reduce wear
  }

  delay(20000);  // Delay between readings
}
