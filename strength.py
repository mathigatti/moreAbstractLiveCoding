
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