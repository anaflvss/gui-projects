import os

# import googletrans as gtrans
from gtts import gTTS
from playsound import playsound

# Functions ---------------------
def listen(voice_lang: str, speech_text: str, saved_file: str):

    try:
        tts = gTTS(speech_text, lang=voice_lang)
        tts.save(saved_file)
        playsound(saved_file)
        os.system("del " + saved_file)
    except:
        pass


# Variables --------------------
button_sound_base64 = b"iVBORw0KGgoAAAANSUhEUgAAABkAAAARCAYAAAAougcOAAAC50lEQVR4nJ2VTWhcVRTHf//73swk4Fc6UyHTmdzJmzEJE6rIiCAi7hSLLgpdCX4UigiiZCPoQoVsCi6ky6JbcWMlKFJwpeJC1M7OgthkwrPTirYpftXJZOa94yJ5QZpMYvzDWbzfO5z/vefd8y78R0VRdLQ+VfuoVqvN7pGmuXK5eCt0+xWfmZwp1f30opL0C8Rx51w6Ktd7X9gI8x/WvX8b0L4mzWYzX5+aPpXkN76ReAM4hNHfa0FxHK/LkpdBJ+ren9k2abVauSy2TINGtfbY+s2/P5fjPUmRmY0sPFutlqOp2qvNw4dvA1i5fPniEDuG8Vzk/fMAinztewAnYdiiS9MLqdyPkoIdxY11C929nU7nUobmyuXiIJdfAjb6yfCpbrfbA4i8PynjdBq4+5yT5p00L2nezIoD53KAG7V6Sea9H6tUKuMAP1y9uqZc+CTGkXwQLGZ5E6XS+4ZuyOxFZ2ZkgZRKMmB0f3r0Q+nxQhB8HUXRFMDy8vIfOBYwXrinUjkC0G63B5KdU2pP73u6dmicwl3F4nngVw3T0xkemn2J9GcSBI9s79rct0jRgU3MTO12e2CwBPZAxjdPlq0ZTGYsMX4HwgObSLJWq5UTHAddyLj3fsykouDnjAXiTmAYHtSEXq//W5IcA+620J3KcCg9aqndHqTJVxkzpQ9idJwkssDMmZn417Tu0Ph4YWj2WT9JHup0Oj8BNBqNO0g5g3j3Urd7BaDVauXMdMLQB2FqdhE2p1DSWi5NB6lcuuucsPlN4jhez57nyuXiYDBcQlzZSJI3M37j+vVnHBxKA3c2nCgV789etNvtBFCjOv2EOXtL0sNbhUduzIKggPFJoXfz7Mq1az0A7/2cM94xsbC6uvrLyLY0m818/6/es8he3/617DLxt6perc6j4FNkH6/E8QLs1fstzUxOlpL82CtgLwETFrjZUSbe+7HAdF6y71bi+DX2GurdFEXR0bqvnfs/98k/vfIxkc8LugwAAAAASUVORK5CYII="
button_mic_base64 = b"iVBORw0KGgoAAAANSUhEUgAAAAoAAAARCAYAAADkIz3lAAAA60lEQVR4nH3SP0oDURDH8c/+wUIFG0XQwk6wEKysJLUHsLT3AJ7G3iIRa7t4ACvBag8QjRIQERRMlljsJK7rmh8MzJv5DvPmveFHm7jGJz7Qw4aGUnQxbdglkjq4ipcW8AnLkGMHexg320TsCEWOXXQWgB1MU5T/QHW4TGuBpAWax9I4jDFpASeRS1IMVJNdtYBdrGCQo8A7HnGOY9XT3OAV2yhmd1jCGdaiALbwhgt8NVut4xb98OfKG+AIz9F6tAiELMBfSsIOcYoD7EfuAfeqxbijWq+hvwsxs2EwMpzEACPVl5bh9yOXfQOjPUQV4ZFBrgAAAABJRU5ErkJggg=="
