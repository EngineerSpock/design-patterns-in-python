class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Game:
    def __init__(self):
        self.rat_enters = Event()
        self.rat_dies = Event()
        self.notify_rat = Event()


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1

        game.rat_enters.append(self.rat_enters)
        game.notify_rat.append(self.notify_rat)
        game.rat_dies.append(self.rat_dies)

        self.game.rat_enters(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_dies(self)

    def rat_enters(self, which_rat):
        if which_rat != self:
            self.attack += 1
            self.game.notify_rat(which_rat)

    def notify_rat(self, which_rat):
        if which_rat == self:
            self.attack += 1

    def rat_dies(self, which_rat):
        self.attack -= 1