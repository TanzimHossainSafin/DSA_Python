class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkListConcept:
    def __init__(self):
      self.head=None
      self.tail=self.head
    def addNode(self,value):
       newNode=Node(value)
       if self.head is None:
          self.head=newNode
          self.tail=newNode
       else:
          temp=self.tail
          temp.next=newNode
          self.tail=temp.next   
    def PrintLinkList(self):
       temp=self.head
       while temp!=None:
          print(temp.value)
          temp=temp.next
a=LinkListConcept()
a.addNode(4)
a.addNode(5)
a.addNode(7)
a.PrintLinkList()