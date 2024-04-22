from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node, queue=deque()):
    res = []
    if node:
        res.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if queue:
            current = queue.popleft()
            res += tree_by_levels(current, queue)
    return res
