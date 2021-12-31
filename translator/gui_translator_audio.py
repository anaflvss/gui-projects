import googletrans as gtrans
import PySimpleGUI as sg

from utils import utils


languages_dict = {value.capitalize(): key for (key, value) in gtrans.LANGUAGES.items()}
languages = list(languages_dict.keys())

# GUI
## 1. Screen layout
sg.theme("Reddit")

# define column elements
col1 = [
    [
        sg.Combo(
            languages,
            key="-LANGUAGE_FROM-",
            size=(38, 1),
            default_value="English",
            background_color=sg.theme_background_color(),
        )
    ],
    [
        sg.Multiline(
            key="-INPUT-",
            size=(40, 10),
            # background_color=sg.theme_background_color(),
            border_width=0,
            no_scrollbar=True,
        )
    ],
    [
        sg.Button(
            "",
            key="-SOUND_FROM-",
            border_width=0,
            image_data=utils.button_sound_base64,
            button_color=sg.theme_element_background_color(),
            # visible=False,
        ),
    ],
]

col2 = [
    [
        sg.Combo(
            languages,
            key="-LANGUAGE_TO-",
            size=(38, 1),
            default_value="Portuguese",
            background_color=sg.theme_background_color(),
        )
    ],
    [
        sg.Multiline(
            key="-OUTPUT-",
            size=(40, 10),
            disabled=True,
            # background_color=sg.theme_background_color(),
            border_width=0,
            no_scrollbar=True,
        )
    ],
    [
        sg.Button(
            "",
            key="-SOUND_TO-",
            border_width=0,
            image_data=utils.button_sound_base64,
            button_color=sg.theme_element_background_color(),
            # visible=False,
        )
    ],
]


layout = [
    [
        sg.Column(col1, element_justification="c"),
        sg.Column(col2, element_justification="c"),
    ],
    [
        sg.Button(
            "Translate",
            key="-TRANSLATE-",
            size=(20, 0),
            visible=True,
            bind_return_key=True,
            border_width=0,
        )
    ],
]

## 2. Window
window = sg.Window("Translator", element_justification="c").layout(layout)


while True:

    event, values = window.Read()
    print(event)

    # Fixes passible typo in user's input
    translate_from = values["-LANGUAGE_FROM-"].capitalize()
    translate_to = values["-LANGUAGE_TO-"].capitalize()

    if event == None or event == sg.WIN_CLOSED:
        break

    if event == "-TRANSLATE-":

        # Empty inputs won't break the application
        if not values["-INPUT-"]:
            window["-OUTPUT-"].Update("")

        else:

            translator = gtrans.Translator()
            translation = translator.translate(
                values["-INPUT-"],
                src=languages_dict[translate_from],
                dest=languages_dict[translate_to],
            ).text

            window["-OUTPUT-"].Update(translation)

    # Generate audio if the user clicks on sound buttons
    if event == "-SOUND_FROM-":

        utils.listen(
            voice_lang=languages_dict[translate_from],
            speech_text=values["-INPUT-"],
            saved_file="sound_from.mp3",
        )

    if event == "-SOUND_TO-":
        utils.listen(
            voice_lang=languages_dict[translate_to],
            speech_text=values["-OUTPUT-"],
            saved_file="sound_to.mp3",
        )


window.close()
