import pyaudio
import wave
import sys


#
# http://people.csail.mit.edu/hubert/pyaudio/
#
def play_wav(wavfile):
    CHUNK = 1024
    wf = wave.open(wavfile, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)
    
    stream.stop_stream()
    stream.close()
    p.terminate()


def nextpow2(targetnum):
    num = 1
    while num < targetnum:
        num = num * 2
    return num