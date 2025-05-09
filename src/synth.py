import subprocess
import math
from math import sin
import wave
from io import BytesIO, SEEK_SET
import random

'''
#def synth_sine(f, r=44100, l=44100, a=1):
#    for x in range(44100):
#        yield int(127.5 + a * 127.5 * sin(2 * math.pi * x * f / 44100))

def synth_two_sine(f1, f2, r=44100, l=44100, a=1):
    return bytes((int(127.5 + a * 127.5 * sin(2 * math.pi * x * f1 / 44100)) + int(127.5 + a * 127.5 * sin(2 * math.pi * x * f2 / 44100))) // 2 for x in range(44100))


def synth_saw(f, r=44100, l=44100, a=1):
    return bytes(int(((f * 255 / r  * x) % 255) * a) for x in range(44100))

def synth_saw_gen(f, r = 44100, a = 1):
    x = 0
    while True:
        yield int(((f * 255 / r  * x) % 255) * a)
        x += 1


# >>> a
# [1, 2, 3, 4, 5]
# >>> b
# ['a', 'b', 'c', 'd', 'e']
# >>> list(zip(a, b))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
# >>> 


def synth_sine(f, r=44100, l=44100, a=1):
    return bytes(int(127.5 + a * 127.5 * sin(2 * math.pi * x * f / 44100)) for x in range(44100))

#def sin(f, r=44100, l=44100, a=1):
#    for x in range(44100):
#        yield int(127.5 + a * 127.5 * sin(2 * math.pi * x * f / 44100))
'''

def sine_composition(*freqs: int, r = 44100, l = 44100, a = 1):
    """
    Generate a byte sequence representing a composite sine wave audio signal.

    Parameters:
    r (int): Sample rate in Hz (default is 44100).
    l (int): Length of the signal in samples (default is 44100, i.e., 1 second at 44.1 kHz).
    a (float): Amplitude scaling factor between 0 and 1 (default is 1).
    *freqs (int): One or more frequencies in Hz to include in the composite wave.

    Returns:
    bytes: A byte sequence representing the summed sine wave signal, where each sample is
           an 8-bit integer (0-255) suitable for audio playback or file writing.

    Note:
    - The output assumes unsigned 8-bit PCM audio where 127.5 is the midpoint (silence).
    - The amplitude and summing of multiple sine waves are not normalized and may clip
      if the total amplitude exceeds the 8-bit range.
    - This function does not include headers for audio formats like WAV.
    """
    a /= len(freqs)
    # return bytes(int(127.5 + 127.5 * a *  sum(n)) for n in zip(*((sin(2 * math.pi * x * f / r) for x in range(l)) for f in freqs)))

    samples = [[sin(2 * math.pi * x * f / r) for x in range(l)] for f in freqs]

    ret = []
    for n in zip(*samples):
        ret.append(int(127.5 + 127.5 * a * sum(n)))
    
    return bytes(ret)






# ~~~ MAIN ~~~

base_freq = 440
pure_intervals = [
    [2, 1], # octave (e.g. 880Hz, 440Hz)
    [3, 2], # fifth
    [4, 3], # fourth
    [5, 4], # major third
    [6, 5], # minor third
    [7, 6],
    [8, 7],
]

wf = BytesIO()
with wave.open(wf, "w") as f:
    f.setparams((1, 1, 44100, 0, "NONE", 0))
    
    '''for interval in pure_intervals:
        f.writeframes(sine_composition(base_freq, base_freq * interval[0] / interval[1], a=0.1))
'''
    #for base_freq in range(100, 2000, 100):
    while base_freq < 2000:
        support_freq = base_freq * 8 / 7
        f.writeframes(sine_composition(base_freq, support_freq, a=0.1)) 
        base_freq = support_freq

wf.seek(0, SEEK_SET)
subprocess.run(["play", "-"], input=wf.getvalue())