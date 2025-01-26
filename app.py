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

@app.route('/queue', methods=['GET', 'POST'])
def queue_view():
    queue_message = request.form.get('queue_message', "Output will appear here")
    dequeue_message = request.form.get('dequeue_message', "Output will appear here")
    
    if request.method == 'POST':
        action = request.form['action']
        queue_input = request.form.get('queue_input', '')
        dequeue_input = request.form.get('dequeue_input', '')

        if action == 'enqueue':
            queue.enqueue(queue_input)
            queue_message = f'Queue contents: {queue.print_queue()}'
        elif action == 'dequeue':
            if queue.is_empty():
                queue_message = 'ERROR! Queue is empty'
            else:
                queue.dequeue()
                queue_message = f'Queue contents: {queue.print_queue()}'
        elif action == 'queue_size':
            size = queue.size()
            queue_message = f'Queue size: {size}'
        elif action == 'queue_empty':
            is_empty = queue.is_empty()
            queue_message = 'Queue is empty' if is_empty else 'Queue is not empty'
        elif action == 'queue_print':
            queue_contents = queue.print_queue()
            queue_message = f'Queue contents: {queue_contents}'
        elif action == 'add_front':
            dequeue.add_front(dequeue_input)
            dequeue_message = f'Dequeue contents: {dequeue.print_queue()}'
        elif action == 'add_rear':
            dequeue.add_rear(dequeue_input)
            dequeue_message = f'Dequeue contents: {dequeue.print_queue()}'
        elif action == 'dequeue_size':
            size = dequeue.size()
            dequeue_message = f'Dequeue size: {size}'
        elif action == 'remove_front':
            if dequeue.is_empty():
                dequeue_message = 'ERROR! Dequeue is empty'
            else:
                dequeue.remove_front()
                dequeue_message = f'Dequeue contents: {dequeue.print_queue()}'
        elif action == 'remove_rear':
            if dequeue.is_empty():
                dequeue_message = 'ERROR! Dequeue is empty'
            else:
                dequeue.remove_rear()
                dequeue_message = f'Dequeue contents: {dequeue.print_queue()}'
        elif action == 'dequeue_empty':
            is_empty = dequeue.is_empty()
            dequeue_message = 'Dequeue is empty' if is_empty else 'Dequeue is not empty'
        elif action == 'dequeue_print':
            dequeue_contents = dequeue.print_queue()
            dequeue_message = f'Dequeue contents: {dequeue_contents}'
        else:
            if action.startswith('queue'):
                queue_message = 'Invalid action'
            else:
                dequeue_message = 'Invalid action'

    return render_template('queue.html', queue_message=queue_message, dequeue_message=dequeue_message)

@app.route ('/binary_tree')
def tree():
    return render_template('binary_tree.html')
@app.route ('/graph')   
def graph():
    return render_template('graphh.html')

if __name__ == '__main__':
    app.run(debug=True)
