class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class CreateLinkList:
    def __init__(self,array):
        self.array=array
    def addLinklist(self):
         newNode=Node(self.array[0])
         self.head=newNode
         self.tail=self.head
         temp=self.head
         for i in range(1,len(self.array)):
            newNode=Node(self.array[i])
            temp.next=newNode
            self.tail=newNode
            temp=temp.next
    def PrintLinklist(self):
        if self.head is None:
            print('Empty LinkList!')
        numberString=''
        temp=self.head
        while temp is not None:
            numberString+=str(temp.value)+','
            temp=temp.next
        print(numberString[:-1])
    def DeleteHead(self):
        if self.head is None:
         return None 
        temp=self.head
        self.head=temp.next
        temp.next=None
        return temp.value
a=CreateLinkList([1,2])
a.addLinklist()
a.PrintLinklist()
print(a.DeleteHead())
a.PrintLinklist()