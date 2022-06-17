
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

def bajo(melody=None, **kwargs):
    b = random.choice([bass, sawbass, jbass, dbass, sawbass])
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

def ambience(melody=None, **kwargs):
    b = random.choice([ambi, razz, prophet, saw, star, spark, blip, nylon])
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

def armonia(melody=None, **kwargs):
    b = random.choice([piano, rave, pasha, prophet, saw, star, spark, blip, arpy, nylon])
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

category = {"techno_falopa": [rave, twang, quin, dirt], "tecno_amable": [arpy, blip, spark, saw, prophet, star, pasha], "gente_bien": [piano, nylon, marimba], }

def ravem(melody=None, **kwargs):
    synths = [rave, twang, quin, dirt]
    b = random.choice(synths)
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

def tecnom(melody=None, **kwargs):
    synths = [arpy, blip, spark, saw, prophet, star, pasha]    
    b = random.choice(synths)
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

def acusticom(melody=None, **kwargs):
    synths = [piano, nylon, marimba]

    b = random.choice(synths)
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)