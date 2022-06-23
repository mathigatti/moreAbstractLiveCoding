
import random
random.seed(None)

def startTime(bpm):
    return Clock.mod(bpm) - 0.1

def changeDur(rate, group=None):
    if group is None:
        group = Master()
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x: x.name, Clock.playing))):
            try:
                print("modifico a", group.players[i])
                group.players[i].dur = float(group.players[i].dur)*rate
            except:
                print("ERROR")
                print(group.players[i].dur)
                print(help(group.players[i].dur))


def changeDurFor(change, intervalo, group=None):
    changeDur(change, group=group)
    Clock.future(intervalo, lambda: changeDur(1/change, group=group))

def progressiveChange(change, times, intervalo, group=None):
    changeDurFor(change, intervalo*times, group)
    Clock.future(intervalo, lambda: progressiveChange(
        change, times-1, intervalo, group))


def spread(values, level=1, tt=var):
    intervals = [32, 32, 64, 64]
    return tt(values, [x*level for x in intervals])


def notalways(order=1, level=3, tt=var):
    if order == 1:
        pattern = [0, 1]
    else:
        pattern = [1, 0]
    return tt(pattern, 4**level)

def intermitent(values, level=0.5, tt=var):
    intervals = [int(c*level) for c in [28, 4, 32, 64, 128, 31, 1, 32]]
    random.shuffle(intervals)
    return tt(values, intervals)

# turn off sometimes
def tos(self):
    self.amp = intermitent([random.choice([0,1,1]) for _ in range(8)])
    return self

Player.tos = tos


def unsolo(player, rate, stop=True):
    if stop:
        player.stop()
    player.solo(0)
    changeDur(rate)


def solo_locop(start, dur, player, rate):
    player.solo()
    Clock.schedule(lambda: unsolo(player, rate, stop=False), start+8)


def magia(self, dur=8, rate=1):
    start = startTime(dur)
    Clock.schedule(lambda: solo_locop(start, dur, self, rate), start)
    return self


Player.magia = magia


def solo_loco(start, dur, sample, rate):
    q9.reset() >> stretch(sample, dur=dur, delay=0, hpf=0).solo()
    Clock.schedule(lambda: unsolo(q9, rate), start+8)


def magia(dur=8, rate=1, sample="dont_follow_rules"):
    start = startTime(dur)
    Clock.schedule(lambda: solo_loco(start, dur, sample, rate), start)


def enciendo(group):
    group.solo(0)

def apagoenciendo(group, duration=16):
    group.solo()
    Clock.future(duration,lambda : enciendo(group))


# Abajo/Arriba Silence Drums


def abajo():
    d_all.lpf = 500
    d_all.solo()


def arriba():
    d_all.lpf = 0
    d_all.solo(0)


def abajoarriba(intervalo):
    abajo()
    Clock.future(intervalo, lambda: arriba())

from FoxDot import FOXDOT_ROOT

from pydub import AudioSegment
from os.path import join

def longitud_en_audios(sample):
    bpms = Clock.bpm
    audio = AudioSegment.from_wav(join(FOXDOT_ROOT, "snd/_loop_", sample + ".wav"))
    length_in_seconds = len(audio)/(1000)
    return round(bpms*length_in_seconds/60)

def loopm(path="foxdot", *args, **kwargs):
    duracion = longitud_en_audios(path)
    if len(args) > 0 or "dur" in kwargs:
        return loop(path,*args, **kwargs)
    else:
        return loop(path,var(P[:duracion],1, start=now), dur=[1], **kwargs) # Cargar sample entero y una sola vez

def once(self, dur=1/16):
    ''' play sound once '''
    self.amp = var([1, 0], [dur, inf], start=now)
    return self


Player.once = once
