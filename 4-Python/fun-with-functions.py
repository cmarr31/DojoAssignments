'''
Assignment: Fun with Functions
Create a series of functions based on the below descriptions.
'''
print "Fun with Functions"
'''
Odd/Even:  Create a function called odd_even that counts from 1 to 2000. 
As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.
Your program output should look like below:
Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.
'''
def odd_even(start,end):
    for i in range(start, 1+end):
        if i % 2 == 0:
            print "Number is {}. This is an even number".format(i)
        else:
            print "Number is {}. This is an odd number".format(i)
print "Odd/Even"
odd_even(1, 200)
'''
Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
and returns a list where each value has been multiplied by 5.

The function should multiply each value in the list by the second argument. 
For example, let's say:

a = [2,4,10,16]

Then:

b = multiply(a, 5)
print b

Should print [10, 20, 50, 80 ].
'''
def multiply(input,num):
  output = input
  for i in range(0,len(input)):
    output[i]=output[i]*num
  return output

a = [2,4,10,16]
print "array = ",a
b = multiply(a, 5)
print "multiply = ",b
'''
Hacker Challenge:
Write a function that takes the multiply function call as an argument. 
Your new function should return the multiplied list as a two-dimensional list. 
Each internal list should contain the number of 1's as the number in the original list. 
Here's an example:

def layered_multiples(arr)
  # your code here
  return new_array
x = layered_multiples(multiply([2,4,5],3))
print x
# output
>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
'''
def layered_multiples(arr):
  new_array=[] 
  print arr #6,12,15
  for num in arr: 
    temp=[]
    for i in range(0,num):
      temp.append(1)
    new_array.append(temp)
  return new_array
print "Hacker Challenge"
x = layered_multiples(multiply([2,4,5],3))
print x