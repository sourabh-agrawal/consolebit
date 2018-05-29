"""
Written by sourabh agrawal
In this program i am implementing double linked list using python3 and concepts of classes
user can perform
    ->insertion at beginning
    ->insertion at end
    ->insertion at any given position

    ->deletion from beginning
    ->deletion from end
    ->deletion after any given no

    ->printing the linked list
"""


# !usr/bin/python3
class linkedlist:
    head = None

    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def insertionatfront(self, no):  # front insertion
        node = linkedlist(no)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node
            del temp

    def insertionback(self, no):  # insertion at the end
        if self.head is None:
            self.insertionatfront(no)
        else:
            node = linkedlist(no)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp
            del temp

    def insertion(self, no):  # insertion at any given position
        if self.head is None:
            self.insertionatfront(no)
        else:
            pos = int(input("Enter the no after which you want to insert this number"))
            node = linkedlist(no)
            temp = self.head
            while temp is not None and temp.value != pos:
                temp = temp.next
            node.next = temp.next
            temp.next.prev = node
            node.prev = temp
            temp.next = node
            del temp

    def deletionfront(self):  # deletion from beginning
        if self.head is None:
            print("list is already empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next.prev = self.head
            print("Node %d is deleted" % temp.value)
            del temp

    def deletionend(self):  # deletion from the end
        if self.head is None:
            print("list is already empty")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            print("Node %d is deleted" % temp.value)
            del temp

    def deletion(self):  # deletion after any given element
        if self.head is None:
            print("list is already empty")
        else:
            no = int(input("Enter the no which you want to delete"))
            temp = self.head
            while temp.next is not None and temp.value != no:
                temp = temp.next
            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            print("Node %d is deleted" % temp.value)
            del temp

    def view(self):  # printing the linked list
        temp = self.head
        print()
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print("")
        del temp


def main():
    print("Choose from the menu")
    n = 1
    l = linkedlist(0)
    while n:
        print("\nPress 1 for inserting at the beginning")
        print("Press 2 for inserting at the last")
        print("Press 3 for inserting at the position")
        print("Press 4 for delete from the beginning")
        print("Press 5 for delete from the end")
        print("Press 6 for delete from a position")
        print("Press 7 to view the linked list")
        print("press 0 for exit")
        print("press any other no to perform the operations again")
        choise = int(input("\nEnter your choise now\t"))
        if choise is 1:
            no = int(input("Enter the no to insert at the beginning"))
            l.insertionatfront(no)
        elif choise is 2:
            no = int(input("Enter the no to insert at the end"))
            l.insertionback(no)
        elif choise is 3:
            no = int(input("Enter the no to insert"))
            l.insertion(no)
        elif choise is 4:
            l.deletionfront()
        elif choise is 5:
            l.deletionend()
        elif choise is 6:
            l.deletion()
        elif choise is 7:
            l.view()
        elif choise is 0:
            break


if __name__ == '__main__':
    main()
