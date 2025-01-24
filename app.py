from flask import Flask, render_template, request
from linked_list import LinkedList
from stack import Stack, precedence, infix_to_postfix
from q import Queue, Dequeue

app = Flask(__name__)
linked_list = LinkedList()
queue = Queue()
dequeue = Dequeue()

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/linked_list', methods=["POST", "GET"])
def linked_list_view():
    success_message = None
    # Handle POST request (form submission)
    if request.method == "POST":
        user_input = request.form.get('input') 
        action = request.form.get('action')  

        if action == 'insert_beginning':
            linked_list.insert_at_beginning(user_input)

        elif action == 'insert_end':
            linked_list.insert_at_end(user_input)

        elif action == 'remove_beginning':
            linked_list.remove_beginning()

        elif action == 'remove_end':
            linked_list.remove_at_end()

        elif action == 'remove_position':
            linked_list.remove_at(user_input)

        elif action == 'search':
            if linked_list.search(user_input):
                success_message = "Item Found"
            else:
                success_message = "Item Not Found"
            return render_template('LINKED LIST.html', success_message=success_message)

        # Automatically print the linked list after each operation
        result = linked_list.print_linked_list()
        if result == False:
            success_message = "Linked list is Empty"
        else:
            success_message = result

    return render_template('LINKED LIST.html', success_message=success_message)

@app.route('/stack', methods=["POST", "GET"])
def stack():
    user_input = ""
    steps = ""
    if request.method == "POST":
        user_input = request.form.get('input') 
        action = request.form.get('action')

        if action == 'convert':
            steps = infix_to_postfix(user_input)
            return render_template('STACK.html', user_input=user_input, steps=steps)
    return render_template('STACK.html', user_input=user_input, steps=steps)

@app.route('/enqueue', methods=['GET', 'POST'])
def enqueue():
    if request.method == 'POST':
        action = request.form['action']
        input_value = request.form.get('input', '')

        if action == 'enqueue':
            queue.enqueue(input_value)
        elif action == 'dequeue':
            queue.dequeue()
        elif action == 'size':
            size = queue.size()
            success_message = f'Queue size: {size}'
            return render_template('enqueue.html', success_message=success_message)
        elif action == 'empty':
            is_empty = queue.is_empty()
            success_message = 'Queue is empty' if is_empty else 'Queue is not empty'
            return render_template('enqueue.html', success_message=success_message)
        elif action == 'print':
            queue_contents = queue.print_queue()
            success_message = f'Queue contents: {queue_contents}'
            return render_template('enqueue.html', success_message=success_message)
        else:
            success_message = 'Invalid action'
            return render_template('enqueue.html', success_message=success_message)

        queue_contents = queue.print_queue()
        success_message = f'Queue contents: {queue_contents}'
        return render_template('enqueue.html', success_message=success_message)

    return render_template('enqueue.html')

@app.route('/dequeue', methods=['GET', 'POST'])
def dequeue_route():
    if request.method == 'POST':
        action = request.form['action']
        input_value = request.form.get('input', '')

        if action == 'add_front':
            dequeue.add_front(input_value)
        elif action == 'add_rear':
            dequeue.add_rear(input_value)
        elif action == 'remove_front':
            dequeue.remove_front()
        elif action == 'remove_rear':
            dequeue.remove_rear()
        elif action == 'size':
            size = dequeue.size()
            success_message = f'Dequeue size: {size}'
            return render_template('dequeue.html', success_message=success_message)
        elif action == 'empty':
            is_empty = dequeue.is_empty()
            success_message = 'Dequeue is empty' if is_empty else 'Dequeue is not empty'
            return render_template('dequeue.html', success_message=success_message)
        elif action == 'print':
            dequeue_contents = dequeue.print_queue()
            success_message = f'Dequeue contents: {dequeue_contents}'
            return render_template('dequeue.html', success_message=success_message)
        else:
            success_message = 'Invalid action'
            return render_template('dequeue.html', success_message=success_message)

        dequeue_contents = dequeue.print_queue()
        success_message = f'Dequeue contents: {dequeue_contents}'
        return render_template('dequeue.html', success_message=success_message)

    return render_template('dequeue.html')

@app.route('/binary_tree')
def tree():
    return render_template('BINARY TREE.html')

if __name__ == '__main__':
    app.run(debug=True)