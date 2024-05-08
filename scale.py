import time
import serial.tools.list_ports



#TinkerAssist video on importing arduino's serial monitor

ports = serial.tools.list_ports.comports()
serialInstance = serial.Serial()

portList = []
for port in ports:
    portList.append(str(port))
    print(str(port))

val = input("Select port: COM")

# go through each port detected
for port in portList:
    # if the player chooses a valid port, choose the first one and break
    if port.startswith("COM"+str(val)):
        portVar = "COM"+str(val)
        print(f"{portVar} selected")
        break

serialInstance.baudrate = 57600
serialInstance.port = portVar
serialInstance.open()

while True:
    if serialInstance.in_waiting:
        packet = serialInstance.readline()
        terminalLine = packet.decode("utf").rstrip("\n")
        print(terminalLine)