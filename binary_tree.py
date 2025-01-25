from tree_printer import print_tree, print_tree_fancy, print_artistic

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def inorder_traversal(self, start, traversal):
        """
        Perform in-order traversal of the binary tree.
        In-order traversal visits nodes in the following order:
        1. Traverse the left subtree.
        2. Visit the root node.
        3. Traverse the right subtree.
        Args:
            start (TreeNode): The starting node of the traversal.
            traversal (str): The string that accumulates the traversal result.
        Returns:
            str: The traversal result as a string with node values separated by '-'.
        """
        
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # def delete_node(self, root, key):
      

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # def search(self, root, key):
       

    def create_expression_tree(self, expression):
        """
        Create an arithmetic expression tree from a list of tokens
        Args:
            expression: List of strings representing the expression in postfix notation
            Example: ["4", "5", "+", "7", "3", "-", "*"] for (4 + 5) * (7 - 3)
        """
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in expression:
            node = Node(token)
            if token in operators:
                # Operator node: pop two operands and attach them
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
            
        self.root = stack[0]
        return self.root

    def evaluate_expression(self, node):
        """
        Evaluate the arithmetic expression tree
        Args:
            node: Root node of the expression tree
        Returns:
            float: Result of the expression
        """
        if node is None:
            return 0
        
        # Leaf node (operand)
        if node.left is None and node.right is None:
            return float(node.value)
        
        # Evaluate left and right subtrees
        left_val = self.evaluate_expression(node.left)
        right_val = self.evaluate_expression(node.right)
        
        # Apply operator
        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val


# Initialize the tree
# tree = BinaryTree(1)
# # Manually add nodes to the tree
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

# print("\nFancy Tree Structure:")
# print(print_tree_fancy(tree.root))

# Alternatively, use the insert functions
# Using only insert_left and insert_right
# Initialize the tree
# tree = BinaryTree(1)
# tree.insert_left(tree.root, 6)
# tree.insert_right(tree.root, 3)
# tree.insert_left(tree.root.left, 2)  # Node 2 is the left child of Node 6
# tree.insert_right(tree.root.left, 5) # Node 5 is the right child of Node 6
# tree.insert_left(tree.root.left.left, 4) # Node 4 is the left child of Node 2
# tree.insert_right(tree.root.right, 7) # Node 7 is the right child of Node 3
# tree.insert_left(tree.root.right, 8) # Node 8 is the left child of Node 3

# tree.insert_left(tree.root.right.right, 18) # Node 8 is the left child of Node 3
# tree.insert_left(tree.root.right.left, 20) # Node 8 is the left child of Node 3
# print("\nFancy Tree Structure:")
# print(print_tree_fancy(tree.root))


# Perform inorder traversal

# print("\nFancy Tree Structure:")
# print(print_tree_fancy(tree.root))

# print(tree.inorder_traversal(tree.root, ""))

# print("\nFancy Tree Structure:")
# print(print_tree_fancy(tree.root))


# Delete a node
# tree.delete_node(tree.root, 3)

# print("\nFancy Tree Structure after deletion:")
# print(print_tree_fancy(tree.root))

# print("delete 3",tree.inorder_traversal(tree.root, ""))

# Search for a node
# result = tree.search(tree.root, 5)
# if result:
#     print(f"Node with value 5 found: {result.value}")
# else:
#     print("Node with value 5 not found")


# print(print_tree_fancy(tree.root))

# print(tree.inorder_traversal(tree.root, ""))


# # Test the tree printing
# print("\nSimple Tree Structure:")
# print_tree(tree.root)

# print("\nFancy Tree Structure:")
# print(print_tree_fancy(tree.root))





# Test the arithmetic expression tree
# Example: (4 + 5) * (7 - 3) = 9 * 4 = 36
expr_tree = BinaryTree(None)
postfix_expr = ["4", "5", "+", "7", "3", "-", "*"]
expr_tree.create_expression_tree(postfix_expr)

print("\nArithmetic Expression Tree:")
print(print_tree_fancy(expr_tree.root))

result = expr_tree.evaluate_expression(expr_tree.root)
print(f"\nExpression result: {result}")


