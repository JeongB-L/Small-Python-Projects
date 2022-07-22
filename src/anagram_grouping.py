#   anagram is a word that uses the same letter but different word from where it came from
#   it has the same key as its anagram
import collections

def grouping_anagram(input):
    input1 = list(input)
    anagrams = collections.defaultdict(list)
    for word in input1:
        #   sort the given word from the list
        #   ex) tea would be something like eat
        #   use the join() for the sole purpose of converting list to string
        #   the string we have now is a key to the anagrams list
        #   a word will then be appended to that index of the anagrams list
        anagrams[''.join(sorted(word))].append(word)
        #   ex) at the index 'eat', the word 'tea' is being stored
    return list(anagrams.values())

if '__main__' == __name__:
    a = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'tae']
    print(grouping_anagram(a))
