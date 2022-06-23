
import random
random.seed(None)

def progressive(amplify1=1, amplify2=1):
  return var(P[1,0.5,0.25]*amplify2,P[16,8,8]*amplify2)

ritmos = [PSum(6, 8), PRand([0.5, 0.25]), PDur([3, 5], 8), PDur([2, 6], 8), PDur([1,7,3,5],8), progressive()]

def kick(sample=3, dur=1, **kwargs):
    return play("X", dur=dur,sample=sample, **kwargs)

def hihat(sample=3, dur=ritmos[1], amp=PWhite(0.5,1), **kwargs):
    random.choice(["-", "-", "n"])
    return play("-", dur=dur, sample=sample, amp=amp, **kwargs)

def snare(echo=random.choice([0,P[0, var([0, [0.5, 0.25]], [14, 2])]]), **kwargs):
    return play(" " + random.choice(["o","O"]), sample=random.choice(range(4)), **kwargs)

def clap(dur=PDur(7,8), amp=PwRand([1,0],[4,1])[:16], sample=PRand(4)[:16], **kwargs):
    char = random.choice(["*", "r", "k", "f"])
    return play(char, dur=dur, amp=amp, sample=sample, **kwargs)

def bata():
	options = [
        play('X#X-', dur=0.5, room=1, mix=0.25, sample=1).every(6,'amen'),
        play('Q#Q-Q#', dur=PDur([3,5],8), rate=0.5, room=1, mix=0.25, sample=2,lpf=200,amp=3),
        play("x-x[Oo]",sample=3).every(6,'amen').every(3,'stutter',4,dur=1, degree="y", ident=1),
        play(P["V::"][:16] & P["<v ><  |o1| >"], drive=0.1, rate=1.2),
        play("<X >< (nb)H(l[hI])>", sample=2, mix=0.1, room=0.9, rate=0.8, amp=2),
        play("<|X2|=><  |@3| >", sample=2),
        play("<|V0|:><  O ><|[--]5|><...(+|L2|)>< m>", sample=2),
        play("<V:><  * ><[--]>")
    ]
	return random.choice(options)

def ruidito():
    length = 4
    amp = notalways()*intermitent([0,1])
    options = [        
        play("/", rate=0.8, mix=0.15, room=0.7, dur=8, amp=amp),
        play("b",dur=9,sus=0.2,rate=PRand([0.5,1,2]), mix=0.1,room=1, amp=amp) + (0,2,-1),
        #nylon(PWalk(1) + linvar([0,15],length),amp=amp*var([linvar([0.9,1],length),0],length), dur=0.125,oct=4, lpf=0, mix=0.2,room=1,scale=Scale.minorPentatonic),
        play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), amp=amp, rate=4, pan=-0.5),
        play("#", dur=32, room=1, amp=amp*2).spread(),
        play("e", amp=amp, dur=PRand([1/2,1/4]), pan=var([-1,1],2))
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

armonia_ps = [piano, pasha, prophet, saw, star, spark, blip, arpy, nylon]
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