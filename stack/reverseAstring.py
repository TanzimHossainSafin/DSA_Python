class ReverseString:
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
    def reverse_string(self,string_name):
        for i in range(len(string_name)):
            self.push(string_name[i])
    def printReverseString(self):
        word=''
        for i in range(len(self.items_stack)):
            word+=self.pop()
        return word
a=ReverseString([])
a.reverse_string("h e l l o")
print(a.printReverseString())
