from PrettyPrint import PrettyPrintTree

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
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def create_expression_tree(self, expression):
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

pt = PrettyPrintTree(lambda x: [child for child in (x.left, x.right) if child], lambda x: x.value if x else None)
tree = BinaryTree(1)
tree.insert_left(tree.root, 6)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 2)  # Node 2 is the left child of Node 6
tree.insert_right(tree.root.left, 5) # Node 5 is the right child of Node 6
tree.insert_left(tree.root.left.left, 4) # Node 4 is the left child of Node 2
tree.insert_right(tree.root.right, 7) # Node 7 is the right child of Node 3
tree.insert_left(tree.root.right, 8) # Node 8 is the left child of Node 3

print("\nFancy Tree Structure:")
pt(tree.root)