import subprocess
import random
import math
from math import sin
import wave

def synth_sine(f, r=44100, l=44100, a=1):
    return bytes(int(127.5 + a * 127.5 * sin(2 * math.pi * x * f / 44100)) for x in range(44100))

def synth_saw(f, r=44100, l=44100, a=1):
    return bytes(int(((f * 255 / r  * x) % 255) * a) for x in range(44100))

def synth_two_sine(f1, f2, r=44100, l=44100, a=1):
    return bytes(int(127.5 + a * 127.5 * sin(2 * math.pi * x * f1 / 44100)) // 2 + int(127.5 + a * 127.5 * sin(2 * math.pi * x * f2 / 44100)) // 2 for x in range(44100))



# ~~~ MAIN ~~~

with wave.open("test.wav", "w") as f:
    f.setparams((1, 1, 44100, 0, "NONE", 0))
    f.writeframes(synth_two_sine(440, 660, l=44100 * 5, a=0.25))
    f.writeframes(synth_sine(440, l=44100 * 5, a=0.25))

subprocess.run(["play", "test.wav"])