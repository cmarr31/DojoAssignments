'''
Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, 
and prints a new list of all the strings containing that character.

Here's an example:

# input
l = ['hello','world','my','name','is','Anna']
char = 'o'
# output
n = ['hello','world']

Hint: how many loops will you need to complete this task?
'''
def find_characters(list,character):
	output = []
	for i in list:
		if character in i:
			output.append(i)
	print output

# test
l = ['hello','world','my','name','is','Anna']
print "list ",l
char = 'o'
print "character ",char
find_characters(l,char)
print " "
# test
l = ['hello','world','my','name','is','Anna']
print "list ",l
char = 'a'
print "character ",char
find_characters(l,char)

