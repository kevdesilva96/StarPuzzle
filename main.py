# Alice and Don star puzzle

# Want to visualise the Win Triangle for a given box setup of 2 by n

import numpy as np

import math

# n=columns
def alice(n):
    arr=[x+1 for x in range(2*n)]
    return np.arr

def don(n):
    don_step = []
    for x in range(1, n+1):
        don_step.append(x)
        don_step.append(x + n)
    return np.array(don_step)




# Function to weave two arrays together
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

def don_kds(n):
    arr1=[x+1 for x in range(n)]
    arr2=[x+n+1 for x in range(n)]
    return (weave(arr1,arr2))

# Function to return first occurence of iten in list
def first_pos(arr,item):
    for i in range(len(arr)):
        if arr[i]==item:
            return i
            quit


# Function to take two arrays and return who wins (given star pos and option for first or both)
def winner(arr1,arr2,star1,star2,win_option=1):

    # Initialise output positions
    arr1_pos=0
    arr2_pos=0

    # Looking for first star only
    if win_option==1:
        for i in range(len(arr1)):
            if arr1[i]==star1 or arr1[i]==star2 and arr1_pos==0:
                arr1_pos=i
        for i in range(len(arr2)):
            if arr2[i]==star1 or arr2[i]==star2 and arr2_pos==0:
                arr2_pos=i
        if arr1_pos<arr2_pos:
            winner="first"
        elif arr2_pos<arr1_pos:
            winner="second"
        else:
            winner="tie"
        return winner
    # Looking for both stars
    elif win_option==2:
        return True
    else:
        return "Invalid winner_option: Select 1 for first start, 2 for both stars"

