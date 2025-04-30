import turtle as t
import subprocess

def play_chord(chord, notes_in_octave):
    base_freq = 440
    time = "1.0"
    waveform = "sin"
    sample_rate = "48000"

    # convert each note from its index on the graph (1, 3, etc) to its frequency (Hz)
    for i in range(3):
        chord[i] = 2 ** (chord[i] / notes_in_octave) * base_freq
        print(chord[i])

    subprocess.run(["play", "-qr", sample_rate, "-n", "synth", time, waveform, str(chord[0]), waveform, str(chord[1]), waveform, str(chord[2]), "vol", "-10dB"])
