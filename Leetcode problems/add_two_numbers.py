class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def reverse(self,l1):
        temp = self.head
        while temp:
            temp.next = self.head
            self.head =    
    
    
    
    def addTwoNumbers(self, l1, l2):
        res = ListNode()
        curr = res
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry 
            carry = val //10
            val = val % 10  
            curr.next = ListNode(val)
            
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return res.next
            
l1 = ListNode(3)
l1.next = ListNode(4)
l1.next.next = ListNode(2)

l2 = ListNode(4)
l2.next = ListNode(6)
l2.next.next = ListNode(5)

obj = LinkedList()
result = obj.addTwoNumbers(l1,l2)    

while result != None:
    print(result.val)
    result = result.next


