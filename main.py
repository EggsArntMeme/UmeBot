from pyautogui import *
import pyautogui
import numpy as np
from PIL import Image, ImageOps
screenRatio = 1
# input()

def check_stat_placement(left): 
    match left:
        case n if 0*(screenRatio) <= n <= 119*(screenRatio):
            return "Speed"
        case n if 120*(screenRatio) <= n <= 239*(screenRatio):
            return "Stam"
        case n if 240*screenRatio <= n <= 359*screenRatio:
            return "Power"
        case n if 360*screenRatio <= n <= 479*screenRatio:
            return "Guts"
        case n if 480*screenRatio <= n <= 599*screenRatio:
            return "Wit"
        case n if 600*screenRatio <= n <= 750*screenRatio:
            return "Skill Pts"
           

statsCheck = pyautogui.screenshot("statsCheck.png", region=[round(350*screenRatio),round(900*screenRatio), round(750*screenRatio), round(35*screenRatio)])

statsCheck = statsCheck.convert('L')
statsCheck = ImageOps.colorize(statsCheck,[0, 0, 0], [255, 255, 255], blackpoint=100)
statsCheck.save('greysacale.png')




# while(input('enter:  3   to exit\n') != '3'):
#     bruhclick = pyautogui.position()
#     print(bruhclick)
#     print(pyautogui.pixel(bruhclick.x, bruhclick.y))

confidence_level = 0.8


found_stat_nums = {
    "Speed" : [],
    "Stam" : [],
    "Power" : [],
    "Guts" : [],
    "Wit" : [],
    "Skill Pts" : []
}
statsCheck = pyautogui.screenshot("statsCheck.png", region=[round(350*screenRatio),round(900*screenRatio), round(750*screenRatio), round(35*screenRatio)])

statsCheck = statsCheck.convert('L')
statsCheck = ImageOps.colorize(statsCheck,[0, 0, 0], [255, 255, 255], blackpoint=200)
statsCheck.save('greysacale.png')

for i in range(10): 
    img_path = f'refrence-imgs/numbers/{i}.png'
    img = Image.open(img_path)
    img = ImageOps.scale(img, screenRatio)
    img = img.convert('L')
    img = ImageOps.colorize(img,[0, 0, 0], [255, 255, 255], blackpoint=200)
    try:
        if pyautogui.locate(img, statsCheck, confidence=confidence_level):
            j = 0
            last_entry = {
                'left': 0,
                'top': 0,
                'value': None,
                'stat': ''
            }
            for location in pyautogui.locateAll(img, statsCheck, confidence=confidence_level):
                placement = check_stat_placement(location.left)
                if (location.left - last_entry['left']) > 1 and (placement != last_entry['stat']):
                    last_entry = {
                                            'id': j,
                                            'left': location.left,
                                            'top': location.top,
                                            'value': i,
                                            'stat': placement
                                }
                    found_stat_nums[placement].append(last_entry)
                    print(placement)
                else:
                    print("")
                    print("FAILED")
                    print(f"OWN: {location}")
                    print(placement)
                    print("")
                j += 1
                pass
    except ImageNotFoundException:
        # print(f"there is no instance of {i+1}.")
        pass
print(found_stat_nums)
print("")

for stat in found_stat_nums:
    message = f'The value(s) in {stat} is: '

    for number in found_stat_nums[stat]:

        match number['value']:

            case 0:
                message += f"{number['value']}"
            case 1:
                message += f" {number['value']}"
            case 2:
                message += f" {number['value']}"
            case 3:
                message += f" {number['value']}"
            case 4:
                message += f" {number['value']}"
            case 5:
                message += f" {number['value']}"
            case 6:
                message += f" {number['value']}"
            case 7:
                message += f" {number['value']}"
            case 8:
                message += f" {number['value']}"
            case 9:
                message += f" {number['value']}"
    if message != f'The value(s) in {stat} is: ':
        print(message + "\n")
    else:
        pass
    pass


# 'id': j,
# 'left': location.left,
# 'top': location.top,
# 'stat': placement

    # match len(found_stat_nums[i]): 
    #     case 1:
    #         print(f"there is 1 instance of the number {i}")
    #         print(f"its in the: {found_stat_nums[i][0]['stat']}")
    #         print("")
    #     case 2:
    #         print(f"there is 2 instance of the number {i}")
    #         for entry in found_stat_nums[i]:
    #             print(f"    Theres 1 in {entry['stat']}")
    #         print("")
    #     case _:
    #         pass
















 
# CHECKING LOCATIONS OF STATS
# for i in range(7):
#     bruhclick = pyautogui.moveTo(round(360*screenRatio+(130*screenRatio*i)), round(920*screenRatio))
#     bruhclick = pyautogui.position()
#     print(f"{i+1}:")
#     print(f"L> pos: x={370*screenRatio+(120*screenRatio*i)}, y={920*screenRatio}")
#     print(f"L> RGB: {pyautogui.pixel(bruhclick.x, bruhclick.y)}")
#     input()


# CHECKING LOCATION OF ENERGY
# for i in range(8):
#     bruhclick = pyautogui.moveTo(595+(40*i), 185)
#     bruhclick = pyautogui.position()
#     print(f"{i+1}/8th:")
#     print(f"L> pos: x={595+(40*i)}, y={185}")
#     print(f"L> RGB: {pyautogui.pixel(bruhclick.x, bruhclick.y)}")
#     input()

# pyautogui.moveTo(595+(40*1), 185)





# Support Position:

# Friendship Level:
# notes: Placement is the end of the middle bar, as as soon as blue is detected, you're almost green, and or if its grey, that means you're still likely only 1-2 bars full
# (first pos) x=1190 , y=320
# (second pos) x=1190 , y=450
# increments by 130px


# COLORS
# GREY (unfilled bar): RGB(105, 103, 115)
# Blue (1-3 bars): RGB(42, 192, 255)
# Green (3-4 bars): RGB(162, 230, 30)
# Orange (4-5 bars): RGB(255, 173, 30)
# MAX: RGB(255, 235, 120)


# ENERGY
# 1/8th:
# L> pos: x=595, y=185
# L> RGB: (49, 167, 255)

# 2/8th:
# L> pos: x=635, y=185
# L> RGB: (41, 216, 255)

# 3/8th:
# L> pos: x=675, y=185
# L> RGB: (33, 239, 198)

# 4/8th:
# L> pos: x=715, y=185
# L> RGB: (33, 243, 70)

# 5/8th:
# L> pos: x=755, y=185
# L> RGB: (141, 243, 0)

# 6/8th:
# L> pos: x=795, y=185
# L> RGB: (255, 227, 0)

# 7/8th:
# L> pos: x=835, y=185
# L> RGB: (255, 186, 16)

# 8/8th:
# L> pos: x=875, y=185
# L> RGB: (255, 118, 41)