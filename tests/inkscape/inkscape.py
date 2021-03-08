import spacenavigator
import time
import pyautogui
from pynput.keyboard import Key, Controller

SpaceMouse_Pro = {'off': 14, 'move': 5}
SpaceNavigator = {'off': 1}

key = Controller()  # Create the controller
success = spacenavigator.open()
state = spacenavigator.read()
print("start")

if success:

    print(success.name)
    if (success.name == "SpaceMouse Pro" or success.name == "SpaceMouse Pro Wireless"):
        setup = SpaceMouse_Pro
    elif (success.name == "SpaceNavigator"):
        setup = SpaceNavigator
    else:
        setup = {'off': 0}

    while not state.buttons[setup['off']]:
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

        time.sleep(0.05)
