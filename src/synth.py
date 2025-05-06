import subprocess
import random
from math import sin
import wave

def play_chord(interval):
    time = "0.1"
    waveform = "sin"
    sample_rate = "48000"
    subprocess.run(["play", "-qr", sample_rate, "-n", "synth", time, waveform, str(interval[0]), waveform, str(interval[1]), "vol", "-10dB"])

def print_chord(base_freq, a, b):
    print(base_freq, a, b)

def synth_sine(f, r=44100, l=44100, a=1):
    return bytes(int(127.5 + a * 127.5 * sin(2 * 3.14159 * x * f / 44100)) for x in range(44100))

def synth_saw(f, r=44100, l=44100, a=1):
    return bytes(int(((f * 255 / r  * x) % 255) * a) for x in range(44100))

with wave.open("test.wav", "w") as f:
    f.setparams((1, 1, 44100, 0, "NONE", 0))
    f.writeframes(synth_saw(440, l=44100 * 5, a=0.25))
exit(0)



# MAIN

base_freq = 440
interval = ""
pure_intervals = [
    [2, 1], # octave (e.g. 880Hz, 440Hz)
    [3, 2], # fifth
    [4, 3], # fourth
    [5, 4], # major third
    [6, 5]  # minor third
]

for base_freq in range(300, 600, 10):
    for interval in pure_intervals:
        #a = random.randint(1, 15)
        #b = a + random.randint(-2, 2)
        #base_freq = random.randint(300, 500)

        

        #interval = input("Interval: ").split(" ")
        #interval = [base_freq, a, b]
        #interval = [4, 3]
        '''
        if interval[0] == "":
            exit()

        for i in range(3):
            interval[i] = int(interval[i])
        '''
        freqs = [0, 0, 0]
        freqs[0] = interval[0] / interval[1] * base_freq
        freqs[1] = base_freq

        #print_chord(interval[0], a, b)
        print(interval)
        play_chord(freqs)
        

        #base_freq = freqs[1]