'''
Assignment: Making Dictionaries
Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. 
Assume the lists will be of equal length.
Your first function will take in two lists containing some strings. 
Here are two example lists:
'''
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
'''
Here's some help starting your function.
Hacker Challenge: If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values
'''
print "making dictionaries"
def make_dict(arr1, arr2):
    keys = []
    values = []
    if len(arr1)>=len(arr2):
        keys = arr1
        values = arr2
    else:
        keys = arr2
        values = arr1
    print keys
    print values
    new_dict = {}
    for i in range(len(keys)):
        new_dict[arr1[i]] = arr2[i]
    return new_dict
print make_dict(name, favorite_animal)