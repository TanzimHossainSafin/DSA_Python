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
    def prepend(self,value):
      newNode=Node(value)
      newNode.next=self.head
      self.head=newNode
    def Insert_After_Node(self,prev_node,data):
       if prev_node is None:
        return
       newNode = Node(data)
       newNode.next = prev_node.next
       prev_node.next = newNode
       if self.tail == prev_node:
        self.tail = newNode
a = LinkListConcept()
a.addNode(4)
a.Insert_After_Node(a.head, -7)
a.addNode(5)
a.addNode(7)
a.Insert_After_Node(a.head.next, 99)
a.PrintLinkList()