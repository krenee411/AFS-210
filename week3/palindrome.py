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
            self.StackSize.pop() 
            self.StackSize -= 1
            #'int' object has no attribute 'pop'

    def size(self):
        return self.StackSize

    def isEmpty(self):
        if self.StackSize == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.StackSize > 0:
            return self.Slist[-1]
        #i have no idea how to peek? maybe look at the middle of list?

    def isPalindrome(e):
        if e[0] == e[-1]:
            return isPalindrome(e[1:-1])
        else:
            return False

            #'Stack' object is not subscriptable???

s=Stack()  
#push
s.push("racecar")
s.push("noon")
s.push("python")
s.push("madam")
#pop
#print(s.pop())
#stack size
print(s.size())
#is it empty //False
print(s.isEmpty())
print(s.peek())
print(s.Slist)
#print(s.isPalindrome())

#queue long
class Queue:
    def __init__(self):
        self.Qlist = list()
        self.QueueLength = 0

    def enqueue(self,e):
        self.Qlist.append(e)  
        self.QueueLength += 1

    def dequeue(self):
         if self.QueueLength == 0:
            return("The stack is empty")
         else:
            self.QueueLength.pop() 
            self.QueueLength= list-1
        #'int' object has no attribute 'pop'

    def length(self):
        return self.QueueLength

    def isEmpty(self):
        if self.QueueLength == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.QueueLength > 0:
            return self.Qlist[-1]
        
    def isPalindrome(e):
        if e[0] == e[-1]:
            return isPalindrome(e[1:-1])
        else:
            return False
print("--------------------------------------------")
q=Queue()
#push
q.enqueue("racecar")
q.enqueue("noon")
q.enqueue("python")
q.enqueue("madam")
#pop
#print(q.dequeue())
#stack size
print(q.length())
#is it empty //False
print(q.isEmpty())
print(q.peek())
print(q.Qlist)