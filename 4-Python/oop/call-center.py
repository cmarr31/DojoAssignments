print "Assignment: Call Center"
'''
You're creating a program for a call center. 
Every time a call comes in you need a way to track that call. 
One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
You will create two classes. 
One class should be Call, the other CallCenter.
Call():
Create your call class with an init method. Each instance of Call() should have a few attributes:
- unique id
- caller name
- caller phone number
- time of call
- reason for call
The call class should have a display method that prints all call attributes.
'''
class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display_all(self):
        print "Unique ID:", self.unique_id
        print "Caller Name:", self.caller_name
        print "Caller Phone #:", self.caller_phone_number
        print "Time of Call:", self.time_of_call
        print "Reason for Call:", self.reason_for_call
        return self
''' CallCenter():
Create your call center class with an init method. 
Each instance of CallCenter() should have the following attributes:
- calls: should be a list of call objects
- queue size: should be the length of the call list
The call center class should have an add method that adds a new call to the end of the call list
The call center class should have a remove method that removes the call from the beginning of the list (index 0).
The call center class should have a method called info that shows the name and phone number for each call in the queue as well as the length of the queue.
'''
class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.queue_size = len(self.calls)
    def add(self, call):
        self.calls.append(call)
        self.queue_size = len(self.calls)
        return self
    def remove(self):
        self.calls.pop(0)
        return self
    def info(self):
        print "Queue length:", self.queue_size
        for call in self.calls:
            print call.time_of_call, call.caller_phone_number, call.caller_name
    def remove_call_by_number(self, phone_number):
        for call in self.calls:
            if call.caller_phone_number == phone_number:
                self.calls.remove(call)
                return self
    def sort_calls_by_time(self):
        self.calls = sorted(self.calls, key=lambda call: call.time_of_call)
        return self
'''
You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
'''
call1 = Call(1, "Mau", "312-000-9999", "08:30", "first")
call2 = Call(2, "Alex", "512-999-0000", "12:00", "lunch")
call3 = Call(3, "Santi", "999-000-1234", "17:00", "dinner")
call4 = Call(4, "Ninja", "999-999-9999", "10:30", "snack")
call5 = Call(5, "Hacker", "000-000-0000", "14:30", "snack")
center = CallCenter([call1, call2, call3])
print " "
center.add(call4)
center.add(call5)
center.info()
print " "
'''
Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
'''
center.remove_call_by_number("312-000-9999")
center.info()
print ""
'''
Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? 
Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
'''
center.sort_calls_by_time()
center.info()