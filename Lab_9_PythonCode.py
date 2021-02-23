import serial
import guizero

import time

ser = serial.Serial('COM3', 9600)
ser.flush()
time.sleep(3)
Servo1_Pos = []
Servo2_Pos = []



def Sto_Position():

    Servo1_Pos.append(slider1.value)
    Servo2_Pos.append(slider2.value)



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


def slider2_read(slider_value):

    print(slider_value)
    ser.flush()
    ser.write(str('M2').encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    ser.flush()
    ser.write(str(slider_value).encode('utf-8'))
    ser.write(str("\n").encode('utf-8'))
    time.sleep(.2)



app = guizero.App()

slider1 = guizero.Slider(app, start=0, end=180, width="fill", command=slider_read)
slider2 = guizero.Slider(app, start=0, end=180, width="fill", command=slider2_read)
RecordButton = guizero.PushButton(app, text="Save", command=Sto_Position)
RepeatButton = guizero.PushButton(app, text="Repeat", command=Repeat_value)

app.display()

ser.close()



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
