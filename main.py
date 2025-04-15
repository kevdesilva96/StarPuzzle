# Alice and Don star puzzle

# Want to visualise the Win Triangle for a given box setup of 2 by n

# n=columns
def alice(n):
    arr=[x+1 for x in range(2*n)]
    return arr

def don(n):
    arr=[if(x%2==0):x for x in range(2*n)]

print(alice(4))
