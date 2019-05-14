"""
Simple script for communicaite with PX4 
by koichi sasaki
"""

print("dronekit start now")

from dronekit import connect
import time

connection_string = "/dev/ttyS0, 57600"

print("connect to FC: %s" % (connection_string))

vehicle = connect(connection_string, wait_ready = True)

try:
    while True:
        while True:
        print("-----------------------------")
        print("Connected now")
        print("Attitude: %s" % vehicle.attitude)
        print("velocity: %s" % vehicle.velocity)
        print("-----------------------------")
        
        time.sleep(1)

except( KeyboardInterrupt, SystemExit):
    print("Detect the interruption")
    
vehicle.close()

print("Compleated")

