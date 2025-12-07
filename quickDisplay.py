from main import collectStatBuffs
import pyautogui as g
import keyboard as k
import math as m
import time as t
import os
statDic = collectStatBuffs()
s = " "

def endFunc():
    if k.is_pressed('p') or k.is_pressed('esc'):
        return True
while(True):
    statDic = collectStatBuffs()
    message = ''
    message += f"|             |             |             |             |             |             |\n"
    temp = ''
    for stat in statDic:
        # printing the stats
        L = 11 - (len(stat))+1
        L, R = m.ceil(L/2), m.ceil(L/2)
        if (L + len(stat)+1 + R) < 14:
            R += 1
        temp += f"{s*L}{stat}{s*R}|"
    message += f"|{temp}\n"
    
    temp = ''
    for stat in statDic:
        if statDic[stat]:
            statGroup = ''
            if len(statDic[stat]) > 1:
                for value in statDic[stat]:
                    # Printing the values collected
                    statGroup += f'{value['value']},'
            else:
                statGroup += f'{statDic[stat][0]['value']}'

            L = 11 - (len(statGroup))+1
            L, R = m.ceil(L/2), m.ceil(L/2)
            if (L + len(statGroup)+1 + R) < 14:
                R += 1
            temp += f"{s*L}{statGroup}{s*R}|"
        else:
            temp += '             |'

    message += f"|{temp}\n"

    message += f"|             |             |             |             |             |             |\n"

    print(message)
    t.sleep(0.5)
    os.system('cls')
    if endFunc():
        exit()









