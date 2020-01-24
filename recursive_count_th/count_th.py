'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # declare counter variable
    counter = 0

    # define base cases
    if len(word) <= 1:
        return 0

    # counter function
    def counter_func(counter):
        return counter + 1

    # recur
    if 'th' in word:
        return count_th(word.replace('th', ' ', 1)) + counter_func(counter)
    else:
        return counter

print(count_th('thhtthht'))

test = 'thhtthht'
print(test.replace('th', '', 2))