import random


def generateArray(length):
    array = []
    while len(array) <length:
        num = random.randint(0,length)
        if num not in array:
            array.append(num)
    return array


def isSorted(array):
    if array == sorted(array):
        return True

def bogoSort(array):
    iterations = 0
    while True:
        random.shuffle(array)
        if isSorted(array):
            return(f'Took {iterations} iterations. Sorting complete! {array}')
        else:
            print(array)
            iterations+=1
        


print(bogoSort(generateArray(5)))


#for mass test cases, add their iteration total to a new list, then use index to show which case goes to which.