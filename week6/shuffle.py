# random-shuffle
from random import randint

# now for some reason this does not always run as expected?? you can run it a few times and it works
# but then it give me IndexError: list index out of range sometimes? Please Help


def randomizer(myList,n):
    for i in range(0,n-1):
        ran = randint(0 ,n)
        if i != ran:
            myList[i], myList[ran] = myList[ran],myList[i]
            return randomizer(myList,n)
        return myList

myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
n = len(myList)
print("Before Shuffle:")
print(myList)
print("After shuffle:")
print(randomizer(myList,n))

#line 8: myList is len(10) so we go from 0 to 10-1 because we do not want to use the same number twice
#line 9: this is giving me a random number between 1-10 which is any number in my array
#line 10: if the number chosen does not match the number picked at random 
#line 11: swap the two numbers 
#line 12: this keeps calling the function until there are no numbers left to call/swap


# print("___________________________________")


# def randomm(myList,n):
#     for i in range(0,n-1):
#         r = randint(0,n)
#         myList[i],myList[r]= myList[r],myList[i]
#         return myList

# myList = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
# n = len(myList)

# print("Before Shuffle:")
# print(myList)
# print("After shuffle:")
# print(randomm(myList,n))