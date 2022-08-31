import sys
import time

import dataReader

start_time = time.time()


def main():
    try:
        datafile = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("\n File not found.")
        sys.exit()

    data = dataReader.reader(datafile)
    solution = knapsack(50000, data)
    cost = []
    for i in solution[1]:
        cost.append(i[1] / 100)
    print("Best actions for 500 € :", solution[0],
          "\nTotal Cost : ", sum(cost),
          "\n with : ", solution[1],
          "\n in : ", time.time() - start_time, " seconds")


def knapsack(max_cost, data):
    matrix = [[0 for x in range(max_cost + 1)] for x in range(len(data) + 1)]

    for i in range(1, len(data) + 1):
        for w in range(1, max_cost + 1):
            if data[i - 1][1] <= w:
                matrix[i][w] = max(data[i - 1][2] + matrix[i - 1][w - data[i - 1][1]], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]

    w = max_cost
    n = len(data)
    best_combination = []

    while w >= 0 and n >= 0:
        e = data[n - 1]
        if matrix[n][w] == matrix[n - 1][w - e[1]] + e[2]:
            best_combination.append(e)
            w -= e[1]

        n -= 1

    return matrix[-1][-1], best_combination


if __name__ == "__main__":
    main()

