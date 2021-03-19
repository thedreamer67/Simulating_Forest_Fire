# Task 1: create a random forest with stated width, height and density (num_of_trees/area)
# output: a 2D matrix of 0s and 1s to represent water and trees

def createForest(width, height, density):
	from random import randint
	forest = [] # Initialise empty list
	trees = round(density * width * height) #Computes the total number of trees and rounds to nearest integer
	randsum = sum(sum(e) for e in forest) #Sums the total amount of trees in each row
	
	while randsum != trees:	#Keep iterating until the random number of trees is correct. This ensures independent randomisation of each element. 
		for x in range(height):
			templist = [] #Initialise an empty list at the start of each new row
			for y in range(width): #Iterate through each element
				templist.append(randint(0,1)) #Add an element to the temporary list
			forest.append(templist) # Add the completed row as an element to forest
	return forest
	
print(createForest(5,10,0.2))#Just to see the result
	
