"""
Guess the number with a GUI. 
"""
import re
import numpy as np
import PySimpleGUI as sg


def string_checker(string: str):
    if re.fullmatch("\d{1,3}", string):
        if 0 <= int(string) <= 100:
            return True
        else:
            return False
    return False


sg.theme("DarkAmber")
layout = [
    [sg.Text("Guess the Number!", font=("Source Sans Pro", 14, "bold"))],
    [sg.Text("Enter an integer from 0 to 100:", font=("Source Sans Pro", 11))],
    [sg.Input(key="X", size=(12, 0), justification="center")],
    [sg.Button("Send", key="SEND", size=(10, 0), visible=True)],
    [
        sg.Text(
            size=(40, 1),
            key="OUTPUT",
            justification="center",
            font=("Source Sans Pro", 10),
        )
    ],
    [sg.Button("Play again", key="PLAY AGAIN", size=(10, 0), visible=False)],
]

window = sg.Window(
    "Guess the number", element_justification="c", resizable=True
).layout(layout)


random_int = np.random.randint(100)
print(random_int)

while True:

    event, values = window.Read()
    print(event, values)

    if event == None:
        break

    if not string_checker(values["X"]):
        window["OUTPUT"].update("""Only numbers between 0 and 100 are valid. :)""")

    else:
        if int(values["X"]) < random_int:
            window["OUTPUT"].update("Too low! Try again.")

        elif int(values["X"]) > random_int:
            window["OUTPUT"].update("Too high! Try again.")

        else:
            window["OUTPUT"].update("That's correct! How did you know?")
            window["SEND"].update(visible=False)
            window["PLAY AGAIN"].update(visible=True)

            if event == "PLAY AGAIN":
                random_int = np.random.randint(100)
                print(random_int)

                window["OUTPUT"].update("")
                window["X"].update("")
                window["SEND"].update(visible=True)
                window["PLAY AGAIN"].update(visible=False)

                continue

    #


window.close()
