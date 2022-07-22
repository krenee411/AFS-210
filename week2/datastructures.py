Data1 = (7, False, "Apple", True, 7, 98.6) #Tuple
print(" ----------  Data 1 :")
print(len(Data1)) #count //6
print(Data1[3]) # fourth value // True

findSeven= 0
for n in Data1:
    if n ==7 :
        findSeven += 1

print(findSeven) #7 appears //2

#-------------------------------------------------------------------------------
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"} #Set

print(" ----------  Data 2 : ")
Data2.pop() #remove random
Data2.add("Alpha") #add Alpha
print(Data2)  #print data 

#-------------------------------------------------------------------------------
Data3 = ["A", 7, -1, 3.14, True, 7]  #List

print(" ----------  Data 3 :")
Data3.reverse()
Data3[1] = "B"
Data3.pop()
print(Data3)
#-------------------------------------------------------------------------------
Data4 ={
    " name": "Joe",
    "age": 26,   
    "active": True,  
    "hourly_wage": 14.75
} #Dictionary

print(" ----------  Data 4 :")
Data4["active"] = False
Data4["address"] = "123 West Main Street"
x=Data4.get("hourly_wage")
print(x * 40)
print(Data4)



