import manager

# Main Function
# Contains instantiation of manager module, main game frame

def main():
	print('Welcome to The Tims! Watch as the Pursuer Tim desperately tries to win the heart of the Target Tim!')
	manager = manager.Manager()
	manager.numberOfRuns, manager.pursuer.xInteractProb, manager.pursuer.yInteractProb, manager.target.xInteractProb, manager.target.yInteractProb = manager.getUserInput()
	manager.dateSuccess, manager.dateFail = manager.dateSimulation()
	manager.reportStats()

main()