class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Store the data and initialize the next reference.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the front of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        """
        new_node = Node(data)
            
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        Recursively calculate the sum of all node data.
        """

        def sum_nodes(node):
            if node is None:
                return 0
            return node.data + sum_nodes(node.next)

        return sum_nodes(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list in-place using recursion.
        """

        def reverse_nodes(current, previous):
            if current is None:
                return previous

            next_node = current.next

            current.next = previous

            return reverse_nodes(next_node, current)

        # The returned node is the new head.
        self.head = reverse_nodes(self.head, None)

    def recursive_search(self, target):
        """
        Recursively search for a target value.
        """

        def search_nodes(node):
            # Base case: reached the end without finding target.
            if node is None:
                return False

            # Found the target.
            if node.data == target:
                return True

            # Search the rest of the list.
            return search_nodes(node.next)

        return search_nodes(self.head)

    def display(self):
        """
        Print the contents of the linked list.
        """
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")