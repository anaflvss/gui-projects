import os

# from sys import platform

from gtts import gTTS
from playsound import playsound


# Variables --------------------
button_sound_base64 = b"iVBORw0KGgoAAAANSUhEUgAAABkAAAARCAYAAAAougcOAAAC50lEQVR4nJ2VTWhcVRTHf//73swk4Fc6UyHTmdzJmzEJE6rIiCAi7hSLLgpdCX4UigiiZCPoQoVsCi6ky6JbcWMlKFJwpeJC1M7OgthkwrPTirYpftXJZOa94yJ5QZpMYvzDWbzfO5z/vefd8y78R0VRdLQ+VfuoVqvN7pGmuXK5eCt0+xWfmZwp1f30opL0C8Rx51w6Ktd7X9gI8x/WvX8b0L4mzWYzX5+aPpXkN76ReAM4hNHfa0FxHK/LkpdBJ+ren9k2abVauSy2TINGtfbY+s2/P5fjPUmRmY0sPFutlqOp2qvNw4dvA1i5fPniEDuG8Vzk/fMAinztewAnYdiiS9MLqdyPkoIdxY11C929nU7nUobmyuXiIJdfAjb6yfCpbrfbA4i8PynjdBq4+5yT5p00L2nezIoD53KAG7V6Sea9H6tUKuMAP1y9uqZc+CTGkXwQLGZ5E6XS+4ZuyOxFZ2ZkgZRKMmB0f3r0Q+nxQhB8HUXRFMDy8vIfOBYwXrinUjkC0G63B5KdU2pP73u6dmicwl3F4nngVw3T0xkemn2J9GcSBI9s79rct0jRgU3MTO12e2CwBPZAxjdPlq0ZTGYsMX4HwgObSLJWq5UTHAddyLj3fsykouDnjAXiTmAYHtSEXq//W5IcA+620J3KcCg9aqndHqTJVxkzpQ9idJwkssDMmZn417Tu0Ph4YWj2WT9JHup0Oj8BNBqNO0g5g3j3Urd7BaDVauXMdMLQB2FqdhE2p1DSWi5NB6lcuuucsPlN4jhez57nyuXiYDBcQlzZSJI3M37j+vVnHBxKA3c2nCgV789etNvtBFCjOv2EOXtL0sNbhUduzIKggPFJoXfz7Mq1az0A7/2cM94xsbC6uvrLyLY0m818/6/es8he3/617DLxt6perc6j4FNkH6/E8QLs1fstzUxOlpL82CtgLwETFrjZUSbe+7HAdF6y71bi+DX2GurdFEXR0bqvnfs/98k/vfIxkc8LugwAAAAASUVORK5CYII="

button_mic_base64 = b"iVBORw0KGgoAAAANSUhEUgAAAA0AAAAUCAYAAABWMrcvAAABKUlEQVR4nJXTu0pDQRAG4C+HBK9FiBiwVQQrO98ghULApxAVtPIxrEV9Bx9AsIidha2IFgraeCkEURMj8VLsHjgJ5xD8Ydidnf/fndmdpR/TOMAzvvGEPUwpwCRO8ZtjJxjPE60WCFJbSYlJZqwXpRBRT/kJqthFZYioEnnVBGXMZk4tQhJ55ZTYGyJI0UvV/0aCUpz/DOGm8VKCDkZwia8CwSeuMIpOgndcYx4beBsQvGINC1H4nqZWwyGOcYEl4V0ecY5FLGMdL6XMjhPYxBwe0BZaZwY32MdHUcFj2BZaZyv6fci78g7u4vw++kNFhG+RHftQHthgTmiVRlxrCF1wK9TV95ZNnAnF532Ldow3s6KjAvKgHWVFU9hBS7jubkylG/1WjNfgD3UkVgNGWAwMAAAAAElFTkSuQmCC"


# Functions ---------------------
def listen(voice_lang: str, speech_text: str, saved_file: str):
    """Creates and executes a audio file for a text-to-speech situation.

    Args:
    voice_lang: str
        the language from the input text

    speech_text: str
        the text to be converted in audio

    saved_file: str
        a temporary mp3 file that will be executed."""

    try:
        tts = gTTS(speech_text, lang=voice_lang)
        tts.save(saved_file)
        playsound(saved_file)

        os.system("del " + saved_file)

        # if platform == "win32":
        #     os.system("del " + saved_file)
        # if platform == "linux":
        #     os.system("rm " + saved_file)

    # If the chosen language is not available in audio:
    except:
        pass
