'''
Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, 
based on that element's data type.
Your program input will always be a list. 
For each item in the list, test its data type. 
If the item is a string, concatenate it onto a new string.
If it is a number, add it to a running sum. 
At the end of your program print the string, the number and an analysis of what the array contains. 
If it contains only one type, print that type, otherwise, print 'mixed'.
Here are a couple of test cases. 
Think of some of your own, too. 
What kind of unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The array you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# input
l = [2,3,1,7,4,12]
#output
"The array you entered is of integer type"
"Sum: 29"

# input
l = ['magical','unicorns']
#output
"The array you entered is of string type"
"String: magical unicorns"
'''
def type_list(input):
    sum = 0
    strings = ""
    types = []
	# Your program input will always be a list
    for i in input:
        if type(i) not in types:
            types.append(type(i))
        if type(i) is str:
			# If the i is a string, concatenate it onto a new string.
            strings += i
        if type(i) is int or type(i) is float:
			# If it is a number, add it to a running sum
            sum += i
	# At the end of your program print the string, the number and an analysis of what the array contains. 
	# If it contains only one type, print that type, otherwise, print 'mixed'.
    print "Strings:", strings
    print "Sum:", sum
    if len(types) == 1:
        typeString = "string"
        if types[0] is float:
            typeString = "float"
        elif types[0] is int:
            typeString = "integer"
        elif types[0] is list:
            typeString = "list"

        print "The array you entered is of", typeString, "type"
    else:
        print "The array you entered is of mixed type"

# test mixed
l = ['magical unicorns',19,' hello',98.98,' world']
print l
type_list(l)
print " "

# test integer
l = [2,3,1,7,4,12]
print l
type_list(l)
print " "

# test list
l = [['list','list']]
print l
type_list(l)
print " "

# test string
l = ['magical',' unicorns']
print l
type_list(l)
print " "

# test float
l = [2.3,1.7,4.12]
print l
type_list(l)