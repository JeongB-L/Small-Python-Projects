#   return some lists consists of 3 numbers that sum up to 0
def brute_force(nums):
    #  use three different pointers i j k.
    #   there will be 3 loops that continuously find the i + j + k == 0
    #   there must be a part where it passes that loop station when there is a duplicate number with different index
    result = []
    #   sort the given list before we begin
    nums.sort()
    #   the first loop must cease when it reaches the length - 2 of the list
    #   l - 1 for the second one. the last one goes to the end
    #   without this step, array index out of range error will occur
    length = len(nums)
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            #   duplicating values can only possibly exist
            #   at the index right before the current one because the list is already sorted
            continue
        for j in range(i + 1, length - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, length):
                if k > i + 2 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    return result
    #   this method takes too much time that a timeout might occur


def two_pointer(nums):
    result = []
    nums.sort()
    length = len(nums)
    for i in range(length - 2):
        #   using two pointers can go through the entire list.
        #   작으면 왼쪽이, 크면 오른쪽이 움직이는 식으로 지속적으로 최적화되어 답을 구함
        #   in this case, the pivot i is keep moving; previous cases are being fully covered. 완전히 모든걸 커버함!
        #   declare two pointers left and right that exists in relation to i

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = length - 1
        while left < right:
            summation = nums[i] + nums[left] + nums[right]
            if summation < 0:
                left += 1
            elif summation > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                #   if there is a duplicate while moving each pointer, it should be move to the next index
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                #   even it is not duplicate, the pointers should continue moving on
                left += 1
                right -= 1
                #   two indices are moved when there was a duplicate to not do the same calculation again
    return result

if '__main__' == __name__:
    nums = [-1, 0, 1, 2, -1, -4]
    print(brute_force(nums))
    print(two_pointer(nums))
