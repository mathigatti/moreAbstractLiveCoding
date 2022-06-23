
import random
random.seed(None)

def progressive(amplify1=1, amplify2=1):
  return var(P[1,0.5,0.25]*amplify2,P[16,8,8]*amplify2)

ritmos = [PSum(6, 8), PRand([0.5, 0.25]), PDur([3, 5], 8), PDur([2, 6], 8), PDur([1,7,3,5],8), progressive()]

def kick(sample=3, dur=4, **kwargs):
    return play("X", dur=dur,sample=sample, **kwargs)

def hihat(sample=3, dur=ritmos[1], **kwargs):
    return play("-", dur=dur, sample=sample, **kwargs)

def snare(echo=random.choice([0,P[0, var([0, [0.5, 0.25]], [14, 2])]]), **kwargs):
    return play(" " + random.choice(["o","O"]), sample=random.choice(range(4)), **kwargs)

def clap(dur=PDur(7,8), amp=PwRand([1,0],[4,1])[:16], sample=PRand(4)[:16], **kwargs):
    char = random.choice(["*", "r", "k", "f"])
    return play(char, dur=dur, amp=amp, sample=sample, **kwargs)

def ruidito():
	options = [
		play("/", rate=0.8, mix=0.15, room=0.7, dur=8, amp=notalways()*intermitent([0,1])),
        play("b",dur=9,sus=0.2,rate=PRand([0.5,1,2]), mix=0.1,room=1, amp=notalways()*intermitent([0,1])) + (0,2,-1),
	]
	return random.choice(options)

def synth_generator(b, melody=None, **kwargs):
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

bajo_ps = [bass, sawbass, jbass, dbass, sawbass]
random.shuffle(bajo_ps)

def bajo(melody=None, change=False, **kwargs):
    global bajo_ps
    if change:
        random.shuffle(bajo_ps)
    return synth_generator(bajo_ps[0], melody=melody, **kwargs)

ambience_ps = [ambi, razz, prophet, saw, star, spark, blip, nylon]
random.shuffle(ambience_ps)

def ambience(melody=None, change=False, **kwargs):
    global ambience_ps
    if change:
        random.shuffle(ambience_ps)
    if "dur" in kwargs:
        return synth_generator(ambience_ps[0], melody=melody, **kwargs)
    else:
        return synth_generator(ambience_ps[0], melody=melody, dur=8, **kwargs)

armonia_ps = [piano, rave, pasha, prophet, saw, star, spark, blip, arpy, nylon]
random.shuffle(armonia_ps)

def armonia(melody=None, change=False, **kwargs):
    global armonia_ps
    if change:
        random.shuffle(armonia_ps)
    return synth_generator(armonia_ps[0], melody=melody, **kwargs)

category = {"techno_falopa": [rave, twang, quin, dirt], "tecno_amable": [arpy, blip, spark, saw, prophet, star, pasha], "gente_bien": [piano, nylon, marimba], }

ravem_ps = [rave, twang, quin, dirt]
random.shuffle(ravem_ps)

def ravem(melody=None, change=False, **kwargs):
    global ravem_ps
    if change:
        random.shuffle(ravem_ps)
    return synth_generator(ravem_ps[0], melody=melody, **kwargs)

tecnom_ps = [arpy, blip, spark, saw, prophet, star, pasha]
random.shuffle(tecnom_ps)

def tecnom(melody=None, change=False, **kwargs):
    global tecnom_ps
    if change:
        random.shuffle(tecnom_ps)
    return synth_generator(tecnom_ps[0], melody=melody, **kwargs)

acusticom_ps = [piano, nylon, marimba]
random.shuffle(acusticom_ps)

def acusticom(melody=None, change=False, **kwargs):
    global acusticom_ps
    if change:
        random.shuffle(acusticom_ps)
    return synth_generator(acusticom_ps[0], melody=melody, **kwargs)

def rise(i = None):
    if i is None:
        i = random.choice(range(1,6))
    path = f"riser{i}"
    return loopm(path).once(dur=2*longitud_en_audios(path))




P[0, var([0, [0.5, 0.25]], [14, 2])]