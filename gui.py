
import functions
import PySimpleGUI as sg
import time


sg.theme('DarkBlue17') #give default coloring theme to our program

clock = sg.Text("",key='clock')
label = sg.Text("Type in a todo") #creates a display text on the window
input_box = sg.InputText(tooltip="enter a todo",key="todo" ) #creates an input field/textbox
add_button = sg.Button("ADD")

list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size = [45, 10], )
edit_button = sg.Button("EDIT")

complete_button = sg.Button("COMPLETE")
exit_button = sg.Button("EXIT")



Window=sg.Window("MY TODO APP",
                 layout=[[clock],[label],
                         [input_box,add_button],[list_box,edit_button,complete_button],[exit_button]],

                 font=('Helvetica',20) )#connecting/calling the variables to the window by adding in the layout
while True:
    event,value=Window.read(timeout=500)# storing the windows input into the variables/assigning turple to morethan 1 variable
    #timeout=10 keeps the clock ticking
    Window['clock'].update(value=time.strftime("%b %d,%Y %H %M %S"))
    print(event)#printing the output
    print(value)#printing the output

    match event:
        case "ADD":
            todos = functions.get_todos()# creating a variable(list)call todos and assign the function to it thereby calling the function
            new_todos = value['todo'] + '\n' #storing the window output value in a new variable
            todos.append(new_todos ) #adding to the todos list
            functions.write_todos(todos) #writing the new tod0 to the tod0 list
            Window["todos"].update(values=todos)
        case "EDIT":
            try:
                todo_to_edit = value['todos'][0]#we include [0] so toget only the str
                new_todo = value['todo'] #get the value at this key 'tod0'

                todos = functions.get_todos() #calling the read function that reads the todos list
                index = todos.index(todo_to_edit) #index the todos and store it in a variable
                todos[index] = new_todo +'\n'#todos at this indext should be replaced by new_todo
                functions.write_todos(todos) #then write the new_todo in the file/list by calling the write function
                Window["todos"].update(values=todos) #this keep the list updated immediately we click the edit button
            except IndexError:
                sg.popup("select an item to edit first" ,font=('Helvetica',20))
        case "COMPLETE":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                Window['todos'].update(values=todos)
            except IndexError:
                sg.popup("select an item to edit first", font=('Helvetica', 20))
        case "EXIT":
            break
        case 'todos':
            Window["todo"].update(value=value['todos'][0])  # this update the text_box with the tod0 we wish to edit
        case sg.WINDOW_CLOSED:
            break


Window.close()