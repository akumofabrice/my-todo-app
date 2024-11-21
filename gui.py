
import functions
import PySimpleGUI as sg

from functions import get_todos

label = sg.Text("Type in a todo") #creates a display text on the window
input_box = sg.InputText(tooltip="enter a todo",key="todo" ) #creates an input field/textbox
add_button = sg.Button("ADD")


Window=sg.Window("MY TODO APP",
                 layout=[[label],
                         [input_box,add_button]],
                 font=('Helvetica',20) )#connecting/calling the variables to the window by adding in the layout
while True:
    event,value=Window.read()# storing the windows input into the variables/assigning turple to morethan 1 variable
    print(event)#printing the output
    print(value)#printing the output

    match event:
        case "ADD":
            todos = functions.get_todos()# creating a variable(list)call todos and assign the function to it thereby calling the function
            new_todos = value['todo'] + '\n' #storing the window output value in a new variable
            todos.append(new_todos ) #adding to the todos list
            functions.write_todos(todos) #writing the new tod0 to the tod0 list

Window.close()