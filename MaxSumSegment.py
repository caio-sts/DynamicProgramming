import numpy as np

A = [20, -30, 15, -10, 30, -20, -30, 30]

B = [-3, 2, 30, -50]

C = [-2,-1,0,1,2]

def maxSumSegment(A):
    if len(A) <= 0 :
        return "Sequência inválida"
    else: 
        S = np.zeros(len(A), dtype= type(A))
        S[0] = A[0]
        begin = 1
        final = len(A) - 1

        for i in range(1, len(A)):
            S[i] = A[i]
            if S[i-1] >= 0 :
                S[i] = S[i] + S[i-1]

        bigSum = S[0]
        for j in range(1, len(A)):
            if S[j] >= bigSum :
                final = j + 1 
                bigSum = S[j]
            if S[j-1] < 0 and j < final :
                begin = j+1

    return "maxSum: "+str(bigSum)+", initial position: "+str(begin)+", final position: "+str(final)

print(maxSumSegment(C))