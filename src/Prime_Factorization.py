#   n is the number to be factored
#   step by step
#   1. try dividing the n from small to big number using a while loop; n mod num == 0
#   2. store it inside the list
#   3. replace the number to be factored with the result of division
#   4. gather the number from the list and make them visibly compact
#   5. something like keep appending in another list of a string of n^n as long as there is new number
def factorization(n):
    #   original_n is created to store the initial n since n will be modified
    original_n = n
    #   all_factor_list is a list that stores all the prime factors of the given n
    all_factor_list = []
    #   the factor begins with 2 because 1 and n are not what we are looking for
    factor = 2
    #   this gate is added for a better efficiency because the factor will never have to go over n
    while factor^2 < n:
        #   as long as n mod factor is 0, the number is factor; therefore it is stored
        if n % factor == 0:
            all_factor_list.append(factor)
            n = n / factor
        else:
            factor += 1
    #   the integer converted n is stored at last because it is still one of the prime factors
    all_factor_list.append(int(n))
    n_of_unique_element = []
    #   all_factor_list must be sorted to return the result at the end succinctly
    all_factor_list.sort()
    unique_result_set = set(all_factor_list)
    for num in unique_result_set:
        i = 0
        crr_counter = 0
        #   a is simply a variable created with the pure purpose of being an iterator
        for a in sorted(all_factor_list):
            if num == all_factor_list[i]:
                crr_counter += 1
            i += 1
        n_of_unique_element.append(crr_counter)

    compact_line = ''
    unique_result_set = list(unique_result_set)

    #   string is being looped to complete the final result
    for loop in range(0, len(unique_result_set)):
        compact_line += str(unique_result_set[loop])
        compact_line += '^'
        compact_line += str(n_of_unique_element[loop])
        compact_line += ' * '

    return compact_line[:len(compact_line) - 2]


if '__main__' == __name__:
    a = factorization(36)
    print(a)