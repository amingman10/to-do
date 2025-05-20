import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label, add_button], [input_box]])
window.read()
window.close()
