# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.val}: {f"left:{self.left}" if self.left else " "}; {f"right:{self.right}" if self.right else ""}'


class Solution:
    def deleteNode(self, root:TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            else:
                # if not root.left.right:
                #     root.left.right = root.right
                #     root = root.left
                # elif not root.right.left:
                #     root.right.left = root.left
                #     root = root.right
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.val = cur.val
                root.right = self.deleteNode(root.right, cur.val)
        return root
    
 