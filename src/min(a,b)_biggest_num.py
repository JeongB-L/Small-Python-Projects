#   use n number of pairs of min(a, b). Then, get the biggest number possible from the sum of those pairs

#   it simply means that the result of min() should be big and the n of elements in the given list must be even
#   the smaller number in a pair has to be as big as possible ->
#   minimize the loss of bigger numbers as much as possible

#  BOOM! LET THE SMALL NUMBERS TAKE PAIR WITH SMALLER NUMBER == PAIRING IN ASCENDING OR DESCENDING ORDER THAT IS SORTED! BOOM!

def ascending_order_solution(nums):
    nums.sort()
    summation = 0
    pair = []
    for num in nums:
        pair.append(num)
        if len(pair) == 2:
            #   the pair is formed
            #   append the result of min(pair) to the sum
            summation += min(pair)
            #   reset the pair
            pair = []
    return summation

def calculating_even_numbers_solution(nums):
    nums.sort()
    summation = 0
    #   the one that is being added to the summation will always be the numbers at 2n indices
    for index, num in enumerate(nums):
        if index % 2 == 0:
            summation += num
    return summation

def good_python_way_solution(nums):
    #   [:: x] means return the number sat 2n indices
    return sum(sorted(nums)[::2])

if '__main__' == __name__:
    nums = [4, 3, 2, 1]
    print(ascending_order_solution(nums))
    print(calculating_even_numbers_solution(nums))
    print(good_python_way_solution(nums))

