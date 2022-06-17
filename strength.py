
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
