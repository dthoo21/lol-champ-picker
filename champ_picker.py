import pyautogui
import sys
import time

select = False
screen_width, screen_height = pyautogui.size()

# pyautogui.click('search_text.png')

# print("Found search bar")

# pyautogui.write(sys.argv[1])
# print("Entered champion name")

# if screen_width == 1920 and screen_height == 1080:
#     pyautogui.move(-390, 64, duration=0.2)
#     pyautogui.click(duration=0.2)

# pyautogui.click('lock_in.png')

while (select == False):
    try:
        pyautogui.click('search_text.png')
        print("Found search bar")

        pyautogui.write(sys.argv[1])
        print("Entered champion name")

        if screen_width == 1920 and screen_height == 1080:
            pyautogui.move(-390, 64, duration=0.2)
            pyautogui.click(duration=0.2)

        pyautogui.click('lock_in.png')
        
        select = True

    except:
        print("Cannot not find elements. Sleep for 1 seconds.")
        time.sleep(1)
