'''
Assignment: Stars
Write the following functions.
'''
print "Stars"
'''
Part I
Create a function called draw_stars() that takes a list of numbers and prints out *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]

draw_stars(x)should print the following in when invoked:

****
******
*
***
*****
*******
*************************
'''
print "Part I"
def draw_stars1(arr):
    for num in arr:
        #print num
        stars=""
        for i in range(num):
            stars+="*" # print "*" * x
        print stars
x = [4, 6, 1, 3, 5, 7, 25]
print x
draw_stars1(x)
'''
Part II
Modify the function above. 
Allow a list containing integers and strings to be passed to the draw_stars() function. 
When a string is passed, instead of displaying *, display the first letter of the string according to the example below.
You may use the .lower() string method for this part.

For example:

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x) should print the following in the terminal:

****
ttt
*
mmmmmmm
*****
*******
jjjjjjjjjjj
'''
print "Part II"
def draw_stars2(arr):
    for item in arr:
        if type(item) == str: # isinstance(x, str):
            temp = item[0]
            temp = temp.lower()
            temp = temp * len(item)
        else:
            temp = "*" * item
        print temp
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print x
draw_stars2(x)