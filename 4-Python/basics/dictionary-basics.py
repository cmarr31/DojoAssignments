'''
Assignment: Making and Reading from Dictionaries
Create a dictionary containing some information about yourself.
The keys should include name, age, country of birth, favorite language.

Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python

There are two steps to this process, building a dictionary and then gathering all the data from it. 
Write a function that can take in and print out any dictionary keys and values.

Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. 
Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application
'''
contacts = []
temp = {"name":"Anna", "age":101, "country of birth": "United States", "favorite language":"Python"}
contacts.append(temp)
temp = {"name":"Mau", "age":35, "country of birth": "Mexico", "favorite language":"JavaScript"}
contacts.append(temp)

def dictionaries(input):
    print "input = ",input
    print ""
    for i in range(len(input)):
        print "input[{}]".format(i),input[i]
        print ""
        for item in input[i]:
            print "My {} is {}".format(item, input[i][item])
        print ""
print "Making and Reading from Dictionaries"
dictionaries(contacts)