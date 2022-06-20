
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

def synth_generator(melody=None, choose=None, **kwargs):
    b = random.choice(choose)
    if melody is None:
        return b([0], **kwargs)
    else:
        return b(melody, **kwargs)

bajo_ps = [bass, sawbass, jbass, dbass, sawbass]
bajo_p = random.choice(bajo_ps)

def bajo(melody=None, choose=[bajo_p], **kwargs):
    return synth_generator(melody=melody, choose=choose, **kwargs)

ambience_ps = [ambi, razz, prophet, saw, star, spark, blip, nylon]
ambience_p = random.choice(ambience_ps)



def ambience(melody=None, choose=[ambience_p], **kwargs):
    return synth_generator(melody=melody, choose=choose, **kwargs)

armonia_ps = [piano, rave, pasha, prophet, saw, star, spark, blip, arpy, nylon]
armonia_p = random.choice(armonia_ps)

def armonia(melody=None, choose=[armonia_p], **kwargs):
    return synth_generator(melody=melody, choose=choose, **kwargs)

category = {"techno_falopa": [rave, twang, quin, dirt], "tecno_amable": [arpy, blip, spark, saw, prophet, star, pasha], "gente_bien": [piano, nylon, marimba], }

ravem_ps = [rave, twang, quin, dirt]
ravem_p = random.choice(ravem_ps)


def ravem(melody=None, choose=[ravem_p], **kwargs):
    return synth_generator(melody=melody, choose=choose, **kwargs)

tecnom_ps = [arpy, blip, spark, saw, prophet, star, pasha]
tecnom_p = random.choice(tecnom_ps)


def tecnom(melody=None, choose=[tecnom_p], **kwargs):
    return synth_generator(melody=melody, choose=choose, **kwargs)

acusticom_ps = [piano, nylon, marimba]
acusticom_p = random.choice(acusticom_ps)

def acusticom(melody=None, choose=[acusticom_p], **kwargs):
    return synth_generator(melody=melody, choose=choose, **kwargs)

def restart_synths():
    global acusticom_p, tecnom_p, ravem_p, bajom_p, ambience_p, armonia_p
    
    acusticom_p = random.choice(acusticom_ps)
    tecnom_p = random.choice(tecnom_ps)
    ravem_p = random.choice(ravem_ps)
    bajo_p = random.choice(bajo_ps)
    ambience_p = random.choice(ambience_ps)
    armonia_p = random.choice(armonia_ps)

