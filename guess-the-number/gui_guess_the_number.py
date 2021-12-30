"""
'Guess the number!' with a GUI. 
"""
import re
import numpy as np
import PySimpleGUI as sg


def check_string(string: str):
    """Checks if the input string is a valid integer between 0 and 100."""
    if re.fullmatch("\d{1,3}", string):
        if 0 <= int(string) <= 100:
            return True
    return False


# GUI
## 1. Screen layout
sg.theme("Black")
layout = [
    [sg.Text("Guess the Number!", font=("Source Sans Pro", 14, "bold"))],
    [sg.Text("Enter an integer from 0 to 100:", font=("Source Sans Pro", 11))],
    [sg.Input(key="X", size=(12, 0), justification="center")],
    [sg.Button("Enter", key="ENTER", size=(10, 0), visible=True, bind_return_key=True)],
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

## 2. Window
window = sg.Window(
    "Guess the number", element_justification="c", resizable=True
).layout(layout)


## 3. Window's logic
random_int = np.random.randint(100)
print(random_int)

while True:

    event, values = window.Read()
    print(event, values)

    if event == None:
        break

    # Make sure the user's input will be valid integers. If not, the program
    # won't run.
    if not check_string(values["X"]):
        window["OUTPUT"].update("Only numbers between 0 and 100 are valid. :)")

    else:
        # If the input is valid, the conditions will adjust the guesses until the
        # user gets it right
        if int(values["X"]) < random_int:
            window["OUTPUT"].update("Too low! Try again.")

        elif int(values["X"]) > random_int:
            window["OUTPUT"].update("Too high! Try again.")

        else:
            window["OUTPUT"].update("That's correct! How did you know?")
            window["ENTER"].update(visible=False)

            # When the guess is right, the play again button shows up on the
            # screen.
            window["PLAY AGAIN"].update(visible=True)

            # If Play again is pressed, the rest of the screen should return to
            # initial layout.
            if event == "PLAY AGAIN":
                random_int = np.random.randint(100)
                print(random_int)

                window["OUTPUT"].update("")
                window["X"].update("")
                window["ENTER"].update(visible=True)
                window["PLAY AGAIN"].update(visible=False)

                continue


window.close()
