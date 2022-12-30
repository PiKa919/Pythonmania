FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of to-dos items"""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args,filepath = FILEPATH):
    """Write a to-do items list in the text file"""

    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)