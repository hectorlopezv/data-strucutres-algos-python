class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.level = 0
a =  Node(1)
b =  Node(2)
c =  Node(3)
d =  Node(4)
e =  Node(5)
f = Node(6)
z= Node(7)
pp = Node(8)
pz = Node(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
c.left = z
z.left = pp
pp.left= pz


def depth_first_values_stack_way(node: Node):
    if node is None:
        return []
    result = []
    stack = [node]

    while len(stack) > 0:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def depth_first_values_way_recursion(node: Node):
    if node is None:
        return []
    left = depth_first_values_way_recursion(node.left)
    right = depth_first_values_way_recursion(node.right)
    return [node.data] + left + right
        
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

def print_subtree(node: Node):
    height = height_sub_tree(node);
    for i in range(1, height + 1):  
        breath_first_values_way_recursion(node, i)

def breath_first_values_way_recursion(node: Node, level:int ):
    if node is None:
        return
    if level == 1:
        print(node.data, end=" ")
    elif level > 1:
        breath_first_values_way_recursion(node.left, level - 1)
        breath_first_values_way_recursion(node.right, level - 1)

def height_sub_tree(node: Node):
    if node is None:
        return 0
    left_height = height_sub_tree(node.left)
    right_height = height_sub_tree(node.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1

def tree_includes_breath_first_values_way(node: Node, value):
    if node is None or value is None:
        return False
    if node.data == value:
        return True
    queque = [node]
    while len(queque) > 0:
        node = queque.pop()
        if node.data == value:
            return True
        if node.left and node.right:
            queque.append(node.left)
            queque.append(node.right)
        elif node.left:
            queque.append(node.left)
        elif node.right:
            queque.append(node.right)
    return False

def tree_includes_depth_first_values_way_recursion(node: Node, value):
    if node is None or value is None:
        return False
    if node.data == value:
        return True
    left = tree_includes_depth_first_values_way_recursion(node.left, value)
    right = tree_includes_depth_first_values_way_recursion(node.right, value)
    return left or right
def tree_sum_depth_first_way(node: Node):
    if node is None:
        return 0
    left = tree_sum_depth_first_way(node.left)
    right = tree_sum_depth_first_way(node.right)
    return left +  right + node.data

def tree_sum_breath_first_way(node: Node):
    if node is None:
        return 0
    queue = [node]
    result = 0
    while len(queue) > 0:
        node = queue.pop(0)
        result += node.data
        if node.left and node.right:
            queue.append(node.left)
            queue.append(node.right)
        elif node.left:
            queue.append(node.left)
        elif node.right:
            queue.append(node.right)
    return result

def tree_min_value_depth_first_way(node: Node):
    if node is None:
        return
    left = tree_min_value_depth_first_way(node.left)
    right = tree_min_value_depth_first_way(node.right)
    if left is None and right is None:
        return node.data
    elif left is None:
        return min(right, node.data)
    elif right is None:
        return min(left, node.data)
def tree_max_value_depth_first_way(node:Node):
    if node is None:
        return 0
    left = tree_max_value_depth_first_way(node.left)
    right = tree_max_value_depth_first_way(node.right)

    return max(left, right, node.data)

def max_root_to_leaf_sum(node: Node):
    if node is None:
        return 0
    left = max_root_to_leaf_sum(node.left)
    right = max_root_to_leaf_sum(node.right)
    return max(left, right) + node.data
def tree_is_balanced(node: Node):
    if node is None:
        return True
    left = height_sub_tree(node.left)
    right = height_sub_tree(node.right)
    if abs(left - right) > 1:
        return False
    return tree_is_balanced(node.left) and tree_is_balanced(node.right)


#write a function to create a balance BST from a sorte list/array of key-value pairs
def create_balanced_bst_from_sorted_array(arr):
    pass
# res = depth_first_values_way_recursion(a)
# res_stack = depth_first_values_stack_way(a)
#res_queue = breath_first_values_way_queue(a)
# res_includes = tree_includes_breath_first_values_way(a, 'f')
# res_includes_breath = tree_includes_depth_first_values_way_recursion(a, 'e')
# res_includes_breath_none = tree_includes_depth_first_values_way_recursion(a, None)
# res_sum_depth = tree_sum_depth_first_way(a)
# res_sum_breath = tree_sum_breath_first_way(a)
# res_min_value = tree_min_value_depth_first_way(a)
res_max_value = tree_max_value_depth_first_way(a)
res_max_root_to_leaf_sum = max_root_to_leaf_sum(a)
res_tree_balanced = tree_is_balanced(a)
res_create_bst = create_balanced_bst_from_sorted_array()
#print_subtree(a)#breath_first_values_way_recursion
# print(res)
# print(res_stack)
#print(res_queue)
# print(res_includes)
# print(res_includes_breath)
# print(res_includes_breath_none)
# print(res_sum_depth)
# print(res_sum_breath)
# print(res_min_value)
print(res_max_value)
print(res_max_root_to_leaf_sum)
print(res_tree_balanced)