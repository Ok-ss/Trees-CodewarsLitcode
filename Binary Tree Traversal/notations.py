class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return f'{self.data}'

# Pre-order traversal
def pre_order(node):
    res = []
    if node:
        res.append(node.data)
        if node.left:
            res += pre_order(node.left)
        if node.right:
            res += pre_order(node.right)
    return res

# In-order traversal
def in_order(node):
    res = []
    if node:
        if node.left:
            res += in_order(node.left)
        res.append(node.data)
        if node.right:
            res += in_order(node.right)
    return res

# Post-order traversal
def post_order(node):
    res = []
    if node:
        if node.left:
            res += post_order(node.left)
        if node.right:
            res += post_order(node.right)
        res.append(node.data)
    return res

