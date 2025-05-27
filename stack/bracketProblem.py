class Concept:
    def __init__(self,stack_array):
        self.items_stack=stack_array
    def push(self,item):
        self.items_stack.append(item)
        return item 
    def pop(self):
        pop_item=self.items_stack.pop(len(self.items_stack)-1)
        return pop_item
    def peek(self):
        return self.items_stack[(len(self.items_stack)-1)]
    def check_bracketBalance(self,bracket):
     for i in range(len(bracket)):
        if bracket[i] == " ":
            continue 
        if bracket[i] in "({[":
           self.items_stack.append(bracket[i])
        else:
           if len(self.items_stack) == 0:
            return "Imbalanced"
           match=self.peek()
           if(match)=='(' and bracket[i]==')' or (match)=='{' and bracket[i]=='}' or (match)=='[' and bracket[i]==']':
              self.pop()
           else:
            return "Imbalanced"
     if len(self.items_stack)==0:
        return "Balanced"
     else:
        return "Imbalanced"
a=Concept([])
print(a.check_bracketBalance("{ {{  }"))


            

