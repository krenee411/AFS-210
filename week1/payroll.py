
class Employee:
    def __init__(self,fName, lName, empId, pay):
        self.fName= fName
        self.lName= lName
        self.empId= empId
        self.pay = pay

    def setfName(self,fName):
        self.fName = fName
    def getfName(self):
        return self.fName

    def setlName(self,lName):
            self.lName = lName
    def getlName(self):
        return self.lName

    def setempId(self, empId):
            self.empId = empId
    def getempId(self):
        return self.empId

    def setPay(self, pay):
            self.pay = pay
    def getPay(self):
        return self.pay



empId = int(input("Please enter the employees ID number:  "))
fName = input("Please enter the employees First Name:  ")
lName = input("Please enter the employees Last Name:  ")
pay = float(input("Please enter the employees hourly pay rate:  "))
emp_hours_worked = float(input("How many hours did " + fName + " work:  "))

#this is the math for the pay
if emp_hours_worked < 40:
    total = emp_hours_worked * pay
else:
   total = (40 * pay) + (emp_hours_worked - 40) * (pay * .50)

#stong and numbers can not concat so we have to trun the number to a string
print(fName +" "+ lName + "'s paycheck amount is: $"+ str(total))