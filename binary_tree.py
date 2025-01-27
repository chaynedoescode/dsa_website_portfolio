from graphviz import Digraph

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def create_tree(self, root_value):
        self.root = Node(root_value)

    def add_node(self, parent_value, new_value, direction):
        parent_node = self.find_node(self.root, parent_value)
        if not parent_node:
            return False
        new_node = Node(new_value)
        if direction == 'left':
            if parent_node.left is None:
                parent_node.left = new_node
            else:
                new_node.left = parent_node.left
                parent_node.left = new_node
        elif direction == 'right':
            if parent_node.right is None:
                parent_node.right = new_node
            else:
                new_node.right = parent_node.right
                parent_node.right = new_node
        return True

    def find_node(self, start, value):
        if start is None:
            return None
        if start.value == value:
            return start
        left_result = self.find_node(start.left, value)
        if left_result:
            return left_result
        return self.find_node(start.right, value)

    def delete_node(self, value):
        self.root = self._delete_node_rec(self.root, value)

    def _delete_node_rec(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_node_rec(node.left, value)
        elif value > node.value:
            node.right = self._delete_node_rec(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.get_min(node.right)
            node.value = temp.value
            node.right = self._delete_node_rec(node.right, temp.value)
        return node

    def get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def reset_tree(self):
        self.root = None

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

    def generate_graph(self):
        dot = Digraph()
        self._add_nodes_edges(self.root, dot)
        return dot

    def _add_nodes_edges(self, node, dot):
        if node:
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                self._add_nodes_edges(node.left, dot)
            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                self._add_nodes_edges(node.right, dot)