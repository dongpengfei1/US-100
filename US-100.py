import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout = 1)
#ser = serial.Serial('COM3', 9600)

def get_input():
    data = ser.read().hex()
    data2 = ser.read().hex()
    ser.flushInput()
    hdata = int(data,base=16)
    ldata = int(data2,base=16)
    distance = (hdata*256+ldata)/10
    return distance

def get_temp():
    temp = ser.read().hex()
    ser.flushInput()
    tdata = int(temp,base=16)
    ovtemp = tdata-45
    return ovtemp

try:
    while True:
        ser.write(chr(0x55).encode())
        time.sleep(0.005)
        print("%f CM" %(get_input()))
        ser.write(chr(0x50).encode())
        time.sleep(0.005)
        print("%f ℃" %(get_temp()))

except ValueError:
    print('获取信息超时')
    ser.flushInput()
    ser.flushOutput()
    ser.close()

except KeyboardInterrupt:
    print("按键终止")
    ser.flushInput()
    ser.flushOutput()
    ser.close()