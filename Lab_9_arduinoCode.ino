/*---------LAB09-------------------*/

#include <Servo.h>

Servo servo1,servo2;  // creating objects for both servo motors connected to the ardiuno

// Declaring both intial positions for the motors to start at

int pos1 = 0;
int pos2 = 0;


void setup() 
{
  Serial.begin(9600);
  servo1.attach(9);  // attaches the servo on pin 9 
  servo2.attach(10);  // attaches the servo on pin 10
}

/*This is the main loop for the code, it will check the serial to see if anything has been entered
then the program will execute one of the if statements. and contorl the correct motor */

void loop()
{
  if(Serial.available() >0)
  {
    String data = Serial.readStringUntil('\n');
    if (data == "M1") // Motor 1
    {
      String data = Serial.readStringUntil('\n');
      pos1 = data.toInt();   //The string information need to be converted to a int IOT for the servo to read it 
      servo1.write(pos1);   //writing the int angle value to the servo motor
    }
    if (data == "M2") // motor2
    {
      String data = Serial.readStringUntil('\n');
      pos1 = data.toInt();
      servo2.write(pos1);
    }
    
    
    Serial.flush(); //serial flush will clear the serial 
    delay(500);
    
    
  }
}
