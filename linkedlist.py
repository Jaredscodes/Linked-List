class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return ("Node({})".format(self.value))
    
    __repr__ = __str__

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    @property
    def isEmpty(self):
        return self.head == None

    def __len__(self):
        return self.count
    def  __contains__(self, value):
        current = self.head
        while current is not none:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
    
    def append(self, value):
        newNode = Node(value)
        if self.isEmpty:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.count += 1
        
            
            
        
            
        
        
