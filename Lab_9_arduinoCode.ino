#include <Servo.h>

Servo servo1,servo2;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos1 = 0;
int pos2 = 0;
int pyint;
String pypos;

void setup() 
{
  Serial.begin(9600);
  servo1.attach(9);
  servo2.attach(10);// attaches the servo on pin 9 to the servo object
}

void loop()
{
  if(Serial.available() >0)
  {
    String data = Serial.readStringUntil('\n');
    if (data == "M1")
    {
      String data = Serial.readStringUntil('\n');
      pos1 = data.toInt();
      servo1.write(pos1);
    }
    if (data == "M2")
    {
      String data = Serial.readStringUntil('\n');
      pos1 = data.toInt();
      servo2.write(pos1);
    }
    
    
    Serial.flush();
    delay(500);
    
    
  }
}
