#   calculate the possible amount of water after the rain in a given height

#   using two pointer
def amount_of_rain1(height) -> int:
    #   regardless of each height, they just work as a wall between left and right
    #   starts from each end side, they eventually meet at the highest point
    if not height:
        return 0
    water = 0
    left = 0
    right = len(height) - 1
    #   current max height are selected to be the beginnings
    left_max = height[left]
    right_max = height[right]
    while left < right:
        #   loop until they meet each other

        #   renew the maximum everytime to get the volume of the water remaining
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)
        if left_max <= right_max:
            water += left_max - height[left]
            left += 1
        else:
            water += right_max - height[right]
            right -= 1
    return water

#   use stack in this case. it is still an O(n) solution
def amount_of_rain2(height) -> int:
    #   stack will store the values that are bigger than the previous ones
    stack = []
    water = 0
    length = len(height)
    for i in range(length):
        #   when it faces the inflection point, where it is higher than the previous height
        while stack and height[i] > height[stack[-1]]:
            #   while stack is not empty and if the crr value is higher than the previous value which is in stack
            #   the top value is gone and now stored to top
            
            #   take out the currently highest one
            top = stack.pop()
            if not len(stack):
                #   break if there's nothing in the stack
                break
            #   get the distance between the current one and subtract the crr to previous highest to 1; the width of that block of water
            width = i - stack[-1] - 1
            #   now waters is the height of that block
            waters = min(height[i], height[stack[-1]], height[top])
            #   now get the surface area of that block
            water += width * waters
        #   append the big ones that were bigger than the previous blocks
        stack.append(i)
    return water


if '__main__' == __name__:
    rain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(amount_of_rain2(rain))
