#!/usr/bin/env python3

from pystyle import *
import os
import time
import keyboard as kb
from datetime import datetime
currentDateAndTime = datetime.now()

os.system('cls')
print(Center.XCenter(""" __      __   _                       _                   _        ____  _                 \n \ \    / /  | |                     | |       /\        | |      |  _ \| |                \n  \ \  / /_ _| | ___  _ __ __ _ _ __ | |_     /  \  _   _| |_ ___ | |_) | |__   ___  _ __  \n   \ \/ / _` | |/ _ \| '__/ _` | '_ \| __|   / /\ \| | | | __/ _ \|  _ <| '_ \ / _ \| '_ \ \n    \  / (_| | | (_) | | | (_| | | | | |_   / ____ \ |_| | || (_) | |_) | | | | (_) | |_) |\n     \/ \__,_|_|\___/|_|  \__,_|_| |_|\__| /_/    \_\__,_|\__\___/|____/|_| |_|\___/| .__/ \n                                                                                    | |    \n                                                                                    |_|    """))
print(Center.XCenter("""\nDeveloped by Atsuyo"""))
currentTime = currentDateAndTime.strftime("%H:%M:%S")
print(Colors.blue + "[" + currentTime + "]" + Colors.white + " Status : undetected")
status: bool = True

def change_status():
    global status
    status = not status

def bhop() -> None:
    global status
    while True:
        time.sleep(0.02)
        if kb.is_pressed("space"):
            kb.press_and_release("space")
            i = 120
            i+1

if __name__ == "__main__":
    kb.add_hotkey("f3", change_status)
    bhop()