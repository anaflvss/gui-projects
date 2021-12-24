"""
Guess the number with a GUI. 
"""

import numpy as np
import PySimpleGUI as sg


sg.theme("DarkAmber")
layout = [
    [sg.Text("Guess the Number!", font=("Source Sans Pro", 14, "bold"))],
    [sg.Text("Enter an integer from 0 to 100:", font=("Source Sans Pro", 11))],
    [sg.Input(key="x", size=(12, 0), justification="center")],
    [sg.Button("Send", key="send", size=(10, 0))],
    [
        sg.Text(
            size=(40, 1),
            key="OUTPUT",
            justification="center",
            font=("Source Sans Pro", 10),
        )
    ],
]

window = sg.Window("Guess the number", element_justification="c").layout(layout)


random_int = np.random.randint(100)
print(random_int)

while True:

    button, values = window.Read()
    window["send"].update("Send")
    window["OUTPUT"].update("")

    if int(values["x"]) < random_int:
        window["OUTPUT"].update("Too low! Try again.")

    elif int(values["x"]) > random_int:
        window["OUTPUT"].update("Too high! Try again.")

    else:
        window["OUTPUT"].update("That's correct! How did you know?")
        window["send"].update("Play again")
        random_int = np.random.randint(100)

        print(random_int)
        continue

    # window["x"].update("")


window.close()


# TODO: after play again, o app não espera par dizer se o valor é maior ou menor.
