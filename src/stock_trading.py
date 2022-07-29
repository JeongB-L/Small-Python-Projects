#   return the biggest profit possible by a single trading
#   each element is the point in the graph. if you buy and sell at 1, your profit is -6
def my_own_solution(prices: list[int]) -> int:
    length = len(prices)
    prices.reverse()
    profit = 0
    for i in range(length):
        for j in range(i + 1, length):
            crr = prices[i] - prices[j]
            profit = max(profit, crr)
    return profit


def brute_force(prices: list[int]) -> int:
    price = 0
    for i, crr in enumerate(prices):
        for j in range(i, len(prices)):
            price = max(prices[j] - crr, price)
    return price


if '__main__' == __name__:
    input = [7, 1, 5, 3, 6, 4]
    print(brute_force(input))
    print(my_own_solution(input))
    input.reverse()
    
    print(input)
