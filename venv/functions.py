FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos)) <-- doc string for helping others understand code

# Modifies text file but doesnt need to return anything
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do item as a list into
    the text file.
    """
    with open(filepath, 'w') as file_arg:
        file_arg.writelines(todos_arg)

# print(help(write_todos)) <-- doc string for helping others understand code
# Doc string experiment w/ multiline strings:
text = """
Day 13 of learning python! Doc strings today! 
Productive night!
"""