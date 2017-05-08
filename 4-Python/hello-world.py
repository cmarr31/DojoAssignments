'''
comment
'''
print("Hello World!")

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print("Hello, " + name + " from inside the function")
  else:
   print("No name")
# now we're unindented and have ended the previous block
print("Outside of the function")

name = "mau"

say_hello(name)

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

hw = "hello %s" % 'deprecated world'
print hw
# the output would be:
# hello deprecated world 

x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
empty_list = ninjas + my_list
empty_list.append(99)
print empty_list
print empty_list[4][2]

for val in "string":
	if val == "i":
		break
print val
  
x = 3
y = x
while y > 0:
  print y
  y = y - 1
  if y == 0:
    break
else:
 print "Final else statement"

class EmptyClass:
	pass

for val in "my_string":
	pass

x='1' 
y = 2
print x + str(y)
print str(x) + str(y)
print int(x) + y
#print x + y

x = [5,34,10,1,6]
x += [2]
print x

var = 100
if var == 200:
   print "1 - Got a true expression value"
   print var
elif var == 150:
   print "2 - Got a true expression value"
   print var
elif var == 100:
   print "3 - Got a true expression value"
   print var
else:
   print "4 - Got a false expression value"
   print var

print "Good bye!"

x=""
#if (!x) print("No x1")
if not x: 
  print("No x2")
#if x not exists:  print("No x3")

def log(i):
	print i

# tuples
x = (1,5,6,9,2)
print "len ",len(x)
print "max ",max(x)
print "min ",min(x)
print "sum ",sum(x)
print "enumerate ",enumerate(x)
print "map ",map(log,x)
print "sorted ",sorted(x)

import math
def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
	
print get_circle_area(9)
