#!/usr/bin/python
#

import argparse


# take an array of prices
# [100, 200, 150, 400, 90, 600] should return 500 because buy at 100 sell at 600
# maximum profit is from a lowest price, before a highest price.
# we need to define the highest price.
# the lowest price is only the lowest prior to the highest price.
# if the stock only goes down, the highest price should be have a second highest price to determine minimum loss.
# max is determined by first number - second number. never another direction.

def find_max_profit(prices):
    max_profit = prices[1] - prices[0]

    for index, item in enumerate(prices):
        for i in prices[index + 1:]:
            if i - item > max_profit:
                max_profit = i - item

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
