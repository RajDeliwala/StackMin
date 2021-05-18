'''
Cracking the coding interview
Chapter 3 - Stacks and Queues
Stacks and Queues: Stack Min
----------------------------------------
Question: How would you design a stack which, in addition to push and pop
, has a function min which returns the minimum element
Push, Pop, and Min should all operate in O(1)

Example: 
input: 
output: 
Constraits or Questions you need to ask:
Solution notes:
Create a custom class for stack in which we can make custom functions for 
Push Pop and Min that all run in constant time
We have to deal with a more space complex solution if we want a constant time 
create another list to constantly compare with whenever we append to the main list
this way we're constantly aware of the lowest elemnt by saving it in the min stack
'''

class Stack:
    def __init__(self):
        #Using a list for the stack
        self.stackdata = []
        self.minStack = []
        self.size = 0

    #Add to the list in O(1)
    def push(self, data):
        if self.size == 0:
            self.minStack.append(data)
        else:
            if data <= self.minStack[-1]:
                self.minStack.append(data)
        self.stackdata.append(data)
        self.size += 1
            
    #Pop from the list in O(1)
    def pop(self):
        temp = self.stackdata.pop()
        self.size -= 1
        if temp == self.minStack[-1]:
            self.minStack.pop()


    def min(self):
        return self.minStack[-1]

stack = Stack()

stack.push(1)
stack.push(15)
stack.push(20)
stack.push(25)
stack.push(30)

popped = stack.min()
print("The minimum element is ", popped)
