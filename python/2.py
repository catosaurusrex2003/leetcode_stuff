                            
from collections import deque

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to return the top view of the binary tree
    def topView(self, root):
        # Vector to store the result
        ans = []
        
        # Check if the tree is empty
        if not root:
            return ans
        
        # Map to store the top view nodes
        # based on their vertical positions
        mpp = {}
        
        # Queue for BFS traversal, each element
        # is a pair containing node 
        # and its vertical position
        q = deque([(root, 0)])
        
        # Push the root node with its vertical
        # position (0) into the queue
        while q:
            # Retrieve the node and its vertical
            # position from the front of the queue
            node, line = q.popleft()
            
            # If the vertical position is not already
            # in the map, add the node's data to the map
            if line not in mpp:
                mpp[line] = node.data
            
            # Process left child
            if node.left:
                # Push the left child with a decreased
                # vertical position into the queue
                q.append((node.left, line - 1))
            
            # Process right child
            if node.right:
                # Push the right child with an increased
                # vertical position into the queue
                q.append((node.right, line + 1))
        
        # Transfer values from the
        # map to the result vector
        for value in sorted(mpp.items()):
            ans.append(value[1])
        
        return ans

# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(10)
root.left.left.right = Node(5)
root.left.left.right.right = Node(6)
root.right = Node(3)
root.right.right = Node(10)
root.right.left = Node(9)

solution = Solution()

# Get the top view traversal
topView = solution.topView(root)

# Print the result
print("Vertical Traversal:")
for node in topView:
    print(node, end=" ")
                           
                        