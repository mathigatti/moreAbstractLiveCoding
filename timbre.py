
# add periodic rythm
def apr(player):
    if random.random() > 0.5:
        n = 3
        player.chop = var([random.choice([0, 2, 3]) for _ in range(n)], [
                          random.choice([12, 4, 8]) for _ in range(n)])

Player.apr = apr

# add periodic effect
def ape(player, spicy=False):
    if random.random() > 0.5:
        player.mix=intermitent([random.choice([0,0.1,0.2]) for _ in range(8)])
        player.room=intermitent([random.choice([0,0.6,0.7]) for _ in range(8)])
    if random.random() > 0.5:
        player.lpf = intermitent([random.choice([0,300,900,0,500]) for _ in range(8)])

    if spicy:
        if random.random() > 0.5:
            player.formant = var([random.randint(0, 10) for _ in range(3)], [16])
        elif random.random() > 0.5:
            n = 3
            player.shape = [random.choice([0, 1, 2]) for _ in range(n)], [
                random.choice([12, 4, 8]) for _ in range(n)]
        elif random.random() > 0.5:
            n = 3
            player.slide = var([random.choice([0, 1, 2]) for _ in range(n)], [
                            random.choice([12, 4, 8]) for _ in range(n)])
            player.glide = var([random.choice([0, 1, 2]) for _ in range(n)], [
                random.choice([12, 4, 8]) for _ in range(n)])


Player.ape = ape

