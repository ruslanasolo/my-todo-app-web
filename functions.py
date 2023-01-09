FILEPATH = "/Users/Rusya/mega/app1/venv/todos.txt"
#FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # custom function definition
    """ Read a text file and return the st of todo items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items lst ib the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


#  if _name_ == "_main_":
    #  print(get_todos(()))
    