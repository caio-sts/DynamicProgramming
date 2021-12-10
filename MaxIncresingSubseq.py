import numpy as np

A = [9,	5,	6,	3,	9,	6,	4, 7]

B = [20, -30, 15, -10, 30, -20, -30, 30]

C = [-3, 2, 30, -50]

D = [-2, -1, 0, 1, 2]

def MaxLenIncreasingSubseq(A):
    ind = np.zeros(len(A), dtype= type(A))
    for i in range(0, len(A)):
        ind[i] = 1
        for j in reversed(range(0, i)):
            if A[j] <= A[i] and ind[j] + 1 > ind[i] :
                ind[i] = ind[j] + 1
    return ind

def MaxIncreasingSubseq(A):
    if len(A) <= 0 :
        return "Sequência inválida"
    else: 
        leng = max(MaxLenIncreasingSubseq(A))           

        S1 = []

        i = 0
        while i < len(A):
            S1.clear()
            S1.append(i)
            j = i+1
            while j < len(A):
                if A[j] >= A[S1[-1]] :
                    S1.append(j)    
                elif len(S1) >= 2 and A[j] >= A[S1[-2]] :
                    S1.pop()
                    S1.append(j)
                if len(S1) == leng :
                        i = len(A)
                        j = len(A)

                j = j + 1               
            
            i = i + 1
        
        S2 = []
        for i in range(0, len(S1)):
            S2.append(A[S1[i]])
            S1[i] = S1[i] + 1

    return "sequência: " + str(S2) + ", posições: " + str(S1) 

print(MaxIncreasingSubseq(A))