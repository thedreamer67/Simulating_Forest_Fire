import numpy as np #this module contains methods for matrices. Here, it is needed for plotting
import random #contains functions for generating random numbers and shuffling. 
import matplotlib.pyplot as plt #needed for plotting
from matplotlib import animation #needed to make a movie
import matplotlib as mpl #needed for plotting


# Task 1

# Takes in width, height and density as input, and returns matrix and 
# graphical representation of forest.   
def createForest(width,height,density):
    # While loop to ensure that the user inputs a valid density. 
    # Prompts user to input another value until the density is valid.
    while density > 1 or density < 0:
        print("Error! The density is only possible to be between 0 and 1 inclusive. Try Again.")
        width = int(input("Enter the width of the forest: "))
        height = int(input("Enter the height of the forest: "))
        density = float(input("Enter the tree density: "))
    
    # Calculates the total number of squares
    area = int(width * height)
    
    # Calculates the total number of trees rounded to nearest integer
    trees = round(density * area)
    
    
    # Initialises an empty list
    forest = []
    
    # Creates a list of the total number of trees and ponds as 
    # elements in the same list
    templist = [] + [1]*trees + [0]*(area - trees)
    
    # Shuffles the order of elements in templist
    random.shuffle(templist)
    
    # Looping list slicing to create sublists in forest matrix
    for i in range(height):
        listslice = templist[i*width:(i+1)*width]
        forest.append(listslice)
    
    return forest


# Task 2

def fireSpreading(forest):
    width = len(forest[0])
    height = len(forest)
    area = width * height
    working_list = []
    for x in forest:
        working_list.extend(x)
        
    if not 3 in working_list:
        if width % 2 == 0 or height % 2 == 0:
            midpoint = int((area/2) + (width/2))
        else:
            midpoint = int(area/2)
        while working_list[midpoint] != 1:  
            midpoint += 1
            if midpoint >= area:
                break
        else:
            # Initial position of fire.
            working_list[midpoint] = 3
        
        
    else:
        # If fire(s) are already present, spread for each fire.
        # Identify whether the fire is not at the edge of the matrix
        # Identify whether the adjacent point is a tree
        # Setting fire only if both above are True
        location_i = 0
        for location in working_list:
            
            if location == 3:
                if (location_i+1) % width != 0:
                    _righti = location_i + 1
                    if working_list[_righti] == 1:
                        working_list[_righti] = 4
                
                if location_i % width != 0:
                    _lefti = location_i - 1
                    if working_list[_lefti] == 1:
                        working_list[_lefti] = 4
                
                if location_i >= width:
                    _abovei = location_i - width
                    if working_list[_abovei] == 1:
                        working_list[_abovei] = 4
                    
                if location_i < (area-width):
                    _belowi = location_i + width
                    if working_list[_belowi] == 1:    
                        working_list[_belowi] = 4
                        
                working_list[location_i] = 2
            
            location_i += 1
        
        count = 0
        for location in working_list:
            if location == 4:
                working_list[count] = 3
            count += 1

   # We want to restore the new forest matrix
    new_forest = []
    for i in range(height):
        listslice = working_list[i*width:(i+1)*width]
        new_forest.append(listslice)
              
    return new_forest
   

    


# Task 3

# Creates an empty list which will include the lists with the number of surviving trees for all 100 forests of each density.
allSurvivors = []
# Asks the user for the height and width of the forest matrix.
w = int(input("Enter the width of the forest: "))
h = int(input("Enter the height of the forest: "))
# Loops for the different densities.
for d10 in range(0, 11):
    # Creates an empty list which will include the number of surviving trees for all 100 forests of one density.
    # d = density
    d = float(d10/10)
    survived_trees_d = []
    # Loops for the 100 forests with density d
    for num in range(1,101):
        # Creates a forest with density d
        forest = createForest(w, h, float(d))
        
        # Burns the created forest
        while True:
            forest = fireSpreading(forest)

            workingforest = []        

            for x in forest:
                workingforest.extend(x)

            if not 3 in workingforest:
                break
        
        # Counts the number of surviving trees in the forest with density d and adds this number to the survived_trees_d list
        y = 0
        for x in workingforest:
            if x == 1:
                y += 1
        survived_trees_d.append(y)
    
    # Adds the list of numbers of surviving trees in the 100 forests with density d to the total_survived_trees list.
    allSurvivors.append(survived_trees_d)

print("")
# Prints the list with all the number of surviving trees in all 100 forests for all densities.
print("List of total number of trees that survived is", allSurvivors)

# Plots the MCM graph based on the allSurvivors list.
if allSurvivors!=[]:
    f, ax = plt.subplots(figsize=(7, 6))
    ax.boxplot(allSurvivors)
    
    ax.set_title('Monte Carlo simulation of forest fire')
    plt.xlabel('Density')
    plt.ylabel('Surviving trees')
    xax = list(map(str, list(np.array(range(11))/10)))
    plt.xticks(list(range(1,11)), xax)
    plt.savefig('SurvivorsVsDensity.png')