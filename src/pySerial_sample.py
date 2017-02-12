# coding:utf-8
import os
from serial import Serial

def serial_tx():
    ser = Serial(
    port="COM8",
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=None,
    xonxoff=0,
    rtscts=0,
    writeTimeout=None,
#   dsrdtr=None
    )
    print "Tx: " + ser.portstr

    ser.write("hello pySerial\n")
    
    ser.close()
    
def serial_rx():
    ser = Serial("COM8") 
    print "Rx: " + ser.portstr
    
    s = ser.read(6)  
    print s
    
    ser.close()

    return s
    
def main():
    serial_tx()
    s = serial_rx()
    
main()
