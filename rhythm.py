
import random
random.seed(None)

ritmos = [PSum(6, 4), PRand([0.5, 0.25])]

def kick(sample=3, **kwargs):
    if "sample" in kwargs:
        return play("X   ", **kwargs)
    else:
        return play("X   ", sample=sample, **kwargs)

def hihat(sample=3, **kwargs):
    if "dur" in kwargs:
        return play("-", **kwargs)
    else:
        return play("-", dur=ritmos[-1], **kwargs)

def clap(**kwargs):
    sample = random.choice(["*", "r", "k", "f"])
    if "dur" in kwargs:
        return play(sample, **kwargs)
    else:
        return play(sample, dur=PDur(7,8), amp=PwRand([1,0],[4,1])[:16], sample=PRand(4)[:16], **kwargs)

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
    return synth_generator(ambience_ps[0], melody=melody, **kwargs)

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