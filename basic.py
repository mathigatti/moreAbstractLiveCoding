import random

### preguntarle a musicos su proceso de composición a nivel abstracto y replicarlo en codigo
### Ver cosas repetidas en sendCodigo

def sonando():
    print(Clock.playing)


def sintes():
    print(SynthDefs)


def escalas():
    print(Scale.names())


def params(player):
    print(player.attr.keys())

def ritmo_picante():
    pass


def mas_picante():
    pass

# ['freq', 'delay', 'buf', 'sample', 'env', 'fmod', 'pan', 'rate', 'midinote', 'channel', 'vib', 'vibdepth', 'slide', 'slidedelay', 'slidefrom', 'glide', 'glidedelay', 'bend', 'benddelay', 'coarse', 'striate', 'pshift', 'hpf', 'hpr', 'lpf', 'lpr', 'swell', 'bpf', 'bpr', 'bpnoise', 'bits', 'crush', 'dist', 'tmp', 'chop', 'tremolo', 'beat_dur', 'echo', 'echotime', 'spin', 'cut', 'room', 'mix', 'formant', 'shape', 'drive', 'sus', 'amp', 'blur', 'amplify', 'dur', 'degree', 'oct', 'bpm', 'atk', 'decay', 'rel', 'root', 'octave', 'deg', 'octa']


'''
- bend

- shape

- 'atk', 'decay', 'rel'

- deg

- blur

- echo y echotime

- delay

- 'vib', 'vibdepth'

- tremolo

- distorsion
	dist
	drive

- beats
	'bits' + 'crush'
'''

# ['aeolian', 'altered', 'bebopDom', 'bebopDorian', 'bebopMaj', 'bebopMelMin', 'blues', 'chinese', 'chromatic', 'custom', 'default', 'diminished', 'dorian', 'dorian2', 'egyptian', 'freq', 'halfDim', 'halfWhole', 'harmonicMajor', 'harmonicMinor', 'hungarianMinor', 'indian', 'justMajor', 'justMinor', 'locrian', 'locrianMajor', 'lydian', 'lydianAug', 'lydianDom', 'lydianMinor', 'major', 'majorPentatonic', 'melMin5th', 'melodicMajor', 'melodicMinor', 'minMaj', 'minor', 'minorPentatonic', 'mixolydian', 'phrygian', 'prometheus', 'romanianMinor', 'susb9', 'wholeHalf', 'wholeTone', 'yu', 'zhi']
