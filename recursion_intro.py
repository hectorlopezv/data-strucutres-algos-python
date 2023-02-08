#Recursion basics
#Recursion is a method of solving problems by having a function call itself
# using the same algorithm.  This is a very powerful technique, but it can
# also be very confusing.  It is important to understand the basics of
# recursion before attempting to use it in your programs.
#Using the stack

def string_reversal_recursion(s:str)->str:
    if len(s) ==1:
        return s
    return string_reversal_recursion(s[1:]) + s[0]

# res_recursion_reversal = string_reversal_recursion("hello")
# print(res_recursion_reversal)

def palindrome_recursion(s:str)->bool:
    if len(s)==1:
        return True
    if s[0] != s[-1]:
        return False
    
    return palindrome_recursion(s[1:-1])

# print(palindrome_recursion("kayak"))

def decimal_to_binary_recursion(n:int)-> str:
    if n == 0:
        return "" 
    return decimal_to_binary_recursion(n//2) + str(n%2)


# print(decimal_to_binary_recursion(233))

def sum_of_natural_number_recursion(n: int)-> int:
    if n <= 1:
        return 1
    return sum_of_natural_number_recursion(n-1) + n

# print(sum_of_natural_number_recursion(10))


#DIVIDE AND CONQUER FRAMEWORK
#(1) Divide the problem into a number of subproblems that are smaller instances of the same problem.
#(2) Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
#(3) Combine the solutions to the subproblems into the solution for the original problem.


def binary_search_recursion(arr:list, left: int, right: int, target: int)-> int:

    if left > right:
        return -1
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    if target > arr[mid]:
        return binary_search_recursion(arr, mid+1, right, target)
    if target < arr[mid]:
        return binary_search_recursion(arr, left, mid-1, target)
    
# print(binary_search_recursion([-1, 0,1,2,3,4,7,9,10,20], 0, 9, 10))

def fibonacci_recursion(n: int)->int:
    if n == 1 or n == 0:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)    

def merge(left: list, right: list)->list:
    result = []
    while len(left)>0 and len(right)>0:
        if left[0]< right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)>0:
        result += left
    if len(right)>0:
        result += right
    return result
    
         
def merge_sort_recursion(arr:list)-> list:
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursion(arr[:mid])
    right = merge_sort_recursion(arr[mid:])

    return merge(left, right)


# print(merge_sort_recursion([4,1,3,2,0,-1,7,10,9,20]))
    
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# a = Node(1)
# b = Node(8)
# c = Node(22)
# d = Node(40)

# a.next = b
# b.next = c
# c.next = d

# a2 = Node(4)
# b2 = Node(11)
# c2 = Node(16)
# d2 = Node(20)

# a2.next = b2
# b2.next = c2
# c2.next = d2


def traversal_linked_list_iterative(head):
    current = head
    while current != None:
        print(current.val)
        current = current.next

def linked_list_reversal(node):
    if node.next == None or node == None:
        return node
    new_head = linked_list_reversal(node.next)
    node.next.next = node
    node.next = None
    return new_head
#traversal_linked_list_iterative(linked_list_reversal(a))

def merge_two_linked_list_recursive(l1, l2):

    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val< l2.val:
        l1.next = merge_two_linked_list_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_linked_list_recursive(l1, l2.next)
        return l2
    
# traversal_linked_list_iterative(merge_two_linked_list_recursive(a, a2))
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
a =  Node(1)
b =  Node(2)
c =  Node(9)
d =  Node(4)
e =  Node(5)
f = Node(6)
z = Node(7)


a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
c.left = z

def breath_first_values_way_queue(node: Node):
    queue = [node]
    result = []

    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.data)
        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)
        elif node.left:
            queue.append(node.left)
        elif node.right:
            queue.append(node.right)

    return result


def insert_value_into_binary_search_tree(node, val):
    if node is None:
        return Node(val)
    if val < node.data:
        node.left= insert_value_into_binary_search_tree(node.left, val)
    else:
        node.right =  insert_value_into_binary_search_tree(node.right, val)
    return node


def print_all_leaf_nodes(node):
    if node is None:
        return
    if node.left is None and node.right is None:
        print(node.data)
    print_all_leaf_nodes(node.left)
    print_all_leaf_nodes(node.right)
def depth_fisrt_recursion(node):
    if node is None:
        return
    print(node.data)
    depth_fisrt_recursion(node.left)
    depth_fisrt_recursion(node.right)



##OPTIMIZATIONS, MEMOIZING, CACHNING

def fibonancci_memoization(n, memo):
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    n_1 = fibonancci_memoization(n-1, memo)
    n_2 = fibonancci_memoization(n-2, memo)
    memo[n] = n_1 + n_2
    return memo[n]

#Last function call is a recursive call, so it will be added to the call stack
def tail_call_recursion_optimization():
    pass
# print(breath_first_values_way_queue(a))
# print(insert_value_into_binary_search_tree(a, 10))
# print(breath_first_values_way_queue(a))
# print_all_leaf_nodes(a)
# fibonancci_memoization(10, {1:1, 0:1})