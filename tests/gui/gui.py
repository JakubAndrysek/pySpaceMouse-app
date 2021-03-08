import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("App Inkscape")],
          # [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Start'), sg.Button('Quit')]]

# Create the window
window = sg.Window('App-Inkscape', layout)

start = False

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == "Start":
        start = not start
        if start:
            window['Start'].update("Stop")
            window['-OUTPUT-'].update("App started")
            print("Start")
        else:
            window['Start'].update("Start")
            window['-OUTPUT-'].update("App stopped")
            print("Stop")

window.close()