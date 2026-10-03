from linked_list import LinkedList

if __name__ == "__main__":
    
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    print("Original list:")
    ll.display()

    print("Recursive sum:", ll.recursive_sum())

    print("Search for 20:", ll.recursive_search(20))
    print("Search for 99:", ll.recursive_search(99))

    ll.recursive_reverse()

    print("Reversed list:")
    ll.display()