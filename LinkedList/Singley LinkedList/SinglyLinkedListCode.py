""" Singley Linked List """

class Node:
    def __init__(self, iteam=None, next=None):
        self.iteam = iteam
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        if self.start == None:
            return True
        return False 

    def insert_at_start(self, data=None):
        # create node
        n = Node(data, self.start)
        # this code works for both the cases empty list as well as non-empty list
        self.start = n

    def insert_at_last(self, data=None):
        n = Node(data)
        # if list is not empty
        if not self.is_empty():
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = n
        else:
            # if list is empty
            self.start = n

    def search(self, data):
        temp = self.start
        while(temp != None):
            if data == temp.iteam:
                return temp
            temp = temp.next
        # search fail / empty list
        return None
    
    def print_list(self):
        temp = self.start
        while(temp != None):
            print(temp.iteam, end=' ')
            temp = temp.next

# Driver Code
mylist = SLL()
mylist.insert_at_start(23)
mylist.insert_at_last(78)
mylist.insert_at_start(89)
mylist.print_list()



