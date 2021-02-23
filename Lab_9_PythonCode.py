import serial #importing serial. will allow us ot write to the serial monitor in the ardiuno
import guizero #guizero will all us to create a gui

import time   #importing time will allow us use all the functions for time

ser = serial.Serial('COM3', 9600) #this will communicates with the serial on com3 using 9600 baudrate
ser.flush()                        #this flushes the serial monitor
time.sleep(3)                      #this gives the ardino time to establish communication
Servo1_Pos = []                    #this array is for the stored positions of the first motor
Servo2_Pos = []                    #this array is for the stored positions of the Second motor 


#This function will store the postions of both motors when the button is pressed
def Sto_Position(): 

    Servo1_Pos.append(slider1.value)
    Servo2_Pos.append(slider2.value)


#This function will recall all the positions of the motor using the serial library write functions in a for loop to run the length of the array
def Repeat_value():

    for i in range(0,len(Servo1_Pos)):

        ser.write(str('M1').encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()
        ser.write(str(Servo1_Pos[i]).encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()

        ser.write(str('M2').encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()
        ser.write(str(Servo2_Pos[i]).encode('utf-8'))
        ser.write(str("\n").encode('utf-8'))
        ser.flush()



#This function will take all the silder values for the slider1 and contorl motor 1
def slider_read(slider_value):

    a = slider_value
    print(slider_value)
    ser.flush()
    ser.write(str('M1').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()
    ser.write(str(slider_value).encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    time.sleep(.2)
    return a

#this function will take all the slider values for the second slider and control motor 2
def slider2_read(slider_value):

    print(slider_value)
    ser.flush()
    ser.write(str('M2').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()
    ser.write(str(slider_value).encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    time.sleep(.2)


#These lines of code will create the GUI using GUizero and set the perameters for all of the interfaces. 
#Each slider and button will have a specific command it will call everything it is used
app = guizero.App()

slider1 = guizero.Slider(app, start=0, end=180, width="fill", command=slider_read)
slider2 = guizero.Slider(app, start=0, end=180, width="fill", command=slider2_read)
RecordButton = guizero.PushButton(app, text="Save", command=Sto_Position)
RepeatButton = guizero.PushButton(app, text="Repeat", command=Repeat_value)

app.display()

ser.close()


#####------------THIS IS TEST CODE DEVELOPED FOR A LED---------------##########


# def led_on_off():
#     user_input = input("\n type on / off / blink / quit : ")
#
#     if user_input == "on":
#         print("LED is on ...")
#         time.sleep(0.1)
#         ser.write(b'H')
#         led_on_off()
#     elif user_input == "off":
#         print("LED is off ...")
#         time.sleep(0.1)
#         ser.write(b'L')
#         led_on_off()
#     elif user_input == "blink":
#         print("LED is blinking ...")
#         for i in range(10):
#             ser.write(b'H')
#             time.sleep(0.5)
#             ser.write(b'L')
#             time.sleep(0.5)
#         led_on_off()
#     elif user_input == "quit" or user_input == "q":
#         print("Program exiting")
#         time.sleep(0.1)
#         ser.write(b'L')
#         led_on_off()
#
#
# time.sleep(2)
#
# led_on_off()
