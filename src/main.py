import turtle as t
import math as m
import subprocess

# PREREQ: sox; python3-tkinter

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

def go_to_note(notes_in_octave, note, graphics_scaling):
    angle = 2 * m.pi / notes_in_octave * note
    t.goto(m.cos(angle) * graphics_scaling, m.sin(angle) * graphics_scaling)


# MAIN

t.delay(0)
graphics_scaling = 150

#notes_in_octave = int(input("Notes in octave: "))

# chords = [
#     [0, 1, 2], [0, 3, 4], [0, 5, 6],
#     [1, 2, 3], [1, 4, 5], [1, 6, 0],
#     [2, 3, 4], [2, 5, 6], [2, 0, 1],
#     [3, 4, 5], [3, 6, 0], [3, 1, 2],
#     [4, 5, 6], [4, 0, 1], [4, 2, 3],
#     [5, 6, 0], [5, 1, 2], [5, 3, 4],
#     [6, 0, 1], [6, 2, 3], [6, 4, 5],
# ]

'''
notes_in_octave = 13
chords = [
    [i, i+2, i+5] for i in range(8) 
]
'''

notes_in_octave = 13
chords = [[i, i+3, i+8] for i in range(0,notes_in_octave,1)] \
    + [[i, i+3, i+8] for i in range(0,notes_in_octave,2)] \
    + [[j, j+3, j+8] for j in range(0,notes_in_octave,3)] \
    + [[j, j+3, j+8] for j in range(0,notes_in_octave,4)] \
    + [[j, j+3, j+8] for j in range(0,notes_in_octave,5)]

for chord_index in range(len(chords)):
    '''
    try:
        a, b, c = input("Chord: ").split()
    except:
        quit()
    
    chord[0] = int(a)
    chord[1] = int(b)
    chord[2] = int(c)
    '''

    chord = chords[chord_index]

    t.resetscreen()

    # draw mod notes_in_octave graph
    t.color("black")
    t.up()
    t.goto(graphics_scaling, 0)
    t.down()
    for note in range(notes_in_octave + 1):
        t.color("red")
        t.stamp()
        t.color("black")
        go_to_note(notes_in_octave, note, graphics_scaling)

    # draw chord triple
    t.up()
    for i in range(3):
        note = chord[i]
        go_to_note(notes_in_octave, note, graphics_scaling)
        t.color("blue")
        t.down()
    note = chord[0]
    go_to_note(notes_in_octave, note, graphics_scaling)

    print()
    print(chord)
    play_chord(chord, notes_in_octave)