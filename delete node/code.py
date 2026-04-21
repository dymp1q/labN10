from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    if node is None:
        return []

    else:
        res = []
        queue = deque()
        queue.append(node)
        while queue:
            nod = queue.popleft()
            res.append(nod.value)
            if nod.left is not None:
                queue.append(nod.left)
            if nod.right is not None:
                queue.append(nod.right)
        return res
