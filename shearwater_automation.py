from time import sleep
from turtle import delay
import pyautogui
import pyperclip

#open SW Cloud 
pyautogui.moveTo(982, 887, duration = 1)
pyautogui.click()

#open connection screen
pyautogui.moveTo(193, 45, duration = 1)
pyautogui.click()

#Connect to computer 
pyautogui.moveTo(360, 470, duration = 1)
pyautogui.click()

sleep(20)

#Go to advanced 
pyautogui.moveTo(305, 429, duration = 1)
pyautogui.click()

#Go to install FW file
pyautogui.moveTo(357, 290, duration = 1)
pyautogui.click()

#Click choose file
pyautogui.moveTo(1036, 500, duration = 1)
pyautogui.click()

#Go to file path bar
pyperclip.copy('C:\projects\DarkWater\Petrel_GEN2_v84_EN_0505.aes')
pyautogui.moveTo(508, 445, duration = 1)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
sleep(2)
pyautogui.hotkey('enter')

#Click proceed
pyautogui.moveTo(1050, 500, duration = 1)
pyautogui.click()
