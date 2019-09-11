// rangefinder using the HC-SR04 ultrasonic sensor

// the ultrasonic sensors pins
const int trigger = 12; // sends a ping
const int echo = 11; // reads the ping


void setup() {
  pinMode(trigger, OUTPUT); // set the trigger as output
  pinMode(echo, INPUT); // set the reader as input
  Serial.begin(9600);
}

void loop() {

  long duration, cm; // used to calculate distance

  // send a ping
  digitalWrite(trigger, LOW); // pull it low for a clean ping
  delayMicroseconds(2);
  digitalWrite(trigger, HIGH); // send the ping
  delayMicroseconds(5);
  digitalWrite(trigger, LOW); // pull it low again

  // store the time it takes for the ping to return
  duration = pulseIn(echo, HIGH);
  // convert the time it takes into centimeters
  cm = microsecondsToCentimeters(duration);

  Serial.println(cm);
  delay(250);
}


long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance traveled.
  return microseconds /29 / 2;
}
