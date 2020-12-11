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
				
def gameOver(enemyDead):
	if enemyDead == True;
		print("Time to move on to the next city")
		
	else:
		print("You are out of health")
		print("You were destroyed by the Alien")
		
def battle(genEnemy, genCharacter):
		print("Be careful!  A troglodite Alien has spotted you!)
		print("Look out! A giant Centariun Alien approaches!")
		print("Oh no it's an Alpha ATLien!")
		print(vars(genEnemy))
		
		battle = True
		
		while battle == True:
		
		
			print("1. Sword Attack\n2. Ranged Attack \n3. Magic Attack")
			choice = input()
		
			while choice != "1" and choice != "2" and choice != "3":
				print("Uh oh....you have to pick 1, 2 , or 3")
				print("1. Sword Attack\n2. Ranged Attack \n3. Magic Attack")
				choice = input()
				
			if choice == "1":
				damage = genCharacter.getAttack()
			elif choice == "2":
				damage = genCharacter.getRanged()
			elif choice == "3":
				damage = genCharacter.getMagic()
				
			print("You attack the Alien!")
			hit = hitChance(genCharacter.getLuck())
			
			if hit = True:
				genEnemy.setHealth(genEnemy.getHealth() - damage)
				print("You've damage the Alien!")
				print("The Alien now only has", genEnemy.getHealth())

			else:
				print("Your attackd missed the Alien")
				
			enemyDead = isDead(genEnemy.getHealth())
			
			if enemyDead = False:
				genCharacter.setHealth(genCharacter.getHealth() - enemyAttack(genEnemy.getChance(), genEnemy.getAttack(), genEnemy.getName, genCharacter.getDefense())))
			
				characterDead = isDead(genCharacter.getHealth())
				
				if characterDead == True:
					battle = False
					return False
				
				else
					print("Your characters remaining health is", genCharacter.getHealth())
					
			else:
				battle = False
				print("You have defeated the Alien!")
				print("You received the following loot...")
				loot(genCharacter.getLuck()), genCharacter)
				
				return True
				
				
			
def levelGenerator(character, level):

	maxNumberOfEnemies = math.ceil(level*6)
	for x in range (0, maxNumberOfEnemies):
		bossChance = random.randint(1,10)
		if bossChance > 7
			levelboss = True
			
		else:
			levelboss = False
			
		characterDead = battle(enemyGen(levelBoss), character)
		gameOver(characterDead)
		
def main():
	classData = createClass()
	character = hero(100, classData[0], classData[1], classData[2], classData[3], classData[4], classData[5])
	pprint(vars(character))
	print("Level 1... Midtown")
	levelGenerator(character, 1)
	print("Level 2... Smyrna")
	levelGenerator(character, 2)
	print("Level 3... Marietta")
	levelGenerator(character, 3)
	print("Level 4... Woodstock")
	levelGenerator(character, 4)
	print("Level 5... Canton")
	levelGenerator(character, 5)
	print("You have escaped Atlanta and the Alien invasion!")
	pprint(vars(character))
	

levelBoss = False

genCharacter = hero(100, 10, 11, 12, 1, 14, "Lee!")			

pprint(vars(genCharacter))

whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)

whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)

whoDied = battle(enemyGen(levelBoss), genCharacter)
gameOver(whoDied)


pprint(vars(genCharacter))
			
		
			
			
		
		

		
		

	