#from functions import get_todos,write_todos #this works only when the 2 files are in same directory
import functions
import time
while True:
    now = time.strftime("%b %d,%Y %H %M %S")
    print(now)
    user_action = input("add,show,edit,complete a todo or exit the program:")
    user_action=user_action.strip()

    if  user_action.startswith("add"):
        todo=user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos,'todos.txt')

    elif   user_action.startswith("show"):

            todos = functions.get_todos()

            new_todos = [item.strip('\n')for item in todos]#list comprehension

            for index,item in enumerate(new_todos):
              index=index+1
              row= f"{index}-{item}"
              print(row)
    elif user_action.startswith("edit") :
        try:
            number=int(user_action[5:])
            number=number-1 #indexing

            todos = functions.get_todos()

            new_todo=input("enter your new todo:")
            todos[number]=new_todo + "\n" #re-assigning/saving the tod0

            functions.write_todos(todos,'todos.txt')

        except ValueError:
            print("your command is invalid")
            continue

    elif  user_action.startswith("complete"):
        try:
            number=int(user_action[8:])

            todos = functions.get_todos()

            number=number-1
            todos.pop(number)

            functions.write_todos(todos,'todos.txt')

        except IndexError :
            print("theres no item with such number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is invalid")
print("good bye")

