import PySimpleGUI as sg

# Define the layout of the main window
layout = [
    [sg.Text('Welcome to the Password Keeper')],
    [sg.Text('Enter a name for the password: '), sg.InputText(key='name')],
    [sg.Text('Enter the password: '), sg.InputText(key='password', password_char='*')],
    [sg.Button('Add Password'), sg.Button('View Passwords'), sg.Button('Exit')],
]

# Create the main window
window = sg.Window('Password Keeper', layout)

# Define an empty list to store passwords
passwords = []

# Define the layout of the password viewer window
viewer_layout = [
    [sg.Text('Saved Passwords')],
    [sg.Listbox(values=passwords, size=(50, 10), key='password_list')],
    [sg.Button('Delete Password'), sg.Button('Close')]
]

# Create the password viewer window
viewer_window = sg.Window('Password Viewer', viewer_layout)

# Event loop for the main window
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Add Password':
        name = values['name']
        password = values['password']
        passwords.append(f'{name}: {password}')
        sg.popup(f'Added password for {name}!')

    if event == 'View Passwords':
        viewer_window['password_list'].update(values=passwords)
        while True:
            viewer_event, viewer_values = viewer_window.read()
            if viewer_event == sg.WINDOW_CLOSED or viewer_event == 'Close':
                break
            if viewer_event == 'Delete Password':
                selected_password = viewer_values['password_list'][0]
                passwords.remove(selected_password)
                viewer_window['password_list'].update(values=passwords)

# Close the windows
window.close()
viewer_window.close()
