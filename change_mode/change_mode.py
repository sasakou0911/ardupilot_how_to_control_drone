"""
Mode change via mavlink  
by koichi sasaki
"""

print("drone kit mode change スタート")

#library import
from kbhit import *
from dronekit import connect
from dronekit import VehicleMode
import time

#kbhitを使う為のおまじない
atexit.register(set_normal_term)
set_curses_term()

#接続文字列の作成
connection_string = "/dev/ttyS0, 57600"

#フライトコントローラーへの接続
print("connect to FC: %s" % (connection_string))
vehicle = connect(connection_string, wait_ready = True)

#main loop
try:
    while True:
        if kbhit():
            key = getch() #一文字取得

            #keyの中身に応じた分岐
            if key == 's':
                mode = 'STABILIZE'
            
            elif key == 'a':
                mode = 'ALT_HOLD'

            elif key == 'p':
                mode = 'POSHOLD'
            
            elif key == 'l':
                mode = 'LOITER'
            
            elif key == 'g':
                mode = 'GUIDED'
                
            elif key == 't':
                mode = 'AUTO'
            
            elif key == 'r':
                mode = 'RTL'
            
            elif key == 'd':
                mode = 'LAND'
        
            vehicle.mode = VehicleMode(mode)

        print("----------------------------")
        print("Mode: %s" % vehicle.mode.name)

        time.sleep(1)

except( KeyboardInterrupt, SystemExit):
    print("interruptionを検知しました")
    
vehicle.close()

print("終了")

