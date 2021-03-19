import numpy as np #this module contains methods for matrices. Here, it is needed for plotting
import random #contains functions for generating random numbers and shuffling. 
import matplotlib.pyplot as plt #needed for plotting
from matplotlib import animation #needed to make a movie
import matplotlib as mpl #needed for plotting

# Task 2: define a function that takes in a 2D matrix which is the forest, and sets it on fire
# output: a gif file of the input forest on fire from start to end

forest = [[1,0,1,1,0],
          [0,1,1,0,1],
          [1,1,0,0,1],
          [1,0,1,0,0],
          [0,1,1,1,0]]

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
