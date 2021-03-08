
from win32gui import GetWindowText, GetForegroundWindow

old = ""
while True:
    new =GetWindowText(GetForegroundWindow())

    if old != new:

        # print(new)

        if new.lower().find("inkscape")>0:
            print("OK")

        old = new
