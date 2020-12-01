import random
import time
import math
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
            
def createClass():
	a = input("Are you more strategic (press 1) or more of a warrior (press 2)")
	while a != "1" and a != "2"
		print("invalid selection")
            	a = input("Are you more strategic (press 1) or more of a warrior (press 2)...")

	if a == "1":
		heroAttack = 50
		heroDefense = 100
	elif a == "2"
		heroAttack = 100
		heroDefense = 50

	b = input("Press enter to roll a dice...")
	time.sleep(0.2)
	print ("rolling dice")
	heroLuck = random.randint(0,10)
	print("your hero has", heroLuck, "luck out of 10")
	
	c = input("are you more of a bow and arrow user (press 1) or a magic user (press 2)")
	while c != "1" and c != "2"
		print("invalid selection")
		c = input("are you more of a bow and arrow user (press 1) or a magic user (press 2)")

	if c == "1"
		heroRanged = 100
		heroMagic = 50
		
	elif c == "2"
		heroRanged = 50
		heroMagic = 100
		
	heroName = input("What is your name hero")
	print ("Welcome", heroName, "!!!")
	
	return (heroAttack, heroLuck, heroRanged, heroDefense, heroMagic, heroName)
	
class_data = createClass()

character = hero(100, class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5], class_data[6])
pprint(vars(character))

class enemy
	def __init__ (self, EHealth, EAttack, Especial, Echance, Ename)
		self.health = EHealth
		self.attack = EAttack
		self.special = Especial
		self.chance = Echance
		self.name = Ename
		
	def getHealth(self):
		return self.health
	def getAttack(self):
		return self.attack		
	def getSpecial(self):
		return self.special		
	def getChance(self):
		return self.chance		
	def getName(self):
		return self.name
	
	def setHealth(self, newHealth):
		self.health = newHealth
	def setAttack(self, newAttack):
		self.attack = newAttack
	def setSpecial(self, newSpecial):
		self.special = newSpecial
	def setChance(self, newChance):
		self.chance = newChance
	def setName(self, newName):
		self.name = newName
	
class boss (enemy)
	def __init__(self, EHealth, EAttack, Especial, Echance, Ename, EsuperMove):
		super().__init__ (EHealth, EAttack, Especial, Echance, Ename)
		
		self.superMove = EsuperMove
		
		get getSuper(self):
			return self.superMove
		get setSuper(self, newSuperMove)
			self.superMove = newSuperMove
			
def enemyGen(levelBoss):
	temp = []
	file = open("adjective.txt","r")
	lines = files.readlines()
	adjective = lines[random.randint(0,len(lines)-1][:-1]
	file.close
	file = open("familynames.txt","r")
	lines = files.readlines()
	familynames = lines[random.randint(0,len(lines)-1][:-1]
	file.close
	
	if levelBoss == False:
		health = random.randint(50,100)
		attack = random.randint(1,10)
		special = random.randint(10,20)
		chance = random.randint(1,10)

		return enemy(health, attack, special, chance, adjective+"  "+familynames)
		
	else:
		health = random.randint(200,100)
		attack = random.randint(20,40)
		special = random.randint(50,60)
		chance = random.randint(1,8)
		superMove = random.randint(100,200)
		
		return boss(health, attack, special, chance, adjective+"  "+familynames, superMove)
		
def enemyAttack(hitChance, attackValue, name, defense):
	print(name, "is winding up for an attack...")
	hit = random.randint(0,10)	
	if hitChance >= hit:
		print("it hits the player!!!")
		loss = attackValue = defense
		print("you stagger losing...", loss, "health")
		return math.ceil(loss)
	else:
		print("the enemy misses!")
		return 0
		
def hitChance(luck):
	hit = random.randint(0,4)
	if luck < hit: 
		print("Miss!")
		return False
		
	else:
		print("The enemy has been hit!")
		return True
		
def isDead(health):
	if health < 1:
		return True
	else 
		return False
		
def loot(luck, genCharacter):
	lootChance = random.randint(0,4)
	if luck < lootCHance:
		print("NO LOOT AWARDED")	
		
	else:
		tableNum = random.randint(0,4)
		lootTableList = ["defense","items","magic","melee","range"]	
		itemType = lootTableList[tableNum]
		file = open(itemType+".txt","r")
		lines = file.readlines()
		
		print("The enemy dropped...")
		
		item = random.randint(0,len(lines)-1)
		
		itemLine = lines[item]
		splitItemLine = itemLine.split(",")
		
		name = splitItemLine[0]
		value = int(splitItemLine[1])
		
		print(name)
		
		if itemType == "attack":
			genCharacter.setAttack(genCharacter.getAttack()+value)
			print("Your new attack is...")
			print(genCharacter.getAttack)
		
		elif itemType == "range":
			genCharacter.setRange(genCharacter.getRange()+value)
			print("Your new ranged attack is...")
			print(genCharacter.getRange)
			
		elif itemType == "defense":
			genCharacter.setDefense(genCharacter.getDefense()+value)
			print("Your new defensize item is...")
			print(genCharacter.getDefense)
			
		elif itemType == "magic":
			genCharacter.setMagic(genCharacter.getMagic()+value)
			print("Your new magic attack is...")
			print(genCharacter.getMagic)
			
		else:
		
			if splitItemLine[2] == "luck":
				genCharacter.setLuck(genCharacter.getLuck()+value)
				print("Your new luck is...")
				print(genCharacter.getLuck())
				
			elif splitItemLine[2] == "health":
				genCharacter.setHealth(genCharacter.getHealth()+value)
				print("Your new Health is...")
				print(genCharacter.getHealth())
				

genCharacter = hero(100, 10, 11, 12, 1, 14, "Lee!")			

pprint(vars(genCharacter))

loot(100, genCharacter)
loot(100, genCharacter)
loot(100, genCharacter)
loot(100, genCharacter)

pprint(vars(genCharacter))
			
			
			
			
		
		

		
		

	