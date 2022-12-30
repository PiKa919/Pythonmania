# developer trick: there is always a type of preexisting library either 3rd party or built in that you can use to make your life easier or modify to your needs

# developer trick: dont give pointless names to variables, a variable name must direcctly indicate what it's doing, say in an interview you are asked to explain what a variable does, you should be able to explain it in a few words, I write readale codes, 

#developer trick: always write functions in a seperate file. this makes your code more readable and easier to debug, this is because the functioms can be used by more than one file.

#always use variable whereever possible
#always give default arguments to functions


import PySimpleGUI as sg
import time
import os
import function
#help(sg)

#check if the file exists, if not create it
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('DarkTeal 9')	# Add a touch of color

# All the stuff inside your window.
#first text and title
label = sg.Text('Hello this is my first GUI', font = 'Lucida', size = 55, text_color = 'red', justification = 'center')
label1 = sg.Text('TO-DO List', font = 'Martian_Mono', size = 55, text_color = 'blue', background_color = 'grey', justification = 'center')

#Exit button
exit_button = sg.Button('Exit', size = 55, button_color='red on grey')

#Add button
add_button = sg.Button(image_source = "add.png",image_size=(45,45), key="Add", image_subsample=15)
input_box = sg.InputText(tooltip = 'Enter TO_DO items', key = 'todo')

#listbox
listbox = sg.Listbox(values = function.get_todos(), enable_events= True, size = (35,10), key = 'todos' )

#Edit and Complete buttons
edit_but = sg.Button('Edit', size = 8)
comp_but = sg.Button('Complete', size = 8)

#clock
clock = sg.Text('Clock', key = 'clock')

#layout of the page
layout = [[label],
        [clock],
        [label1],
        [input_box,add_button],
        [listbox, edit_but, comp_but],
        [exit_button] ]

#window output
win = sg.Window('My first GUI', layout = layout, font =20)

#running the application
while True:
    event, values = win.read(timeout=200) # type: ignore #timeout is the time in milliseconds(every 200 milliseconds the clock will update)) 
    win['clock'].update(value = time.strftime('%b %d, %Y %H:%M:%S')) #update the clock
    match event:
        case 'Add':
            todos = function.get_todos()        #get the todos from the text file           
            new_todo = values['todo'] + '\n'    #get the new todo from the input box
            todos.append(new_todo)              #append the new todo to the list of todos
            function.write_todos(todos)         #write the new list of todos to the text file   
            win['todos'].update(values = todos) #use the listbox key to update the listbox

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]   #get the selected item in the listbox
                new_todo = values['todo']           #get the new todo from the input box
                todos = function.get_todos()        #get the todos from the text file
                index = todos.index(todo_to_edit)   #get the index of the selected item in the listbox
                todos[index] = new_todo + '\n'      #replace the selected item with the new todo
                function.write_todos(todos)         #write the new list of todos to the text file
                win['todos'].update(values = todos) #use the listbox key to update the listbox
            except:
                sg.popup('Select an item to edit', font = 20) #popup a message if no item is selected

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]   #get the selected item in the listbox
                todos = function.get_todos()            #get the todos from the text file
                todos.remove(todo_to_complete)          #remove the selected item from the list of todos
                function.write_todos(todos)             #write the new list of todos to the text file
                win['todos'].update(values = todos)     #use the listbox key to update the listbox
                win['todo'].update(value = '')          #clear the input box

            except IndexError:
                sg.popup('Select an item to complete', font = 20) #popup a message if no item is selected

        
        case 'todos':
            win['todo'].update(value = values['todos'][0]) #update the input box with the selected item in the listbox


    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    