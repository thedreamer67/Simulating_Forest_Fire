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
    
    # Accounts for the case where all are trees (each element in each 
    # list of the matrix is 1) to address the limitations of 
    # colors.ListedColormap() when only a single element is present
    if trees == area:
        fig = plt.figure(figsize=(15,15))
        plt.imshow(forest, mpl.colors.ListedColormap(['g']), interpolation='none')
        fig.savefig('forest.pdf')
    # Prints a graphical representation when density is not 1. 
    else:
        fig = plt.figure(figsize=(15,15))
        plt.imshow(forest, mpl.colors.ListedColormap(['b', 'g']), interpolation='none')
        fig.savefig('forest.pdf') 
    
    return forest

# Calls the function         
forest = createForest(int(input("Enter the width of the forest: ")),
                   int(input("Enter the length of the forest: ")),
                   float(input("Enter the tree density: ")))




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
        else:
            # Initial position of fire.
            working_list[midpoint] = 3
        
        fire_i = midpoint

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

   # We want to restore the the forest matrix
    new_forest = []
    for i in range(height):
        listslice = working_list[i*width:(i+1)*width]
        new_forest.append(listslice)
              
    return new_forest


fig = plt.figure(figsize=(15,15)) 
ims = []    

while True:

    forest = fireSpreading(forest)
    print(forest)
    
    workingforest = []        
    
    for x in forest:
        workingforest.extend(x)
        
    if 0 in workingforest and 1 in workingforest and 2 in workingforest and 3 in workingforest: #Pond, tree, ash, fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b', 'g', 'k', 'r']), animated=True, interpolation='none')
    elif not(0 in workingforest) and 1 in workingforest and 2 in workingforest and 3 in workingforest: #Tree, ash, fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['g', 'k', 'r']), animated=True, interpolation='none')
    elif 0 in workingforest and not(1 in workingforest) and 2 in workingforest and 3 in workingforest: #Pond, ash, fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b', 'g', 'k', 'r']), animated=True, interpolation='none')
    elif 0 in workingforest and 1 in workingforest and not(2 in workingforest) and 3 in workingforest: #Pond, tree, fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b', 'g', 'r']), animated=True, interpolation='none')
    elif 0 in workingforest and 1 in workingforest and 2 in workingforest and not(3 in workingforest): #pond, tree, ash
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b', 'g', 'k']), animated=True, interpolation='none')
    elif not(0 in workingforest) and not(1 in workingforest) and 2 in workingforest and 3 in workingforest: #Ash and fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['k', 'r']), animated=True, interpolation='none')
    elif not(0 in workingforest) and 1 in workingforest and not(2 in workingforest) and 3 in workingforest: #Tree and fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['g', 'r',]), animated=True, interpolation='none')
    elif not(0 in workingforest) and 1 in workingforest and 2 in workingforest and not(3 in workingforest): #Tree and ash
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['g', 'k']), animated=True, interpolation='none')
    elif 0 in workingforest and not(1 in workingforest) and not(2 in workingforest) and 3 in workingforest: #Pond and Fire
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b', 'r']), animated=True, interpolation='none')
    elif 0 in workingforest and not(1 in workingforest) and 2 in workingforest and not(3 in workingforest): #Pond and Ash
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b', 'k']), animated=True, interpolation='none')
    elif 0 in workingforest and not(1 in workingforest) and not(2 in workingforest) and not(3 in workingforest): #All pond
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['b']), animated=True, interpolation='none')
    else: #All ash
        im = plt.imshow(np.array(forest), cmap = mpl.colors.ListedColormap(['k']), animated=True, interpolation='none')
    
    ims.append([im])

    
    if not 3 in workingforest:
        break

    
ani = animation.ArtistAnimation(fig, ims, interval = 500, blit = True, repeat_delay=0, repeat = True)
ani.save('fire.gif', writer='imagemagick')