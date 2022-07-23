#	sum of two numbers
def two_sum(num: list[int], target: int) -> list[int]:
	length = len(num)
	for a in range(0, length):
		for b in range(a + 1, length):
			if num[a] + num[b] == target:
				return [a, b]
				
def two_sum1(nums, target) -> list[int]:
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]

def two_sum2(nums, target):
	for i, n in enumerate(nums):
		#	n is the value and i is the index
		complement = target - n
		if complement in nums[i + 1:]:
			#	if the complement exists, then the sum number exists as well
			print(nums.index(n))
			print(nums[i +1:].index(complement))
			#	return the index of each value
			return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
			
def two_sum3(nums, target):
		#	uses dictionary in this case.
		#	best time complexity because dictionary is faster
		nums_map = {}
		#	store the key and the value in opposite direction
		for i, num in enumerate(nums):
			nums_map[num] = i
			#	{key : value}
		for i, num in enumerate(nums):
			#	check if the complement exists in the map, 
			#	check if the index 
			if target - num in nums_map and i != nums_map[target - num]:
				#	1, 2, 3, 4 target= 7
				#	i = 2, nums_map[4] = 3, 
				#	second statement exists to check if the complement is not the complement by itself, even they are same number, index must be different
				return [i, nums_map[target - num]]
				
def two_sum3(nums, target):
		#	use only a single for loop
		nums_map = {}
		for i, num in enumerate(nums):
			if target - num in nums_map:
				return [nums_map[target - num], i]
			nums_map[num] = i
			#	even the target is the complement of the last and the first element, it works anyway
		
if __name__ == '__main__':
	num = [1,2,3,4,5]
	target = 6
	print(two_sum3(num, target))