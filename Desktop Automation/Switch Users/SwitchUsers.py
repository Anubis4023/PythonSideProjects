from pywinauto.application import Application
import mouse
import time


#Open the mouse settings application and connect to the window that opens
openMouse = Application(backend="uia").start('C:\Program Files (x86)\Glorious Model O Software\OemDrv.exe')#.connect(title='Glorious Model O Software', timeout=3)
#openMouse.GloriousModelOSoftware.print_control_identifiers()

#GLORIOUS O MODEL
#Move mouse to profiles button
mouse.move(582, 737, True, 0)
time.sleep(1)
mouse.click(button='left')
#Select my profile
mouse.move(582, 767, True, 0)
mouse.click(button='left')
#Apply changes
mouse.move(1380, 822, True, 0)
time.sleep(1)
mouse.click(button='left')
#Close the window
mouse.move(1430, 227, True, 0)
time.sleep(1)
mouse.click(button='left')

#Open discord and connect to the window that opens
app = Application(backend="uia").start(r"C:\Users\pacow\AppData\Local\DiscordPTB\app-1.0.1013\DiscordPTB.exe")#.connect(title = 'Discord', timeout=10)
#discord.window(best_match='Discord').print_control_identifiers()

#DISCORD
#Open profiles list
mouse.move(109, 1007, True, 0)
mouse.click(button='left')
#Click on 'Switch Accounts'
mouse.move(175, 947, True, 0)
mouse.click(button='left')
#Let list of profiles load
time.sleep(1)
#Switch account to my profile
mouse.move(1068, 503, True, 0)
mouse.click(button='left')
#Let my profile load for discord
time.sleep(2)

#Move mouse to switch mic settings
#Click on settings
mouse.move(314, 1012, True, 0)
mouse.click()
#Let settings load
time.sleep(1)
#Click on 'Voice & Video'
mouse.move(477, 681, True, 0)
mouse.click()
#Open list of input devices
mouse.move(966, 184, True, 0)
mouse.click()
#Select XIBERIA
mouse.move(857, 368, True, 0)
mouse.click()

#TODO: #3 Close the settings window before closing Discord

#Close the Discord window
mouse.move(1904, 12, True, 0)
mouse.click(button='left')