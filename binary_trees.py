class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# k = log(n + 1)

def parse_tuple(data):
    #root node
   
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node
    
tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print("tree2", tree2)
def print_tree(node: TreeNode,space='\t', level = 0):

    #none
    if node is None:
        print(space*level +'∅')
        return

    #no children
    if node.left is None and node.right is None:
          print(space*level + str(node.key))
          return

    #children

    print_tree(node.right, space, level+1)
    print(space * level + str(node.key))
    print_tree(node.left, space, level+1)

print_tree(tree2, '  ')

def tree_to_tutple(node):
    if node is None:
        return None;
    if node.left is None and node.right is None:
        return node.key
    tree_tuple = tree_to_tutple(node.left), node.key, tree_to_tutple(node.right)
    return tree_tuple
etl =tree_to_tutple(tree2)

print("etl", etl)


#Traversing binary tree
#InOrder Traversal
#Preorder Traversal
