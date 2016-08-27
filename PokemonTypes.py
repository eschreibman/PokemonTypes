#Eliza Schreibman
#Main and only file for running the PokemonTypes Program

########################################### BEGIN OF COLORS ############################################

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

############################################ END OF COLORS ############################################



############################################ BEGIN OF TYPE ############################################
#Pokemon types
class Type:
	#initializer that takes the name as a string and a color from bcolors
	def __init__(self, name, color):
		self.name = name
		self.color = color
		self.weakAgainstMe = []
		self.strongAgainstMe = []
		self.noEffectAgainstMe = []
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
	def add_noEffectAgainstMe(self, noEfTypes):
		for noEffect in noEfTypes:
			self.noEffectAgainstMe.append(noEffect)

	#takes an array of Types
	def add_notEffectiveAgainst(self, neaTypes):
		for nea in neaTypes:
			self.notEffectiveAgainst.append(nea)
	
	#takes an array of Types
	def add_superEffectiveAgainst(self, seaTypes):
		for sea in seaTypes:
			self.superEffectiveAgainst.append(sea)

	def printweakAgainstMe(self):
		printList(self.weakAgainstMe, " are weak against ", [self])

	def printstrongAgainstMe(self):
		printList(self.strongAgainstMe, " are strong against ", [self])

	def printNoEffectonMe(self):
		printList(self.noEffectAgainstMe, " have no effect on ", [self])

	def printnotEffectiveAgainst(self):
		finalstring = ""
		length = len(self.notEffectiveAgainst)
		if(length > 0):
			for t in range(length):
				#we're at the end and only need a space
				if (t + 1 == length):
					comma = ""
				#at the second to end and need an and
				elif (t + 2 == length):
					if (length > 2):
						comma = ", and "
					else:
						comma = " and "
				#else comma
				else:
					comma = ", "
				finalstring += (self.notEffectiveAgainst[t].color + str(self.notEffectiveAgainst[t]) + bcolors.ENDC + comma)
			print self.color + self.name + bcolors.ENDC + " is not very effective against " +  finalstring + bcolors.ENDC
	
	def printsuperEffectiveAgainst(self):
		finalstring = ""
		length = len(self.superEffectiveAgainst)
		if(length > 0):
			for t in range(length):
				#we're at the end and only need a space
				if (t + 1 == length):
					comma = ""
				#at the second to end and need an and
				elif (t + 2 == length):
					if (length > 2):
						comma = ", and "
					else:
						comma = " and "
				#else comma
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


############################################# END OF TYPE #############################################


########################################## BEING OF FUNCTIONS ##########################################
#global array of all types
allTypes = []
normal = Type("normal", bcolors.BLACK)
fire = Type("fire", bcolors.DARKRED)
water = Type("water", bcolors.BLUE)
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
	normal.add_noEffectAgainstMe([ghost])
	fire.add_weakAgainstMe([fire, grass, ice, bug, steel])
	water.add_weakAgainstMe([fire, water, ice, steel])
	electric.add_weakAgainstMe([electric, flying, steel])
	grass.add_weakAgainstMe([water, electric, grass, ground])
	ice.add_weakAgainstMe([ice])
	fighting.add_weakAgainstMe([bug, rock, dark])
	poison.add_weakAgainstMe([grass, fighting, poison, bug])
	ground.add_weakAgainstMe([poison, rock])
	ground.add_noEffectAgainstMe([electric])
	flying.add_weakAgainstMe([grass, fighting, bug])
	flying.add_noEffectAgainstMe([ground])
	psychic.add_weakAgainstMe([fighting, psychic])
	bug.add_weakAgainstMe([grass, fighting, ground])
	rock.add_weakAgainstMe([normal, fire, poison, flying])
	ghost.add_weakAgainstMe([poison, bug])
	ghost.add_noEffectAgainstMe([normal, fighting])
	dragon.add_weakAgainstMe([fire, water, electric, grass])
	dark.add_weakAgainstMe([ghost, dark])
	dark.add_noEffectAgainstMe([psychic])
	steel.add_weakAgainstMe([normal, grass, ice, flying, psychic, bug, rock, dragon, steel])
	steel.add_noEffectAgainstMe([poison])

def setStrongAgainstMe():
	normal.add_strongAgainstMe([fighting])
	fire.add_strongAgainstMe([water, ground, rock])
	water.add_strongAgainstMe([electric, grass])
	electric.add_strongAgainstMe([ground])
	grass.add_strongAgainstMe([fire, ice, poison, flying, bug])
	ice.add_strongAgainstMe([fire, fighting, rock, steel])
	fighting.add_strongAgainstMe([flying, psychic])
	poison.add_strongAgainstMe([ground, psychic])
	ground.add_strongAgainstMe([water, grass, ice])
	flying.add_strongAgainstMe([electric, ice, rock])
	psychic.add_strongAgainstMe([bug, ghost, dark])
	bug.add_strongAgainstMe([fire, flying, rock])
	rock.add_strongAgainstMe([water, grass, fighting, ground, steel])
	ghost.add_strongAgainstMe([ghost, dark])
	dragon.add_strongAgainstMe([ice, dragon])
	dark.add_strongAgainstMe([fighting, bug])
	steel.add_strongAgainstMe([fire, fighting, ground])

def setNotEffectiveAgainst():
	normal.add_notEffectiveAgainst([rock, ghost, steel])
	fire.add_notEffectiveAgainst([fire, water, rock, dragon])
	water.add_notEffectiveAgainst([water, grass, dragon])
	electric.add_notEffectiveAgainst([electric, grass, ground, dragon])
	grass.add_notEffectiveAgainst([fire, grass, poison, flying, bug, dragon, steel])
	ice.add_notEffectiveAgainst([fire, water, ice, steel])
	fighting.add_notEffectiveAgainst([poison, flying, psychic, bug, ghost])
	poison.add_notEffectiveAgainst([poison, ground, rock, ghost, steel])
	ground.add_notEffectiveAgainst([grass, flying, bug])
	flying.add_notEffectiveAgainst([electric, rock, steel])
	psychic.add_notEffectiveAgainst([psychic, dark, steel])
	bug.add_notEffectiveAgainst([fire, fighting, poison, flying, ghost, steel])
	rock.add_notEffectiveAgainst([fighting, ground, steel])
	ghost.add_notEffectiveAgainst([normal, dragon])
	dragon.add_notEffectiveAgainst([steel])
	dark.add_notEffectiveAgainst([fighting, dark])
	steel.add_notEffectiveAgainst([fire, water, grass, steel])

def setSuperEffectiveAgainst():
	fire.add_superEffectiveAgainst([grass, ice, bug, steel])
	water.add_superEffectiveAgainst([fire, ground, rock])
	electric.add_superEffectiveAgainst([water, flying])
	grass.add_superEffectiveAgainst([water, ground, rock])
	ice.add_superEffectiveAgainst([grass, ground, flying, dragon])
	fighting.add_superEffectiveAgainst([normal, ice, rock, dark, steel])
	poison.add_superEffectiveAgainst([grass])
	ground.add_superEffectiveAgainst([fire, electric, poison, rock, steel])
	flying.add_superEffectiveAgainst([grass, fighting, bug])
	psychic.add_superEffectiveAgainst([fighting, poison])
	bug.add_superEffectiveAgainst([grass, psychic, dark])
	rock.add_superEffectiveAgainst([fire, ice, flying, bug])
	ghost.add_superEffectiveAgainst([psychic, ghost])
	dragon.add_superEffectiveAgainst([dragon])
	dark.add_superEffectiveAgainst([psychic, ghost])
	steel.add_superEffectiveAgainst([ice, rock])

def populateAllData():
	setWeakAgainstMe()
	setStrongAgainstMe()
	setNotEffectiveAgainst()
	setSuperEffectiveAgainst()

#parses the user string
#searches for types of either one or two words
#returns an array where the first element in the number of correct words
#and the following elements are the correct type(s) (if any)
def searchForType(t):
	#parse the input to see how many words were entered
	parsedInput = t.split(" ")
	lenInput = len(parsedInput)

	if(lenInput == 1):
		#print "You entered one word: " + parsedInput[0]
		#see if the type entered matches a single name type
		for a in allTypes:
			if (str(parsedInput[0]) == a.name):
				return [1, a]
	elif (lenInput == 2):
		#print "You entered two words: " + parsedInput[0] + " and " + parsedInput[1]
		for a in allTypes:
			if (str(parsedInput[0]) == a.name):
				for b in allTypes:
					if(str(parsedInput[1]) == b.name):
						return [2, a, b]
				print "Your second word, " + parsedInput[1] + ", is not a type"
				return [0]
		print "Your first word, " + parsedInput[0] + ", is not a type"
	else:
		print "You did not enter one or two types. You entered " + str(lenInput) + " types, words, or space."
	return [0]

#printing for single types
def printAllData(someType):
	print "\n"
	someType.printNoEffectonMe()
	someType.printweakAgainstMe()
	someType.printstrongAgainstMe()
	someType.printnotEffectiveAgainst()
	someType.printsuperEffectiveAgainst()
	print "\n"

#printing for double types
def printDoubleType(typeOne, typeTwo):
	print "\n"
	combinedNoEffectList = typeOne.noEffectAgainstMe + typeTwo.noEffectAgainstMe
	printList(set(combinedNoEffectList), " have no effect on ", [typeOne, typeTwo])
	#types that are weak against both types 
	veryWeakList = set(typeOne.weakAgainstMe) & set(typeTwo.weakAgainstMe)
	printList(veryWeakList, " are Very weak against ", [typeOne, typeTwo])
	#logic to find types that are weak, but not very weak, against the double type
	combinedWeakList = ((set(typeOne.weakAgainstMe) - set(typeTwo.strongAgainstMe)) ^ (set(typeTwo.weakAgainstMe) - set(typeOne.strongAgainstMe)))
	printList(combinedWeakList, " are weak against ", [typeOne, typeTwo])
	#types that are strong against both types 
	veryStrongList = set(typeOne.strongAgainstMe) & set(typeTwo.strongAgainstMe)
	printList(veryStrongList, " are Very strong against ", [typeOne, typeTwo])
	#logic to find types that are strong, but not very strong, against the double type
	combinedStrongList = ((set(typeOne.strongAgainstMe) - set(typeTwo.weakAgainstMe)) ^ (set(typeTwo.strongAgainstMe) - set(typeOne.weakAgainstMe)))
	printList(combinedStrongList, " are strong against ", [typeOne, typeTwo])
	print "\n"

# modular list printing
# parameters: a list of types, a string phrase, an array of one or two types
def printList(list, phrase, typeOrTypes):
	finalstring = ""
	length = len(list)
	i = 0
	if (length > 0):
		for t in list:
			#we're at the end and only need a space
			if (i + 1 == length):
				comma = ""
			#at the second to end and need an and
			elif (i + 2 == length):
				if (length > 2):
					comma = ", and "
				else:
					comma = " and "
			#else comma
			else:
				comma = ", "
			finalstring += (t.color + str(t) + bcolors.ENDC + comma)
			i = i + 1
		if (len(typeOrTypes) == 1):
			print finalstring + phrase + typeOrTypes[0].color + typeOrTypes[0].name + bcolors.ENDC
		else:
			print finalstring + phrase + typeOrTypes[0].color + typeOrTypes[0].name + bcolors.ENDC + " " + typeOrTypes[1].color + typeOrTypes[1].name + bcolors.ENDC

########################################### END OF FUNCTIONS ###########################################



############################################ BEGIN OF MAIN ############################################

#good old main
def main():
	populateAllData()
	promptPhrase = "Enter a Type or Types (in lower case, separated by spaces) or 'q' to quit: "
	notFoundPhrase = "That was not a found type. Expected format: 'fire' or 'ice water'. Please try again: "
	possibleType = raw_input(promptPhrase)
	while(str(possibleType) != "q"):
		userType = searchForType(possibleType)
		#print "user type: " + str(userType)
		if(userType[0] == 1):
			printAllData(userType[1])
			possibleType = raw_input(promptPhrase)
		elif(userType[0] == 2):
			printDoubleType(userType[1], userType[2])
			possibleType = raw_input(promptPhrase)
		else:
			possibleType = raw_input(notFoundPhrase)









#when the program is run, call the above "main" function
if __name__ == "__main__": main()


