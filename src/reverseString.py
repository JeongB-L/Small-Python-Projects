#   method that reverses the given string
#   two ways that can be done

#   first method
def reverse_string(s):
    #   index for each side of the string
    left = 0
    right = len(s) - 1
    #   the loop stops when left and right gets closer
    s = list(s)
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return "".join(s)

def reverse_string2(s):
    a = list(s)
    a.reverse()
    return "".join(a)


if '__main__' == __name__:
    s = "Very Nice Guy"
    s = reverse_string2(s)
    print(s)
