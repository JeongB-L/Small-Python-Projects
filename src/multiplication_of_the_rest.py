#   given a list, return the results of all multiplications for all the numbers except the current output[i]
#   WARNING : do not use division for solving this problem

def my_own_solution1(nums: list[int]):
    #   assuming there is no duplicate
    temp = []
    mul = 1
    result = []
    for i in range(len(nums)):
        crr = nums[i]
        for j in range(len(nums)):
            if nums[j] != crr:
                temp.append(nums[j])
        for element in temp:
            mul *= element
        result.append(mul)
        #   reset the temporarily used variables
        mul = 1
        temp = []
    return result

def my_own_solution_with_no_assumption(nums: list[int]):
    #   the only difference is that I must distinguish whether it is at the current index by index
    mul = 1
    result = []
    temp = []
    length = len(nums)
    for i in range(length):
        for j in range(length):
            if j != i:
                temp.append(nums[j])
        for element in temp:
            mul *= element
        result.append(mul)
        mul = 1
        temp = []
    return result

def multiply_left_and_right(nums: list[int]) -> list[int]:
    #   multiply the result of the multiplication from left and right except myself
    #   the multiplication of every number except output[i] means each element is not added by once
    #   1 -> 1 -> 2 -> 6
    #   24   12   4   1
    out = []
    crr = 1
    for i in range(len(nums)):
        out.append(crr)
        crr *= nums[i]
    crr = 1
    #   (len(nums) - 1, -1, -1) means it goes to the opposite direction
    temp = []
    for i in range(len(nums) - 1, -1, -1):
        #   multiplied ones from the right side are multiplied to the ones from the left side
        out[i] *= crr
        crr *= nums[i]
        #       #   깨달음: multiplying left and right is simple: a1 * a2 * a3 ... ai... * a(i + 1) * ... an
        #                   left side of the calculation is done in the first step, then the calculation
        #                   on the other side is done, which is just multiplying them, so that theres no difference
        #                   between brute forcing and this. 그냥 말 그대로 곱하면 왼쪽은 본인을 제외한 모든 수의 곱이고
                        #   오른쪽도 마찬가지. cum sum의 개념 사용. 왼쪽 애들로 "만" 곱한거를 나중에 오른쪽 애들로 "만" 곱한걸
                #           곱해줬을 뿐.  cum sum 으로 2개의 숫자를 이미 곱함 -> 나머지 1개랑 그냥 1 을 곱해줌
        #   QED
    return out

def test(input):
    temp = []
    #   the closing bound is -1 because if 0 then it won't include the 0th index
    for i in range(len(input) - 1, -1, -1):
        temp.append(i)
    return temp
if '__main__' == __name__:
    input = [1, 2, 3, 4]
    print(my_own_solution1(input))
    print(my_own_solution_with_no_assumption(input))
    print(multiply_left_and_right(input))


