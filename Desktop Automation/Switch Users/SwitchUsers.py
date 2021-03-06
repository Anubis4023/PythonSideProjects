from pywinauto.application import Application
import mouse
import time


#Open the mouse settings application and connect to the window that opens
openMouse = Application(backend="uia").start('C:\Program Files (x86)\Glorious Model O Software\OemDrv.exe')
#openMouse.GloriousModelOSoftware.print_control_identifiers()

#GLORIOUS O MODEL
#Move mouse to profiles button
mouse.move(582, 737, True, 1)
#time.sleep(1)
mouse.click(button='left')
#Select my profile
mouse.move(582, 767, True, 0)
mouse.click(button='left')
#Apply changes
mouse.move(1380, 822, True, 1)
#time.sleep(1)
mouse.click(button='left')
#Wait for changes to be applied
#time.sleep(2)
#Close the window
mouse.move(1435, 227, True, 1)
#time.sleep(1)
mouse.click(button='left')

#Open discord
openDiscord = Application(backend="uia").start(r"C:\Users\pacow\AppData\Local\DiscordPTB\app-1.0.1013\DiscordPTB.exe")
#discord.window(best_match='Discord').print_control_identifiers()

#wait for Discord to finish loading page
time.sleep(5)

#DISCORD
#Open profiles list
mouse.move(109, 1007, True, 1)
mouse.click(button='left')
#Click on 'Switch Accounts'
mouse.move(175, 947, True, 1)
mouse.click(button='left')
#Let list of profiles load
#time.sleep(1)
#Switch account to my profile
mouse.move(1068, 503, True, 1)
mouse.click(button='left')
#Let my profile load for discord
time.sleep(2)

#Move mouse to switch mic settings
#Click on settings
mouse.move(314, 1012, True, 1)
mouse.click()
#Let settings load
#time.sleep(1)
#Click on 'Voice & Video'
mouse.move(477, 681, True, 1)
mouse.click()
#Open list of input devices
mouse.move(966, 184, True, 1)
mouse.click()
#Select XIBERIA
mouse.move(881, 469, True, 1)
mouse.click()
#Close settings window
mouse.move(1471, 109, True, 0)
mouse.click()
#Close the Discord window
mouse.move(1904, 12, True, 0)
mouse.click()


#Close Discord background process
app2 = Application(backend="uia").connect(path="explorer.exe")
sys_tray = app2.window(class_name="Shell_TrayWnd")
hidden_tray_button = sys_tray.child_window(title="Notification Chevron").wrapper_object()
hidden_tray_button.click()

notifyWindow = Application().connect(best_match="NotificationOverflow")

list_box = Application(backend="uia").connect(class_name="NotifyIconOverflowWindow")
list_box_win = list_box.window(class_name="NotifyIconOverflowWindow")

Discord = list_box_win.child_window(title="DiscordPtb")
if Discord.exists():
    Discord.wrapper_object().right_click_input()
    time.sleep(1)
    mouse.move(50, -15, False, 1)
    mouse.click()

#time.sleep(1)
#hidden_tray_button.click()
#time.sleep(3)
#print("Trying again")
#hidden_tray_button.click()
mouse.move(0, 60, False, 1)

Steam = list_box_win.child_window(title="Steam")
if Steam.exists():
    Steam.wrapper_object().right_click_input() #Open submenu
    time.sleep(1)
    mouse.move(-220, -15, False, 1) #Move to exit/close button, need to find coordinates through simple testing and mouse.get_position
    mouse.click() #Click on exit/close button
    #These next two lines are necessary if closing the background app closes the hidden icons submenu
    time.sleep(1)
    hidden_tray_button.click()

Overwolf = list_box_win.child_window(title="Overwolf")
if Overwolf.exists():
    Overwolf.wrapper_object().right_click_input() #Open submenu
    time.sleep(1)
    mouse.move(50, -25, False, 1) #Move to exit/close button, need to find coordinates through simple testing and mouse.get_position
    mouse.click() #Click on exit/close button
    #These next two lines are necessary if closing the background app closes the hidden icons submenu
    time.sleep(1)
    hidden_tray_button.click()
    
Curseforge = list_box_win.child_window(title="CurseForge")
if Curseforge.exists():
    Curseforge.wrapper_object().right_click_input() #Open submenu
    time.sleep(1)
    mouse.move(-100, -15, False, 1) #Move to exit/close button, need to find coordinates through simple testing and mouse.get_position
    mouse.click() #Click on exit/close button

#FORMAT to add more background processes to close
# time.sleep(1)
# hidden_tray_button.click()

# Name = list_box_win.child_window(title="NAME")
# if Name.exists():
#     Name.wrapper_object().right_click_input() #Open submenu
#     time.sleep(1)
#     mouse.move(50, -15, False, 0) #Move to exit/close button, need to find coordinates through simple testing and mouse.get_position
#     mouse.click() #Click on exit/close button


openChrome = Application(backend="uia").start('C:\Program Files\Google\Chrome\Application\chrome.exe')
#time.sleep(1)
mouse.move(1045, 485, True, 1)
mouse.click()

