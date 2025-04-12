# LINKED LIST IMPLEMENTATION
class node:
    def __init__(self,val):
        self.data = val
        self.next = None


def insert_front(n,head):
    newnode = node(n)
    if head == None:
        head = newnode
        return head
    else:
        newnode.next = head
        head = newnode
        print(f"node {newnode.data} is inserted to the front of the list")
        return head

def insert_rear(n,head):
    newnode = node(n)
    temp = head
    if temp == None:
        temp = newnode
        print(f"node {newnode.data} is inserted to the rear of the list")
        return temp
    else:
        while temp.next != None:
            temp = temp.next
        temp.next = newnode
        print(f"node {newnode.data} is inserted to the rear of the list")
        return head

def printing(head):
    if head == None:
        print("ther are no elements in the linked list")
        return
    else:
        print("elements in the linked list are")
        temp = head
        while temp.next != None:
            print(temp.data,end='->')
            temp = temp.next
        print(temp.data,end = '->')
        print(None)
        return

def main():
    head = None
    while True:
        print("enter 1.insert front 2.insert rear 3.printing 4.end")
        choice = int(input("enter your choice"))
        if choice == 1:
            print("enter an element to insert front to list")
            n = int(input())
            head = insert_front(n,head)
        elif choice == 2:
            print("enter an element to insert front to list")
            n = int(input())
            head  = insert_rear(n,head)
        elif choice == 3:
            printing(head)
        else:
            print("stoping the operation")
            break
if __name__ == "__main__":
    main()