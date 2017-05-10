print "Assignment: Hospital"
'''
Patient:
- Attributes: Id: an id number, Name, Allergies, Bed number: should be none by default
Hospital
- Attributes: Patients: an empty array, Name: hospital name, Capacity: an integer indicating the maximum number of patients the hospital can hold.
- Methods:
--Admit: add a patient to the list of patients. Assign the patient a bed number. 
    If the length of the list is >= the capacity do not admit the patient.
    Return a message either confirming that admission is complete or saying the hospital is full.
--Discharge: look up and remove a patient from the list of patients. 
    Change bed number for that patient back to none.
'''
class Patient(object):
    def __init__(self, id_number, name, allergies, bed_number = 0):
        self.id = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
    def display_all(self):
        print "ID:", self.id
        print "Name:", self.name
        print "Allergies:", self.allergies
        print "Bed Number:", self.bed_number
        print " "
class Hospital(object):
    def __init__(self, patients, name, capacity = 3):
        self.patients = patients
        self.name = name
        self.capacity = capacity
        self.occupancy = len(self.patients)
        self.beds = [5]
    def admit(self, patient):
        if self.occupancy < self.capacity:
            self.patients.append(patient) # Add a patient to the list of patients. 
            #self.queue_size = len(self.calls)
            print "admited"
            self.occupancy += 1
            # Assign the patient a bed number. 
            # If the length of the list is >= the capacity do not admit the patient.
            # Return a message either confirming that admission is complete or saying the hospital is full.
        else:
            print "rejected"
        return self
    def discharge(self, patient):
        print "discharged"
        self.occupancy -= 1
        self.patients.pop(0) # Discharge: look up and remove a patient from the list of patients.
        # Change bed number for that patient back to none.
        return self
    def display_all(self):
        print "Patients:", len(self.patients)
        print "Name:", self.name
        print "Capacity:", self.capacity
        print "Occupancy:", self.occupancy
        print " "
        return self
print " "
p1 = Patient(1, "Mau", "most drugs").display_all()
p2 = Patient(2, "Alex", "apples").display_all()
p3 = Patient(3, "Santi", "sugar").display_all()
p4 = Patient(4, "Gerardo", "none").display_all()
h = Hospital([p1, p2, p3],"General Hospital").display_all().admit(p4).display_all().discharge(p1).display_all().admit(p4).display_all()