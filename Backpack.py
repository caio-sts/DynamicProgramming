#Binary Knapsack // 0-1 Knapsack // Mochila binária

import numpy as np

Wmax = 5
V = [100, 20, 60, 40]
W = [3, 2, 4, 1]


def backpack(wtmax, w, v):
    memo = np.zeros((len(w) + 1, wtmax + 1))

    for lin in range(1, len(memo)):
        for col in range(1, len(memo[0])):
            if w[lin - 1] > col:
                memo[lin][col] = memo[lin-1][col]
            elif w[lin-1] <= col:
                memo[lin][col] = max(memo[lin-1][col], v[lin-1] + memo[lin-1][col - w[lin-1]])

    maxVal = memo[len(memo)-1][len(memo[0])-1]  # maximum value into the knapsack

    i = len(memo)-1  # quantity of objects
    j = len(memo[0])-1  # maximum weight
    listItems = []
    while i > 0 and j > 0:
        if memo[i][j] != memo[i-1][j]:
            listItems.append(i)
            j -= w[i-1]
            i -= 1
        else:
            i -= 1
    listItems.reverse()

    return "Lista dos itens: {}\nValor máximo possível: {}".format(listItems, maxVal)


print(backpack(Wmax, W, V))
