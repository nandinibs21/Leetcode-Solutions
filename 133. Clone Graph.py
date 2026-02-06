# Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        clones = {node: Node(node.val)}

        q = deque([node])
        while q:
            cur = q.popleft()
            cur_clone = clones[cur]

            for nei in cur.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                cur_clone.neighbors.append(clones[nei])

        return clones[node]
