#This code gives the simplified the calculation of the Nash equilibrium calculation.
#install and import all the necessary libraries
import os
os.system('pip3 install numpy')
os.system('pip3 install scipy')
os.system("pip3 install nashpy")
import nashpy as nash
import numpy as np
# Create the payoff matrix
A = np.array([[80,100],[50,70]]) # A is the row player
B = np.array([[80,50],[100,70]]) # B is the column player
game2 = nash.Game(A,B)
game2
# Find the Nash Equilibrium with Support Enumeration
equilibria = game2.support_enumeration()
#this allows to repeat the decision scenarios inside the game and compare
#the current option with the possible option that each player has to end up with a better decision.
for eq in equilibria:
    print(eq)
