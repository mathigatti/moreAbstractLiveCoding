
# add periodic effect
def ape(player):
    if random.random() > 0.5:
        player.formant = var([random.randint(0, 10) for _ in range(3)], [16])
    elif random.random() > 0.5:
        player.mix = var([0, 1.], [12])
        player.room = var([0, 1.], [12])
    elif random.random() > 0.5:
        n = 3
        player.shape = [random.choice([0, 1, 2]) for _ in range(n)], [
            random.choice([12, 4, 8]) for _ in range(n)]
    if random.random() > 0.5:
        n = 3
        player.slide = var([random.choice([0, 1, 2]) for _ in range(n)], [
                           random.choice([12, 4, 8]) for _ in range(n)])
        player.glide = var([random.choice([0, 1, 2]) for _ in range(n)], [
            random.choice([12, 4, 8]) for _ in range(n)])
    elif random.random() > 0.5:
        n = 3
        player.chop = var([random.choice([0, 2, 3]) for _ in range(n)], [
                          random.choice([12, 4, 8]) for _ in range(n)])


Player.ape = ape

