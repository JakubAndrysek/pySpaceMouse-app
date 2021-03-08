import spacenavigator
import time
import pyautogui
from pynput.keyboard import Key, Controller
from win32gui import GetWindowText, GetForegroundWindow
import PySimpleGUI as sg

version = 1.0

# gui setup
layout = [[sg.Text(f"InkscapeNavigator - v{version}", size=(30,1))],
          [sg.Text("Connecting mouse...", size=(30,1), key="mouse")],
          # [sg.Input(key='-INPUT-')],
          # [sg.Text(key='mouse_state')],
          [sg.Text("To start press 'Start'",size=(30,1), key='mouse_state')],
          [sg.Text("X:0.0, Y:0.0, Z:0.0",size=(30,1), key='axis')],
          [sg.Button('Start'), sg.Button('Stop'), sg.Button('Quit'), sg.Text("By kubaandrysek.cz", justification="right")]]

window = sg.Window('InkscapeNavigator', layout, )
app_start = False

# spacenavigator setup
key = Controller()
success = spacenavigator.open()
state = spacenavigator.read()

# check mouse
if not success:
    sg.Popup('Navigator is not connected/working', keep_on_top=True)
    exit()


window.read(timeout=1)
# window['mouse'].update("Connected to: "+success.name)
window['mouse'].update(f"Connected to: {success.name}")
print("Name: "+success.name)

while True:
    event, values = window.read(timeout=30)

    if event == "Start":
        app_start = True
        window['mouse_state'].update("App started")
        print("Start")

    if event == "Stop" or state.buttons[1]:
        app_start = False
        window['mouse_state'].update("App stopped")
        print("Stop")

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if app_start:
        new = GetWindowText(GetForegroundWindow())

        if new.lower().find("inkscape") > 0:
            # if True:
            window['mouse_state'].update("Running")
            window['axis'].update("X:%1.1f, Y:%1.1f, Z:%1.1f" % (state.x, state.y, state.z))

            state = spacenavigator.read()
            print("X:%1.1f, Y:%1.1f, Z:%1.1f" % (state.x, state.y, state.z))

            if (state.x != 0 or state.y != 0 or state.z != 0):
                key.press(Key.ctrl)

                if state.x > 0.4:
                    key.press(Key.left)

                if state.x < -0.4:
                    key.press(Key.right)

                if state.y > 0.4:
                    key.press(Key.down)

                if state.y < -0.4:
                    key.press(Key.up)

                if state.z > 0.4:
                    pyautogui.scroll(20)
                    # print("down")

                if state.z < -0.4:
                    pyautogui.scroll(-20)

                key.release(Key.ctrl)

        else:
            window['mouse_state'].update("Paused - not Inkscape")

    time.sleep(0.01)

window.close()
