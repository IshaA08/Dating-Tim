import random

# Pursuer Tim Class
# __init__ method: contains six attributes; two are for keeping count of each kind of interaction, another two for the user given probability for each kind of interaction, one for storing whichever interaction the pursuer partakes in and a sixth attribute that generates a random integer used for probability related actions 
# getProbabilities method # Arguments: self, user given probabilities for X and Y # Attains user input and alters associated attributes
# pursuerAction method # Arguments: self, xInteractProb, x and y Interactions count variables # Randomly generates whichever action the pursuer takes, using probabilities given by user; also does the additional tasks changing the counter for each king of interaction and re-generates a random number for further cycles of the method 
class Pursuer:
	def __init__(self):
		self.xInteractions = 0 # Number of each interaction
		self.yInteractions = 0
		self.xInteractProb = 0 # Probability of each interaction
		self.yInteractProb = 0
		self.whichPursuerOccurs = '' # Value changes according to whether X or Y occurs
		self.randomProbability = random.randrange(0, 101)
	
	def getProbabilities(self):
		print('\nEnter the probabilities of the X and Y behaviours for the Pursuer Tim.')
		try:
			self.xInteractProb = float(input('\nProbability of X-interactions: '))
			self.yInteractProb = float(input('\nProbability of Y-interactions: '))
			if self.xInteractProb < 0: # Have to first make sure that neither numbers are negative, then proceed for further checking
				print('\nPlease enter positive numerical values that sum to 100, try again.')
				self.xInteractProb, self.yInteractProb = self.getProbabilities()
			elif self.yInteractProb < 0:
				print('\nPlease enter positive numerical values that sum to 100, try again.')
				self.xInteractProb, self.yInteractProb = self.getProbabilities()
			elif self.xInteractProb + self.yInteractProb == 100:
				self.xInteractProb = self.xInteractProb
				self.yInteractProb = self.yInteractProb
			elif self.xInteractProb + self.yInteractProb == 1:
				self.xInteractProb = self.xInteractProb
				self.yInteractProb = self.yInteractProb
			else: # Handles input sum checking using recursion
				print('\nPlease enter numerical values that sum to 100, try again.')
				self.xInteractProb, self.yInteractProb = self.getProbabilities()
		except: # Handles type error through recursion
			print('\nPlease enter numerical values that sum to 100, try again.')
			self.xInteractProb, self.yInteractProb = self.getProbabilities()
		return self.xInteractProb, self.yInteractProb
	
	def pursuerAction(self): # Randomly generate and return interaction # Only need to check for one probability because if it's not in one probability, it must in the other then
		self.xInteractProb = int(self.xInteractProb)
		self.yInteractProb = int(self.yInteractProb)
		if self.randomProbability in range(0, self.xInteractProb + 1):
			self.whichPursuerOccurs = 'X'
			self.xInteractions += 1
		else:
			self.whichPursuerOccurs = 'Y'
			self.yInteractions += 1
		self.randomProbability = random.randrange(0, 101)
		return self.whichPursuerOccurs, self.xInteractions, self.yInteractions