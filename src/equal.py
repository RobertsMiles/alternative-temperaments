import turtle as t
import math as m
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

def go_to_note(notes_in_octave, note, graphics_scaling):
    angle = 2 * m.pi / notes_in_octave * note
    t.goto(m.cos(angle) * graphics_scaling, m.sin(angle) * graphics_scaling)

def draw_graph(t):
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


# MAIN

t.delay(0)
graphics_scaling = 150

#notes_in_octave = int(input("Notes in octave: "))

#chords = [
#    [0, 1, 2], [0, 3, 4], [0, 5, 6]#,
    #[1, 2, 3], [1, 4, 5], [1, 6, 0],
    #[2, 3, 4], [2, 5, 6], [2, 0, 1],
    #[3, 4, 5], [3, 6, 0], [3, 1, 2],
    #[4, 5, 6], [4, 0, 1], [4, 2, 3],
    #[5, 6, 0], [5, 1, 2], [5, 3, 4],
    #[6, 0, 1], [6, 2, 3], [6, 4, 5],
#]

'''
notes_in_octave = 13
chords = [
    [i, i+2, i+5] for i in range(8) 
]
'''
'''
notes_in_octave = 13
chords = [[i, i+3, i+8] for i in range(0,notes_in_octave,1)] \
    + [[i, i+3, i+8] for i in range(0,notes_in_octave,2)] \
    + [[j, j+3, j+8] for j in range(0,notes_in_octave,3)] \
    + [[j, j+3, j+8] for j in range(0,notes_in_octave,4)] \
    + [[j, j+3, j+8] for j in range(0,notes_in_octave,5)]
    '''

notes_in_octave = 13
'''
# STS(13)
chords = [
    [1,3,12],
    [4,13,6],
    [12,13,5],
    [11,6,7],
    [10,5,8],
    [11,13,8],
    [2,5,6],
    [10,3,13],
    [10,11,4],
    [3,5,7],
    [1,11,5],
    [3,6,8],
    [9,13,7],
    [1,4,7],
    [4,12,8],
    [2,7,8],
    [9,1,8],
    [1,2,13],
    [10,12,7],
    [9,11,3],
    [9,10,2],
    [2,11,12],
    [9,4,5],
    [2,3,4],
    [9,12,6],
    [1,10,6]
]
'''
chords = [
    [0, 4, -9999]
]

for chord_index in range(len(chords)):

    chord = chords[chord_index]

    draw_graph(t)

    print()
    print(chord)
    play_chord(chord, notes_in_octave)