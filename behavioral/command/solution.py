from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount