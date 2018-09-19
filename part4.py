#Hospital Management System
class Hospital:
    # Hospital class constructor to initialize the name,city and state of hospital
    def __init__(self,name, city, state):
        self.name = name
        self.city = city
        self.state = state
    # Method to print the details of Hospital;name, city and State
    def hospDetails(self):
        print(self.name, self.city, self.state)
# Class Doctor gives first and last name of the Doctor
class Doctor:
    # Doctor class constructor to initialize first and last name of doctor.
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    # Method to print out first and last name of doctors
    def doctors(self):
        print(self.fname, self.lname)
#Nurse class give the names of Nurses
class Nurse:
    # Nurse class constructor to initialize first and last name of Nurse.
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    #  Method to print first and last name of the nurse
    def nurses(self):
        print(self.fname, self.lname)
# Patient class to give names of a Patient and Admission Number.
class Patient:
    # Patient class constructor to initialize first, last name and admission Number of a Patient.
    def __init__(self, fname,lname,adm):
        self.fname = fname
        self.adm = adm
        self.lname= lname
    # Method to print patients names,first and last
    def patients(self):
        print(self.fname,self.lname,self.adm)

    #  Private Patient data member to print patient's last name and Admission number
    def __patidentity(self):
        __privPatient={self.lname:self.adm} # dictinary to hold patient last name and Admission as key,value respectively
        for key,value in __privPatient.items():
            print(key, value)
    # public method to call the private class data member(patidentity)
    def patshortcut(self):
        self.__patidentity()
# Class to give names of the hospital clerk
class AdmissionClerk:
    # AdmissionClerk class contractor;initialize first and last name of the clerk
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    # method to print ou names of hospital clerk
    def clerk(self):
        print(self.fname,self.lname)
# Class Book inherits from the parent classes Hospital and Patient; Gives the booking details: Hospital,patient and Date
class Book(Hospital,Patient):
    # Constructor initializing Book class objects
    def __init__(self,hname,hcity,hstate,pfname,plname,padm,date):
        Patient.__init__(self,pfname,plname,padm) # Invokes the parent class Patient objects
        super().__init__(hname,hcity,hstate) # initialization of parent Hospital class objects
        self.date=date
    # Book class method to display the booking details,Hospital,patient name and date
    def bookingdetail(self):
        print("HosName:",self.name,"City:",self.city,"State:",self.state,"PatientNames:",self.fname,self.lname,self.adm,"Date:",self.date)
# Class specialization which is Doctor class' child gives the doctors' area of specialization
class Specialization(Doctor):
    # specialization class constructor
    def __init__(self,fname,lname,speciality):
        super().__init__(fname,lname) # Invokes and initialize the parent class Doctor objects and methods
        self.speciality =speciality
    # Display Doctor's name and area of specialization
    def specialityinfo(self):
        print("FirstName:",self.fname,"LastName",self.lname,"Specialization:",self.speciality)
hospital = Hospital("KUMED",'Overland Park',"Kansas")
doctor=Doctor('Pat', 'Robert')
nurse=Nurse('Ali','Mohammed')
patient=Patient('nick',' Johns','301')
clerk=AdmissionClerk('Johnson','Ellena')
booking=Book(hospital.name,hospital.city,hospital.state,patient.fname,patient.lname,patient.adm,'09/26/2018')
specialdoctor=Specialization(doctor.fname,doctor.lname,"Oncology")
print("Hospital Details:")
hospital.hospDetails()
print("Doctor Details: ")
doctor.doctors()
print("Nurse Details:")
nurse.nurses()
print("Patient Full Details:")
patient.patients()
print("Patient Shortcut:Last Name and Admission Number:")
patient.patshortcut()
print("Hospital Clerk: ")
clerk.clerk()
print("Hospital Booking Details:")
booking.bookingdetail()
print("Doctors Area of Specialization:")
specialdoctor.specialityinfo()