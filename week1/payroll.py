
class Employee:
    def __init__(self,fName, lName, empId, empPay):
        self.fName= fName
        self.lName= lName
        self.empId= empId
        self.empPay = empPay
        # self.total = total

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

    def setempPay(self, empPay):
            self.empPay = empPay
    def getempPay(self):
        return self.empPay

    # def setTotal(self, total):
    #         self.total = total
    # def getTotal(self):
    #     return pay(self.total)


empId = int(input("Please enter the employees ID number:  "))
fName = input("Please enter the employees First Name:  ")
lName = input("Please enter the employees Last Name:  ")
empPay = float(input("Please enter the employees hourly pay rate:  "))
emp_hours_worked = float(input("How many hours did " + fName + " work:  "))

#this is the math for the pay
def pay():
    if emp_hours_worked <= 40:
        print(fName +" "+ lName + "'s paycheck amount is: $"+ str(emp_hours_worked * empPay))
    else:
        print(fName +" "+ lName + "'s paycheck amount is: $" + str((40 * empPay) + (emp_hours_worked - 40) * (empPay * 1.5)))

pay()
#stong and numbers can not concat so we have to trun the number to a string
# print(fName +" "+ lName + "'s paycheck amount is: $" + str(pay()))
