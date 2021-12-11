import numpy as np

# sample set
P = [2, 3, 5, 7, 10]

# Target value
alvo = 19


def subsetsum(vect, tgt):
    memo = np.zeros((len(vect), 1 + tgt))  # memoization table

    for lin in range(len(vect)):
        memo[lin][0] = 1  # always possible to make 0 weight subset

    memo[0][vect[0]] = 1

    for lin in range(1, len(memo)):
        for col in range(1, len(memo[0])):
            if vect[lin-1] > col or memo[lin-1][col] == 1:
                memo[lin][col] = memo[lin-1][col]
            elif memo[lin-1][col] == 0:
                actsum = col - vect[lin]
                memo[lin][col] = memo[lin-1][col - vect[lin]]

    if memo[len(vect)-1][len(memo[0])-1] == 1:
        i = len(memo)-1  # quantity of objects
        j = len(memo[0])-1  # maximum weight
        listItems = []

        while i > 0 and j > 0:
            if memo[i][j] != memo[i - 1][j]:
                listItems.append(vect[i])
                j -= vect[i]
                print(j)
                i -= 1
            else:
                i -= 1

        if j == vect[0]:
            listItems.append(vect[0])

        listItems.reverse()

        return "Lista dos itens: {}\nValor máximo possível: {}".format(listItems, tgt)
    else:
        return "Não há subconjunto em {} cuja soma é {} ".format(vect, tgt)


print(subsetsum(P, alvo))