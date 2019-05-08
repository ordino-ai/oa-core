# voice.py - Audio output: Text To Speech (TTS)

import platform
from io import BytesIO
import os
import pyttsx3
from oa.core import oa
from oa.modules.abilities.core import get, put
from playsound import playsound
from oa.WaveRNN import say

sys_os = platform.system()
flMac = (sys_os == 'Darwin')
if flMac:
    import subprocess
else:
    import pyttsx3




def _in():
    if not flMac:
        tts = pyttsx3.init()

    while not oa.core.finished.is_set():
        s = get()
        # Pause Ear (listening) while talking. Mute TTS.
        # TODO: move this somewhere else
        put('speech_recognition', 'mute')

        if flMac:
            _msg = subprocess.Popen(['echo', s], stdout=subprocess.PIPE)
            _tts = subprocess.Popen(['say'], stdin=_msg.stdout)
            _msg.stdout.close()
            _tts.communicate()
        else:
            say.say(s)
            # tempDir = tempfile.gettempdir()
            # filename = genFilename(s, '.mp3') 
            # filepath = os.path.join(tempDir, filename)
            # if not os.path.exists(filepath):
            #     try:
            #         tts = gTTS(s, 'en')
            #         with open(filepath, 'wb') as f:
            #             tts.write_to_fp(f)
            #         print(f"Video Download: {filename}")
            #     except:
            #         raise Exception('Failed to Download Video')
            # else:
            #     print("Video already in cache")

            # playsound(filepath)
            # print(f"Writing to {filepath}")
            # song = AudioSegment.from_file(filepath, format="mp3")
            # p.play()
            # play(song)
            #tts.say(s)
            #tts.runAndWait()

        # Wait until speaking ends.
        # Continue ear (listening). Unmute TTS.
        # TODO: move this somewhere else
        put('speech_recognition', 'unmute')
