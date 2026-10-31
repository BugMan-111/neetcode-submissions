class MinStack:

    def __init__(self):
        # init stack object
        self.stack1 = []
        self.stack2 = []
        

    def push(self, val: int) -> None:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            # init
            self.stack1.append(val)
            self.stack2.append(val)
            return 

        self.stack1.append(val)
        if val < self.stack2[-1]:
            self.stack2.append(val)
        else:
            self.stack2.append(self.stack2[-1])


            
        

    def pop(self) -> None:
        # remove an element from the top
        self.stack1.pop(-1)
        self.stack2.pop(-1)
        

    def top(self) -> int:
        # get the value of the top
        return self.stack1[-1]
        

    def getMin(self) -> int:
        # get the minimum element from the stack
        return self.stack2[-1]
        
        
