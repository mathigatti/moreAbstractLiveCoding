
def mayor(pentatonic=False):
    if pentatonic:
        Scale.default = "minorPentatonic"
    else:
        Scale.default = "minor"

def menor(pentatonic=False):
    if pentatonic:
        Scale.default = "minorPentatonic"
    else:
        Scale.default = "minor"

pmajor = [var([0, 4, 5, 3], 4), var([0, 4, 3, 4], 4), var([0, 5, 3, 4], 4), var(
    [0, 3, 5, 4], 4), var([5, 3, 4, 0], 4), var([5, 4, 0, 3], 4)]
pminor = [var([0, 5, 4, 2], 1), var([0, 2, 3, 4], 4), var([0, 2, -1, -3], 4),
          var([0, 1, 2], [12, 2, 2]), var([0, 4, 5, 3], 4), var([0, -2, -1, 2], 4)]


def arpegio(notes, chord=(0, 2, 4)):
    return [note+interval for note in notes for interval in chord]


def acorde(notes, chords=(0, 2, 4)):
    return [tuple([note+interval for interval in chord]) for note in notes]

def increasePitch(player, increment=1):
    player += increment

def ipp(player, increment=1, times=4, interval=8):
    start = startTime(interval)
    increasePitch(player, increment)
    if times > 0:
        Clock.schedule(lambda: ipp(player, increment, times-1, interval), start+interval)

# pitch ascendent change
def pac(self, increment=1, times=16, interval=1):
    start = startTime(interval)
    ipp(self,increment, times, interval)
    Clock.schedule(lambda: increasePitch(self, int(-2/3*increment*times)), start+interval*times)
    return self

Player.pac = pac

def un_pasito(pasos=2, length=32):
  return PWalk(pasos)[:length]
