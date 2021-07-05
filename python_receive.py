import serial

try:
    arduino = serial.Serial('COM6',9600,timeout=1)
except:
    print("check port")

rawdata=[]


rawdata.append(str(arduino.readline()))
line = arduino.readline().decode("utf-8")
myvar = line


print(str(myvar))

