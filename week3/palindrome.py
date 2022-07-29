# Stack tall
class Stack:
    def __init__(self):
        self.Slist = []
        self.StackSize = 0

    def push(self,e):
        self.Slist.append(e)  
        self.StackSize +=1

    def pop(self):
        if self.StackSize == 0:
            return("The stack is empty")
        else:
            self.Slist.pop() 
            self.StackSize -= 1
           

    def size(self):
        return self.StackSize

    def isEmpty(self):
        if self.StackSize == 0:
            return True
        else:
            return False
    
    def peek(self):
            return self.Slist[len(self.Slist)-1]
        

#queue long
class Queue:
    def __init__(self):
        self.Qlist = []
        self.QueueLength = 0

    def enqueue(self,e):
        self.Qlist.insert(0,e)  
        self.QueueLength += 1

    def dequeue(self):
         if self.QueueLength == 0:
            return("The stack is empty")
         else:
            self.Qlist.pop() 
            self.QueueLength -= 1
        

    def length(self):
        return self.QueueLength

    def isEmpty(self):
        if self.QueueLength == 0:
            return True
        else:
            return False
    
    def peek(self):
        return self.Qlist[len(self.Qlist)-1]
        
def isPalindrome(word):   
    s=Stack()
    q=Queue()
    for letter in word.lower():
        s.push(letter)
    for letter in word.lower():
        q.enqueue(letter)
    if s.Slist == q.Qlist:
        return True
    else:
        return False
        
            
# s=Stack()  
# #push
# s.push("racecar")
# s.push("noon")
# s.push("python")
# s.push("madam")
# #pop
# s.pop()
# #stack size
# print(s.size())
# #is it empty //False
# print(s.isEmpty())
# print(s.peek())
# print(s.Slist)

# print("--------------------------------------------")
# q=Queue()
# #push
# q.enqueue("racecar")
# q.enqueue("noon")
# q.enqueue("python")
# q.enqueue("madam")
# #pop
# q.dequeue()
# #stack size
# print(q.length())
# #is it empty //False
# print(q.isEmpty())
# print(q.peek())
# print(q.Qlist)

print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))