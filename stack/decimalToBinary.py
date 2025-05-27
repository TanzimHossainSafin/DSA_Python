class DecimalToBinary:
    def __init__(self,stack_array):
        self.items_stack=stack_array
    def push(self,item):
        self.items_stack.append(item)
        return item 
    def pop(self):
        pop_item=self.items_stack.pop(len(self.items_stack)-1)
        return pop_item
    def peak(self):
        return self.items_stack[(len(self.items_stack)-1)]
    def DeciToBin(self,number):
        while number>0:
         binary=number%2
         number=number//2
         self.push(binary)
    def PrintDeciToBin(self):
        binary_num=''
        for i in range(len(self.items_stack)):
            binary_num+=str(self.pop())
        return binary_num
a=DecimalToBinary([])
a.DeciToBin(242)
print(a.PrintDeciToBin())