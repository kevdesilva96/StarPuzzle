# Alice and Don star puzzle

# Want to visualise the Win Triangle for a given box setup of 2 by n

import numpy as np

# n=columns
def alice(n):
    arr=[x+1 for x in range(2*n)]
    return arr

def don(n):
    don_step = []
    for x in range(1, n+1):
        don_step.append(x)
        don_step.append(x + n)
    return np.array(don_step)

# Now to see the results

print(alice(4))
print(don(4))
