class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        if self.top:            
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    else:
        raise ValueError(f"Invalid operator: {op}")

# Function to perform infix to postfix conversion
def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    steps = []
    expression = expression.replace(" ", "")
    
    for char in expression:
        if char.isalnum():  
            postfix.append(char)
            steps.append(''.join(postfix))  # Collect step after adding operand
        elif char == '(':  
            stack.push(char)
        elif char == ')':  
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
                steps.append(''.join(postfix))  # Collect step after popping from stack
            stack.pop()  
        else:  
            while (not stack.is_empty() and stack.peek() not in '()' and precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
                steps.append(''.join(postfix))  # Collect step after popping from stack
            stack.push(char)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
        steps.append(''.join(postfix))  # Collect step after popping from stack

    final_answer = ''.join(postfix)
    return f"answer: {final_answer}\n\nsteps:\n" + '\n'.join(steps)