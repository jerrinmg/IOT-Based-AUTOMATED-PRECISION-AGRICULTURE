

int sp = A0;   // select the input pin for the potentiometer
int dp =13; 
     // select the pin for the LED
int sv = 0;  // variable to store the value coming from the sensor
int a=0,p=0;
void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(dp, OUTPUT);
  pinMode(12,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:
  sv = analogRead(sp);
  float v = sv * (5.00/ 1023.00);
  //a=(sv*5)/1023;
 //v=5.00-v;
  Serial.print(v);
  //p=(v/5)*100;
  p=map(v,5.00,2.75,0,100);
  //Serial.print("percentage="+p+" ");
  Serial.println(p);
 //Serial.write(p);
   //turn the ledPin on
  if(p<40.00)
   {
       digitalWrite(dp, HIGH);
       digitalWrite(12,HIGH);
       delay(5000);
  // stop the program for <sensorValue> milliseconds:
      digitalWrite(12,LOW);
         delay(1000);
        /* digitalWrite(12,HIGH);
          delay(1000);
         digitalWrite(12,LOW);*/
   }
  else%
  {
  digitalWrite(dp, LOW);
  digitalWrite(12,LOW);
  delay(10000);
  // stop the program for for <sensorValue> milliseconds:
  }
 delay(20000);
  
}
