Data1 = (7, False, "Apple", True, 7, 98.6) #Tuple
print(" ----------  Data 1 :")
print(len(Data1)) #count 
print(Data1[3]) # fourth value 

findSeven= 0
for n in Data1:
    if n ==7 :
        findSeven += 1

print(findSeven) #7 appears

#-------------------------------------------------------------------------------
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"} #Set

print(" ----------  Data 2 : ")
Data2.pop() #remove random
Data2.add("Alpha") #add Alpha
print(Data2)  #print data 

#-------------------------------------------------------------------------------
Data3 = ["A", 7, -1, 3.14, True, 7]  #List

print(" ----------  Data 3 :")
Data3.reverse()  # reverse
Data3[1] = "B" #replace second value
Data3.pop()  #remove last item
print(Data3)  #print
#-------------------------------------------------------------------------------
Data4 ={
    " name": "Joe",
    "age": 26,   
    "active": True,  
    "hourly_wage": 14.75
} #Dictionary

print(" ----------  Data 4 :")
Data4["active"] = False  #change active to False
Data4["address"] = "123 West Main Street"  #add Address
x=Data4.get("hourly_wage") #get hourly_wage from dictionary 
print(x * 40)  # get pay for 40 hours
print(Data4)  #print



