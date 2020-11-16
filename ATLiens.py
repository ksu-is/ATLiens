import random
import time
from pprint import pprint
class hero:
    def __init__(self, Phealth, Pattack, Pluck, Prange, Pdefense, Pmagic, Pname):
        self.health = Phealth
        self.attack = Pattack
        self.luck = Pluck
        self.range = Prange
        self.defense = Pdefense
        self.magic = Pmagic
        self.name = Pname

        def getHealth(self):
            return self.health
        def getAttack(self):
            return self.attack
        def getLuck(self):
            return self.luck
        def getRange(self):
            return self.range
        def getDefense(self):
            return self.defense
        def getMagic(self):
            return self.magic
        def getName(self):
            return self.name

        def setHealth(self, newHealth):
            self.health = newHealth
        def setAttack(self, newAttack):
            self.attack = newAttack
        def setLuck(self, newLuck):
            self.luck = newLuck
        def setRange(self, newRange):
            self.range = newRange
        def setDefense(self, newDefense):
            self.defense = newDefense
        def setMagic(self, newMagic):
            self.magic = newMagic
        def setName(self, newName):
            self.name = newName