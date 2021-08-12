
def reverseLinkedList(head):
    # init values
    curr = head
    prev = None
    while True:
        tmp_curr = curr.next # None
        curr.next = prev # c
        prev = curr # d
        if tmp_curr is None:
            return curr
        curr = tmp_curr # None

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

if __name__ == "__main__":
    print("Starting")
   
    l1 = LinkedList("a")
    l1.next= l2 = LinkedList("b")
    l2.next= l3 = LinkedList("c")
    l3.next= l4 = LinkedList("d")
   
    item = l1
    while True:
        print(item.value)
        if item.next is None:
            break
        item = item.next

    item = reverseLinkedList(l1)
    print("-----\nReversed!\n----")
   
    while True:
        print(item.value)
        if item.next is None:
            break
        item = item.next