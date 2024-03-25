import random
import pursuer 
import target

# Manager Class -- layman between the pursuer and target modules
# Main body of the simulator # Calls Pursuer and Target modules
# __init__ method: contains instantiation of pursuer and target classes, a variable for user input for the amount of times the simulation should run, has two more variables for keeping count of failed/successful interactions between the Tims
# getUserInput method: in charge of attaining all necessary user input (target/pursuer probabilities and number of runs)
# dateSimulation method: actually carries out the dates for the desired amount of cycles as per user input, uses for loop to do this and also prints results of each interaction
# reportStats method: simply prints out the end results of the simulation in user-friendly format; does not actually change any members
# No arguments needed for any methods
class Manager:
	def __init__(self):
		self.pursuer = pursuer.Pursuer()
		self.target = target.Target()
		self.numberOfRuns = 0 
		self.dateSuccess = 0 
		self.dateFail = 0 
	
	def getUserInput(self):
		self.pursuer.xInteractProb, self.pursuer.yInteractProb = self.pursuer.getProbabilities()
		self.target.xInteractProb, self.target.yInteractProb = self.target.getProbabilities()
		try:
			self.numberOfRuns = int(input('\nFrom one to one hundred, how many times do you want the Tims to interact?'))
			if self.numberOfRuns in range(1, 101):
				self.numberOfRuns = self.numberOfRuns
			else:
				print('\nSorry, that number is not in the range of one to one hundred, try again.')
				self.numberOfRuns = self.getUserInput()
		except:
			print('\nPlease provide an integer from one to one hundred, try again.')		
			self.numberOfRuns = self.getUserInput()
		return self.numberOfRuns, self.pursuer.xInteractProb, self.pursuer.yInteractProb, self.target.xInteractProb, self.target.yInteractProb
	
	def dateSimulation(self):
		print('\nCommencing Tim interactions; the Pursuer nervously approaches the Target.')
		for i in range(1, self.numberOfRuns + 1):
			self.pursuer.whichPursuerOccurs, self.pursuer.xInteractions, self.pursuer.yInteractions = self.pursuer.pursuerAction(self.pursuer.xInteractProb, self.pursuer.xInteractions, self.pursuer.yInteractions)
			self.target.whichTargetOccurs, self.target.xInteractions, self.target.yInteractions = self.target.targetAction(self.target.xInteractProb, self.target.xInteractions, self.target.yInteractions)
			if self.pursuer.whichPursuerOccurs == self.target.whichTargetOccurs:
				self.dateSuccess += 1 
				print('\nTurn #', i, ' : Match; Pursuer', self.pursuer.whichPursuerOccurs, 'and Target', self.target.whichTargetOccurs)
			else:
				self.dateFail += 1 
				print('\nTurn #', i, ' : No Match; Pursuer', self.pursuer.whichPursuerOccurs, 'and Target', self.target.whichTargetOccurs)	
		return self.dateSuccess, self.dateFail

	def reportStats(self):
		print('\n\nThe simulation has ended. The results of the Tims\' dates are:')
		print('\nThe Pursuer Tim\nNumber of X interactions:', self.pursuer.xInteractions, '\nNumber of Y interactions:', self.pursuer.yInteractions)
		print('\nThe Target Tim\nNumber of X interactions:', self.target.xInteractions, '\nNumber of Y interactions:', self.target.yInteractions)
		print('\nTotal number of successful dates:', self.dateSuccess)
		print('\nTotal number of failed dates:', self.dateFail)
		print('\nTotal number of dates: ', self.numberOfRuns, '\nPercentage of dates succeeded: ', int(((self.dateSuccess/(self.dateSuccess + self.dateFail))*100)), '%', '\nPercentage of dates failed: ', int(((self.dateSuccess/(self.dateSuccess + self.dateFail))*100)), '%')
