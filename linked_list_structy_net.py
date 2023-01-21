class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("F")

a.next = b
b.next = c
c.next = d
d.next = e

a2 = Node("Q")
b2 = Node("R")
a2.next = b2


def traversal_linked_list_iterative(head):
    current = head
    while current != None:
        print(current.val)
        current = current.next
def traversal_linked_list_recursive(head):
    if head == None:
        return 
    print(head.val)
    traversal_linked_list_recursive(head.next)
def sum_linked_list_iterative(head):
    current = head
    sum = 0
    while current != None:
        sum += current.val
        current = current.next
    return sum
def sum_linked_list_recursive(head):
    if head == None:
        return 0
    return head.val + sum_linked_list_recursive(head.next)


def find_linked_list_iterative(head, target):
    current = head
    while current !=None:
        if current.val == target:
            return True
        current = current.next
    return False
def find_linked_list_recursive(head, target):
    if head == None:
        return False
    if head.val == target:
        return True
    
    return find_linked_list_recursive(head.next, target)
def get_node_at_index_iterative_iterative(head, index):
    
    current = head
    while current!= None:
        if index == 0:
            return current.val 
        current = current.next
        index -= 1
    return -1

def get_node_at_index_recursive(head, index):
    if head == None:
        return -1
    if index == 0:
        return head.val
    return get_node_at_index_recursive(head.next, index -1)

def reverse_linked_list_iterative(head):
    current = head
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def reverse_linked_list_recursive(head, prev = None):
    if head == None:
        return prev  
    next = head.next
    head.next = prev
    return reverse_linked_list_recursive(next, head)

def zipper_linked_list_iterative(head1, head2):
    head = head1
    current1 = head1
    current2 = head2
    while current1 != None and current2 != None:

        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        current2.next = next1
        current1 = next1.next
        current2 = next2.next
        next1.next= next2
        if current2 == None:
            next1.next.next = current1
        if current1 == None:
            next1.next.next = current2
    return head

def zipper_linked_list_recursive(head1, head2):
    if head1 == None and head2 ==None:
        return None
    if head1 == None:#left over nodes
        return head2
    if head2 == None: #left over nodes
        return head1
    
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
        
    head2.next = zipper_linked_list_recursive(next1, next2)
    return head1
        

        
    


# traversal_linked_list_iterative(a)
# traversal_linked_list_recursive(a)
# sum_linked_list =sum_linked_list_iterative(a)
# print(sum_linked_list)
# sum_linked_list_recursive =sum_linked_list_recursive(a)
# print(sum_linked_list_recursive)
# find_iterative =find_linked_list_iterative(a, 5)
# print(find_iterative)
# find_recursive = find_linked_list_recursive(a, 6)
# print(find_recursive)
# get_node_at_index_iterative_res= get_node_at_index_iterative_iterative(a, 2)
# print(get_node_at_index_iterative_res)
# get_node_at_index_recursive_res = get_node_at_index_recursive(a, 2)
# print(get_node_at_index_recursive_res)
# reverse_list = reverse_linked_list_iterative(a)
# print(traversal_linked_list_iterative(reverse_list))
# reverse_list_recursive = reverse_linked_list_recursive(a)
# print(traversal_linked_list_iterative(reverse_list_recursive))
# zipper_iterative = zipper_linked_list_iterative(a, a2)
# print(traversal_linked_list_iterative(zipper_iterative))
# zipper_iterative = zipper_linked_list_iterative(a2, a)
# print(traversal_linked_list_iterative(zipper_iterative))
zipper_recursive = zipper_linked_list_recursive(a, a2)
print(traversal_linked_list_iterative(zipper_recursive))