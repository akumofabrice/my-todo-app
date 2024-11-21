from cProfile import label

from PySimpleGUI import Window

import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo") #creates a display text on the window
input_box = sg.InputText(tooltip="enter a todo") #creates an input field/textbox
add_button = sg.Button("ADD")


Window=sg.Window("MY TODO APP",layout=[[label],[input_box,add_button]] )#connecting/calling the variables to the window by adding in the layout
Window.read()
Window.close()