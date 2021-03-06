class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        node = Node(data)
        if head is None:
            head = node
            return head
        current = head
        # current.next atau head.next itu mirip makai recursion, tapi di class.
        while current.next is not None:
            current = current.next
        current.next = node
        return head



mylist= Solution()
T=int(input())
head= None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	