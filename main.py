# Alice and Don star puzzle

# Want to visualise the Win Triangle for a given box setup of 2 by n

# Import libraries
import matplotlib.pyplot
import numpy as np
import math
import matplotlib

# CC functions for Alice and Don's steps
# Where n = columns
def alice_cc(n):
    alice_step = []
    for x in range(1, 2*n+1):
        alice_step.append(x)
    return np.array(alice_step)

def don_cc(n):
    don_step = []
    for x in range(1, n+1):
        don_step.append(x)
        don_step.append(x + n)
    return np.array(don_step)

# KDS function to weave two arrays together
def weave(arr1,arr2):
    #Check if arrs same size
    if len(arr1)==len(arr2):
        arr=[]
        for i in range(len(arr1)*2):
            if(i%2==0):
                arr.append(arr1[math.floor(i/2)])
            else:
                arr.append(arr2[math.floor(i/2)])
        return arr
    else:
        print("Arrays not same size")
        quit

def alice_kds(n):
    arr1 = [x+1 for x in range(2*n)]
    return arr1

def don_kds(n):
    arr1=[x+1 for x in range(n)]
    arr2=[x+n+1 for x in range(n)]
    return (weave(arr1,arr2))

# Function to take two arrays and return who wins (given star pos and option for first or both)
def winner(arr1,arr2,star1,star2,win_option=1):

    # Initialise output positions
    arr1_pos=-1
    arr2_pos=-1

    # Looking for first star only
    if win_option==1:
        for i in range(len(arr1)):
            if (arr1[i]==star1 or arr1[i]==star2) and arr1_pos==-1:
                arr1_pos=i
        for i in range(len(arr2)):
            if (arr2[i]==star1 or arr2[i]==star2) and arr2_pos==-1:
                arr2_pos=i
        if arr1_pos<arr2_pos:
            winner=1
        elif arr2_pos<arr1_pos:
            winner=2
        else:
            winner=0
        return winner
    # Looking for both stars
    elif win_option==2:
        return True
    else:
        return "Invalid winner_option: Select 1 for first star, 2 for both stars"

# Function to create array with all possible star combinations

def star_combinations(n):
    # Generate all combinations of stars
    star_pos = {}
    star_win = {}
    for i in range(1, 2 * n + 1):
        for j in range(i + 1, 2 * n + 1):
            if i not in star_pos:
                star_pos[i] = []
                star_win[i] = []
            star_pos[i].append((i, j))
            star_win[i].append(winner(alice_cc(n),don_cc(n),i,j,2))
    return star_pos, star_win

def winner_count(n):
    # Initialise counts
    count0 = 0
    count1 = 0
    count2 = 0

    star_combos, star_wins = star_combinations(n)

    for key, array in star_wins.items():
        for num in array:
            if num==0:
                count0+=1
            if num==1:
                count1+=1
            if num==2:
                count2+=1
    return count0, count1, count2

def graph(steps):
    l1=[]
    l2=[]
    l3=[]
    for i in range (steps):
        l1.append(winner_count(i)[0])
        l2.append(winner_count(i)[1])
        l3.append(winner_count(i)[2])
    matplotlib.pyplot.plot(l1)
    matplotlib.pyplot.plot(l2)
    matplotlib.pyplot.plot(l3)
    matplotlib.pyplot.show()


#########################################################
# Testing the updated function
#star_combos, star_wins = star_combinations(4)
#for key, value in star_combos.items():
#    print(f"Row {key}: {value}")
#for key, value in star_wins.items():
#    print(f"Row {key}: {value}")

#print(winner(alice_kds(4),don_kds(4),2,5,1))

graph(10)






