import time
import functions

now = time.strftime("%b %d. %Y %H:%M:%S")
print("Current Time: ", now)
while True:
    action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ")
    action = action.strip()

    if action.startswith("add"):
        todo = action[4:]
        # Captures def get_todos
        todos = functions.get_todos()
        todos.append(todo + '\n')
        # Captures def write_todos
        functions.write_todos(todos)


    elif action.startswith("show"):
        # Captures def get_todos
        todos = functions.get_todos()

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)
        print(len(todos))

    elif action.startswith("edit"):
        try:
            number = int(action[5:])
            number = number - 1

            # Captures def get_todos
            todos = functions.get_todos()

            print('Here is the existing list: ', todos)

            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + '\n'
            print('Here is how it will be: ', todos)

            # Captures def write_todos
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif action.startswith("complete"):
        try:
            number = int(action[9:])
            # Captures def get_todos
            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)
        except IndexError:
            print("There is no item with that number.")
            continue

        # Captures def write_todos
        functions.write_todos(todos)

        message = f"Todo {todo_to_remove.strip()} was removed from the list."
        print(message)

    elif action.startswith("exit"):
        print("Thank you! Bye!")
        break
    else:
        print("Command is not valid.")