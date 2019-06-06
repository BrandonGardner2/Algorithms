# Given an array, move all 0s within the array to the end.
# Apporach 1: Loop array once. Remove any 0s and put in a new array. Extend first array afterward.

# Approach 2: Set index 0, counter len(arr). While index < counter loop through array.
# When a 0 is found, remove it and move it to the end of the array. Change counter -= 1


def move_zeros(a):
    index = 0
    counter = len(a)

    while index < counter:
        if a[index] == 0:
            a += [a.pop(index)]
            counter -= 1
        else:
            index += 1

    return a


print(move_zeros([1, 0, 1, 1, 0, 1, 1, 1, 2, 0,
                  0, 0, 4, 5, 6, 8, 1, 12, 0, 45, 0, 3, 6]))
