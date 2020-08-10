import pyautogui
import sys
import time

select = False
screen_width, screen_height = pyautogui.size() # Measure screen size for multiple screen resolution support

print("#############################\n# Daniel's LoL Champ Picker #\n#############################\n")

while (select == False): # Repeat while operation has failed
    try:
        pyautogui.click('search_text.png') # Find and select the search bar
        print("Found search bar")

        pyautogui.write(sys.argv[1]) # Write the argument
        print("Entered champion name")

        if screen_width == 1920 and screen_height == 1080: # For 1080p screen
            pyautogui.move(-390, 64, duration=0.2) # Move from search bar to champion icon
            pyautogui.click(duration=0.2) # Select champion icon
            print("Selected champion icon")

        # 720p support to be added

        pyautogui.click('lock_in.png') # Find and select lock in button
        print("Locked in")
        
        select = True # Cease loop. Operation has succeeded

    except:
        print("Cannot not find elements. Sleep for 1 seconds.")
        time.sleep(1) # Limit loop speed
