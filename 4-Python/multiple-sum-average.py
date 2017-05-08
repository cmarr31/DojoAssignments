'''
Assignment: Multiples, Sum, Average
This assignment has several parts. 
All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. 
Don't forget to test your code as you go!
'''
# Multiples
'''
Part I - Write code that prints all the odd numbers from 1 to 1000. 
Use the for loop and don't use a list to do this exercise.
'''
print "odd numbers from 1 to 1000".upper()
for i in range(1, 1001, 2):
    print i
print " "

'''
Part II - Create another program that prints all the multiples of 5 from 5 to 1,000.
'''
print "multiples of 5 from 5 to 1,000".upper()
for i in range(5,1001,5):
    print i
print " "

'''
Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
print "Sum List".upper()
list = [1, 2, 5, 10, 255, 3]
sum = 0
for i in list:
    sum += i
print sum
print " "

'''
Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
print "Average List".upper()
print sum/len(list)