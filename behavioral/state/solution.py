class CombinationLock:
    def __init__(self, combination):
        self.combination = combination
        self.reset()

    def reset(self):
        self.status = 'LOCKED'
        self.digits_entered = 0
        self.failed = False

    def enter_digit(self, digit):
        if self.status == 'LOCKED':
            self.status = ''
        self.status += str(digit)
        if self.combination[self.digits_entered] != digit:
            self.failed = True
        self.digits_entered += 1

        if self.digits_entered == len(self.combination):
            self.status = 'ERROR' if self.failed else 'OPEN'