#Eliza Schreibman
#Main and only file for running the PokemonTypes Program

#some font colors I saw how to do this via stack overflow
class bcolors:
	RED = '\033[91m' #psycic
	DARKRED =    "\033[0,31m" #fire
	YELLOW = '\033[93m' #electric
	DARKYELLOW = "\033[0,33m" #ground
	GREEN = '\033[92m' #grass
	DARKGREEN =  "\033[0,32m" #bug
	BLUE = '\033[94m' #water
	CYAN =   "\033[0,36m" #ice
	MAGENTA = "\033[0,35m" #dragon
	PINK = '\033[95m'
	GRAY =  "\033[0,37m" #steel
	BLACK =    "\033[1,30m" #dark
	BOLD = '\033[1m' #ghost
	UNDERLINE = '\033[4m'
	ENDC = '\033[0m'

############################################ BEGIN OF TYPE ############################################
#Pokemon types
class Type:
	#initializer that takes the name as a string and a color from bcolors
	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.weakAgainstMe = []
		self.strongAgainstMe = []
		self.notEffectiveAgainst = []
		self.superEffectiveAgainst = []

	#takes an array of Types
	def add_weakAgainstMe(self, weakTypes):
		for weakType in weakTypes:
			self.weakAgainstMe.append(weakType)

	#takes an array of Types
	def add_strongAgainstMe(self, strongTypes):
		for strongType in strongTypes:
			self.strongAgainstMe.append(strongType)

	#takes an array of Types
	def add_notEffectiveAgainst(self, neaTypes):
		for nea in neaTypes:
			self.notEffectiveAgainst.append(nea)
	
	#takes an array of Types
	def add_superEffectiveAgainst(self, seaTypes):
		for sea in seaTypes:
			self.superEffectiveAgainst.append(sea)

	def printweakAgainstMe(self):
		finalstring = ""
		length = len(self.weakAgainstMe)
		for t in range(length):
			if(t + 1 == length):
				comma = ""
			elif (t + 2 == length):
				comma = ", and "
			else:
				comma = ", "
			finalstring += (self.weakAgainstMe[t].color + str(self.weakAgainstMe[t]) + bcolors.ENDC + comma)
		print finalstring + " are weak against " + self.color + self.name + bcolors.ENDC

	def printstrongAgainstMe(self):
			finalstring = ""
			length = len(self.strongAgainstMe)
			for t in range(length):
				if(t + 1 == length):
					comma = ""
				elif (t + 2 == length):
					comma = ", and "
				else:
					comma = ", "
				finalstring += (self.strongAgainstMe[t].color + str(self.strongAgainstMe[t]) + bcolors.ENDC + comma)
			print finalstring + " are strong against " + self.color + self.name + bcolors.ENDC

	def printnotEffectiveAgainst(self):
			finalstring = ""
			length = len(self.notEffectiveAgainst)
			for t in range(length):
				if(t + 1 == length):
					comma = ""
				elif (t + 2 == length):
					comma = ", and "
				else:
					comma = ", "
				finalstring += (self.notEffectiveAgainst[t].color + str(self.notEffectiveAgainst[t]) + bcolors.ENDC + comma)
			print self.color + self.name + bcolors.ENDC + " is not very effective against " +  finalstring + bcolors.ENDC
	
	def printsuperEffectiveAgainst(self):
			finalstring = ""
			length = len(self.superEffectiveAgainst)
			for t in range(length):
				if(t + 1 == length):
					comma = ""
				elif (t + 2 == length):
					comma = ", and "
				else:
					comma = ", "
				finalstring += (self.superEffectiveAgainst[t].color + str(self.superEffectiveAgainst[t]) + bcolors.ENDC + comma)
			print self.color + self.name + bcolors.ENDC + " is super effective against " +  finalstring + bcolors.ENDC


	#called if you try to print a Type
	def __str__(self):
		return self.name

	#to print out the arrays
	def __repr__(self):
		return self.name


############################################ END OF TYPE ############################################

#global array of all types
allTypes = []
normal = Type("normal", bcolors.BLACK)
fire = Type("fire", bcolors.DARKRED)
water = Type("water", bcolors.BLACK)
electric = Type("electric", bcolors.YELLOW)
grass = Type("grass", bcolors.GREEN)
ice = Type("ice", bcolors.CYAN)
fighting = Type("fighting", bcolors.BLACK)
poison = Type("poison", bcolors.BLACK)
ground = Type("ground", bcolors.DARKYELLOW)
flying = Type("flying", bcolors.BLACK)
psychic = Type("psychic", bcolors.RED)
bug = Type("bug", bcolors.DARKGREEN)
rock = Type("rock", bcolors.BLACK)
ghost = Type("ghost", bcolors.BOLD)
dragon = Type("dragon", bcolors.MAGENTA)
dark = Type("dark", bcolors.BLACK)
steel = Type("steel", bcolors.GRAY)
allTypes = [normal, fire, water, electric, grass, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel]

def setWeakAgainstMe():
	normal.add_weakAgainstMe([ghost])
	fire.add_weakAgainstMe([fire, grass, ice, bug, steel])

def setStrongAgainstMe():
	normal.add_strongAgainstMe([fighting])
	fire.add_strongAgainstMe([water, ground, rock])

def setNotEffectiveAgainst():
	normal.add_notEffectiveAgainst([rock, ghost, steel])
	fire.add_notEffectiveAgainst([fire, water, rock, dragon])

def setSuperEffectiveAgainst():
	fire.add_superEffectiveAgainst([grass, ice, bug, steel])


def populateAllData():
	setWeakAgainstMe()
	setStrongAgainstMe()
	setNotEffectiveAgainst()
	setSuperEffectiveAgainst()

def searchForType(t):
	for a in allTypes:
		if (t == a.name):
			return a
	return None


def printAllData(someType):
	someType.printweakAgainstMe()
	someType.printstrongAgainstMe()
	someType.printnotEffectiveAgainst()
	someType.printsuperEffectiveAgainst()

#good old main
def main():
	populateAllData()
	possibleType = raw_input("Enter a Type or 'q' to quit: ")
	while(possibleType != "q"):
		userType = searchForType(possibleType)
		if(userType != None):
			printAllData(userType)
			possibleType = raw_input("Enter a Type or 'q' to quit: ")
		else:
			possibleType = raw_input("that was not a type. try again: ")









#when the program is run, call the above "main" function
if __name__ == "__main__": main()


