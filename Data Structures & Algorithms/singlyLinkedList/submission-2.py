class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head=None
    
    def get(self, index: int) -> int:
        temp=self.head
        i=0
        while temp!=None:
            if(i==index):
                return temp.value
            i+=1
            temp=temp.next
        return -1

    def insertHead(self, val: int) -> None:
        node=Node(val)
        node.next=self.head
        self.head=node

    def insertTail(self, val: int) -> None:
        node=Node(val)
        temp=self.head
        prev=None
        if temp==None:
            self.head=node
        else:
            while(temp!=None):
                prev=temp
                temp=temp.next
            prev.next=node

    def remove(self, index: int) -> bool:
        temp=self.head
        i=0
        prev=None
        if index==0 and temp!=None:
            self.head=temp.next
            return True
        else:
            while temp!=None:
                if index==i:
                    prev.next=temp.next
                    return True
                prev=temp
                temp=temp.next
                i+=1
        return False
    def getValues(self) -> List[int]:
        arr=[]
        temp=self.head
        while temp!=None:
            arr.append(temp.value)
            temp=temp.next
        return arr