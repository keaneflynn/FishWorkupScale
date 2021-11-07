import serial
import serial.tools.list_ports as portScan
import re

class ScaleGrab:   
    def __init__(self):
        ports = portScan.comports()
        for i in ports:
            store = i.device
        self.ser = serial.Serial(store)

    def readout(self):
        byteRead = self.ser.readline()
        weight_str = byteRead.decode("utf-8")
        weight_str = re.findall(r'\d+(?:[.,]\d+)?', weight_str)[0]
        weight_g = float(weight_str)

        return weight_g
        
