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
a=Concept([2,5,8])
a.push(6)
print("peek item is now",a.peek())
print(a.items_stack)
print(a.pop())
print(a.items_stack)
print("peek item is now",a.peek())
