class Player:
    def __init__(self):
        self.name = "anon"
        self.hp = 100

    def kick(self, p, d):
        p.hp -= d