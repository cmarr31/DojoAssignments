'''
Assignment: Names
Write the following function.
'''
print "Names"
'''
Part I
Given the following list:
'''
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
'''
Create a program that outputs:
Michael Jordan
John Rosales
Mark Guillen
KB Tonel
'''
def print_names(arr):
    for item in arr:
        print item["first_name"] + " " + item["last_name"]
print "Part I"
print_names(students)
print " "
'''
Part II
Now, given the following dictionary:
'''
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
'''
Create a program that prints the following format (including number of characters in each combined name):
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. 
Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.
'''
def print_names_and_numbers(dictionary):
    for category in dictionary:
        print category
        i = 0
        for contact in dictionary[category]:
            # print "contact = ", contact
            i = i +1
            temp = contact["first_name"] + " " + contact["last_name"]
            temp = temp + " " + str(len(temp)-2)
            print str(i) + " - " + temp
print "Part II"
print_names_and_numbers(users)