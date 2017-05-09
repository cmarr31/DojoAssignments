'''
Assignment: Dictionary in, tuples out
Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. 
Here's an example:
# function input
'''
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
'''
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
'''
print "dictionary in tuples out "
def tuples(input):
    print "input = ", input
    output = []
    for item in input:
      temp = (item, input[item])
      print "temp = ", temp
      output.append(temp)
    return output

print tuples(my_dict)