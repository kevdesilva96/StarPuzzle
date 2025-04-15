# Alice and Don star puzzle

# Want to visualise the Win Triangle for a given box setup of 2 by n

import math

# n=columns
def alice(n):
    arr=[x+1 for x in range(2*n)]
    return arr

def don(n):
    arr=[if(x%2==0):x for x in range(2*n)]

# Now to see the results

print(alice(4))


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
