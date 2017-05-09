# 1 Find and Replace
'''
In this string: str = "It's thanksgiving day. 
It's my birthday,too!" print the position of the first instance of the word "day". 
Then create a new string where the word "day" is replaced with the word "month".
'''
str = "It's thanksgiving day. It's my birthday,too!"
print "1 Find and Replace = ".upper(), str
print "day = {}".format(str.find("day"))
str = str.replace("day", "month")
print "result = ",str
print " "

# 2 Min and Max
'''
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. 
Your code should work for any list.
'''
x = [2,54,-2,7,12,98]
print "2 Min and Max = ".upper(),x
print "min = {}".format(min(x))
print "max = {}".format(max(x))
print " "

# 3 First and Last
'''
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
Now create a new list containing only the first and last values in the original list. 
Your code should work for any list.
'''
x = ["hello",2,54,-2,7,12,98,"world"]
print "3 First and Last = ".upper(),x
print "first = ",x[0]
print "last = ", x[len(x) - 1]
y = x[0]
y+=x[len(x) - 1]
print "new list = ",y
print " "

# New List
'''
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
Sort your list first. 
Then, split your list in half. 
Push the list created from the first half to position 0 of the list created from the second half. 
The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 
Stick with it, this one is tough!
'''
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print "New List = ".upper(),x
x.sort()
print "sorted = ",x
first_half = x[0:len(x)/2]
print "first half = ", first_half
second_half = x[len(x)/2:len(x)]
print "second half = ", second_half
second_half.insert(0,first_half)
print "result = ",second_half