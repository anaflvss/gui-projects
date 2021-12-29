import os

import googletrans as gtrans
import PySimpleGUI as sg
from gtts import gTTS
from playsound import playsound


languages_dict = {value.capitalize(): key for (key, value) in gtrans.LANGUAGES.items()}
languages = list(languages_dict.keys())


def listen(voice_lang: str, speech_text: str, saved_file: str):
    tts = gTTS(speech_text, lang=voice_lang)
    tts.save(saved_file)
    playsound(saved_file)
    os.system("del " + saved_file)


# GUI
## 1. Screen layout
sg.theme("Reddit")
layout = [
    [
        sg.Text("From", size=(4, 1), font=("Source Sans Pro", 12)),
        sg.Combo(languages, key="-LANGUAGE_FROM-", size=(33, 1)),
        sg.Text("To", size=(2, 1), font=("Source Sans Pro", 12)),
        sg.Combo(languages, key="-LANGUAGE_TO-", size=(35, 1)),
    ],
    [
        sg.Multiline(key="-INPUT-", size=(40, 10)),
        sg.Multiline(key="-OUTPUT-", size=(40, 10), disabled=True),
    ],
    [
        sg.Button("Sound", key="-SOUND_FROM-"),
        sg.Button("Sound", key="-SOUND_TO-"),
    ],
    [
        sg.Button(
            "Translate", key="ENTER", size=(10, 0), visible=True, bind_return_key=True
        )
    ],
]

## 2. Window
window = sg.Window("Translator").layout(layout)


while True:

    event, values = window.Read()
    print(event, values)

    translate_from = values["-LANGUAGE_FROM-"]
    translate_to = values["-LANGUAGE_TO-"]

    if event == None:
        break

    if event == "ENTER":

        translator = gtrans.Translator()
        translation = translator.translate(
            values["-INPUT-"],
            src=languages_dict[translate_from],
            dest=languages_dict[translate_to],
        ).text

        window["-OUTPUT-"].Update(translation)

        # window["-SOUND_FROM-"].Update(visible=True)
        # window["-SOUND_TO-"].Update(visible=True)

    if event == "-SOUND_FROM-":

        listen(
            voice_lang=languages_dict[translate_from],
            speech_text=values["-INPUT-"],
            saved_file="sound_from.mp3",
        )

    if event == "-SOUND_TO-":
        listen(
            voice_lang=languages_dict[translate_to],
            speech_text=values["-OUTPUT-"],
            saved_file="sound_to.mp3",
        )

window.close()


## TODO (and other comments):
# 1. when there's no user input, the app crashes. Fix that!
# 2. Improve layout, specially the sound buttons and style
# 3. This app only works for windows
# 4. Make sure gtts has all the languages from gtrans. Otherwise, address the
#  exception
# 5. there's a tiny delay from the events print and the update of user's input
