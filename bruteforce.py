from itertools import combinations
import time

table = [('Action-1', 20, 5), ('Action-2', 30, 10), ('Action-3', 50, 15),
         ('Action-4', 70, 20), ('Action-5', 60, 17), ('Action-6', 80, 25),
         ('Action-7', 22, 7), ('Action-8', 26, 11), ('Action-9', 48, 13),
         ('Action-10', 34, 27), ('Action-11', 42, 17), ('Action-12', 110, 9),
         ('Action-13', 38, 23), ('Action-14', 14, 1), ('Action-15', 18, 3),
         ('Action-16', 8, 8), ('Action-17', 4, 12), ('Action-18', 10, 14),
         ('Action-19', 24, 21), ('Action-20', 114, 18)]

start_time = time.time()


def main():
    solution = bruteforce(table, 500)
    print("Best actions for 500 € :", solution[0],
          "\nTotal Cost : ", solution[1],
          "\nTotal Profit (after 2 years) : ", solution[2],
          "\nin : ", time.time() - start_time, " seconds")


def bruteforce(table_actions, max_cost):
    profit_max = 0
    best_combination = []
    for i in range(len(table_actions)):
        combinations_list = combinations(table_actions, i+1)

        for combi in combinations_list:
            total_cost = get_cost(combi)
            total_profit = get_profit(combi)

            if total_cost <= max_cost and total_profit > profit_max:
                profit_max = total_profit
                best_combination = (combi, total_cost, total_profit)
    return best_combination


def get_cost(actions):
    cost = 0
    for action in actions:
        cost += action[1]
    return cost


def get_profit(actions):
    profit = 0
    for action in actions:
        profit += action[1] * action[2] / 100
    return profit


if __name__ == "__main__":
    main()
