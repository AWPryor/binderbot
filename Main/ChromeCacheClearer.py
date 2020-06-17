#This Script currently has a bug which requires you to be in full screen when you run it.

import pyautogui
import time

def Main():
    #Save the Current mouse Position.
    position = pyautogui.position()
    
    #Open a new Chrome Tab.
    OpenChrome()
    
    #Clear the Cookies and close the chrome tab.
    ClearCookiesCashe()
    
    #Return the mouse to it's original position.
    pyautogui.moveTo(position)

def OpenChrome():
    #Click on the Chrome Icon
    image = "Images/ChromeIcon.png"
    
    pyautogui.click(pyautogui.locateCenterOnScreen(image))
    
    #Wait for chrome to open.
    time.sleep(2)
    
    #Focus on Chrome tab's url bar.
    image2 = "Images/Marker.png"
    x = pyautogui.locateCenterOnScreen(image2)
    pyautogui.click(x[0]+100,x[1]+50)
    
def ClearCookiesCashe():
    #Go to the page to delete cache + cookies.
    pyautogui.typewrite('chrome://settings/clearBrowserData\n')
    
    #Wait for it to load.
    time.sleep(2)
    
    #Clear the cache + cookies.
    image = "Images/ClearDataIcon.png"
    pyautogui.click(pyautogui.locateCenterOnScreen(image))
    
    #Close Chrome.
    image = "Images/Marker2.png"
    pyautogui.click(pyautogui.locateCenterOnScreen(image))

Main()