import subprocess
import random

def play_chord(interval):
    time = "1.0"
    waveform = "sin"
    sample_rate = "48000"

    

    subprocess.run(["play", "-qr", sample_rate, "-n", "synth", time, waveform, str(interval[0]), waveform, str(interval[1]), "vol", "-10dB"])

def print_chord(base_freq, a, b):
    print(base_freq, a, b)

# MAIN

base_freq = 440
interval = ""
pure_intervals = [
    [2, 1], # octave
    [3, 2], # fifth
    [4, 3], # fourth
    [5, 4], # major third
    [6, 5]  # minor third
]

#for base_freq in range(400, 500, 5):
    #for interval in pure_intervals:
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

interval = [5, 4]

freqs = [0, 0, 0]
freqs[0] = interval[0] / interval[1] * base_freq
freqs[1] = base_freq

        #print_chord(interval[0], a, b)
print(interval)
play_chord(freqs)
        

        #base_freq = freqs[1]