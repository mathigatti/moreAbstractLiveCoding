
'''
ascende pitch indefinidamente
generators con sinth elegido fijo
método sc para synth change
charlar con lu que recursos faltan
resolver beats, drums, pensar que recursos ritmicos faltan
    - ver marcadores
    - euler beats
    - santiago vazquez teoria y libro de comandos basicos
'''

def changeAmp(rate, group=None):
    if group is None:
        group = Master()
    for i in range(len(group)):
        if (not group.players[i].synthdef is None) and (group.players[i].name in list(map(lambda x: x.name, Clock.playing))):
            try:
                print("modifico a", group.players[i])
                group.players[i].amp = float(group.players[i].amp)*rate
            except:
                print("ERROR")
                print(group.players[i].amp)
                print(help(group.players[i].amp))


def fadeo(self, dur=16):
    self.amp = linvar([float(self.amp), 0], [dur, inf], start=now)
    return self

Player.fadeo = fadeo

def fadei(self, dur=16,amp=None):
    if amp is not None:
        self.amp = linvar([0, amp], [dur,inf], start=now)
    else:
        self.amp = linvar([0, float(self.amp)], [dur, inf], start=now)
    return self

Player.fadei = fadei
