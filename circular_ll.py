class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        tail = self.head.prev  # last node
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    # Delete node by value
    def delete(self, key):
        if self.head is None:
            return False

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if curr.next == curr:  # only one node
                    self.head = None
                else:
                    if curr == self.head:
                        self.head = curr.next
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                return True

            curr = curr.next
            if curr == self.head:
                break

        return False

    # Update node value
    def update(self, old_value, new_value):
        if self.head is None:
            return False

        curr = self.head
        while True:
            if curr.data == old_value:
                curr.data = new_value
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    # Display forward
    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=" <-> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(back to head)")

    # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head.prev  # start from tail
        while True:
            print(curr.data, end=" <-> ")
            curr = curr.prev
            if curr.next == self.head:  # stop when we come back around
                print(curr.data, end=" <-> ")
                break
        print("(back to head)")


def main():
    cll = CircularDoublyLinkedList()

    while True:
        print("\n----- Circular Doubly Linked List Menu -----")
        print("1. Insert")
        print("2. Delete")
        print("3. Update")
        print("4. Display Forward")
        print("5. Display Backward")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter value to insert: "))
            cll.insert(data)
            print("Node inserted.")
        elif choice == 2:
            key = int(input("Enter value to delete: "))
            if cll.delete(key):
                print("Node deleted.")
            else:
                print("Value not found.")
        elif choice == 3:
            old_val = int(input("Enter value to update: "))
            new_val = int(input("Enter new value: "))
            if cll.update(old_val, new_val):
                print("Node updated.")
            else:
                print("Value not found.")
        elif choice == 4:
            print("Forward Traversal:")
            cll.display_forward()
        elif choice == 5:
            print("Backward Traversal:")
            cll.display_backward()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
