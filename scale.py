import time
import serial.tools.list_ports

#TinkerAssist video on importing arduino's serial monitor
# used as a basis

# debug variable for prints
DEBUG = True

class Scale:
    def __init__(self) -> None:
        self.ports = serial.tools.list_ports.comports()
        self.serialInstance = serial.Serial()
        self.find_ports()

    def find_ports(self):
        portList = []
        for port in self.ports:
            portList.append(str(port))
            print(str(port))

        # by default, the port number will be 3
        val = 3
        # allow user change if it's in debug mode
        if DEBUG:
            val = input("Select port: COM")

        # go through each port detected
        for port in portList:
            # if the player chooses a valid port, choose the first one and break
            if port.startswith("COM"+str(val)):
                portVar = "COM"+str(val)
                print(f"{portVar} selected")
                break

        self.serialInstance.baudrate = 57600
        self.serialInstance.port = portVar
        self.serialInstance.open()

    def get_mass(self):
        while True:
            if self.serialInstance.in_waiting:
                packet = self.serialInstance.readline()
                terminalLine = packet.decode("utf").rstrip("\n")
                print(terminalLine)
                if DEBUG:
                    temp = terminalLine.find("one reading:")
                    print(f"         {temp}")
                if terminalLine.find("one reading:")>=0:
                    mass = terminalLine.rsplit("average:")[-1].strip()
                    if DEBUG:
                        print(f"mass={mass}")
                    return mass

'''
Test main
'''
if DEBUG:
    scale = Scale()
    while True:
        print(scale.get_mass())