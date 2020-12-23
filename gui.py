from to_nassi import nassi
import PySimpleGUI as sg
import os.path


#sg.theme_previewer()
sg.theme('DarkGrey11')

java_file_list_column = [
    [  
        sg.Text('Java File'),
        sg.In(size=(25, 1), enable_events=True, key="-JAVA FOLDER-"),
        sg.FileBrowse(file_types=(('Java-File', '*.java'), ('ALL Files','*.*')), key='-JAVA FILE-'),  # ('ALL Files','*.*')
    ],
]

file_list_column = [
    [  
        sg.Text('Output Folder'),
        sg.In(size=(25, 1), enable_events=True, key="-OUTPUT FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-OUTPUT FILE LIST-"
        )
    ],
]

diagramm_viewer_column = [
    [sg.Text("Choose your Code. ")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key='-IMAGE-')],
]

buttons_column = [
    [sg.Button(button_text='Create Image', key='-CREATE-')],
    [sg.Button(button_text='Donate', key='-DONATE-')],
]


layout = [
    [   
        sg.Column(java_file_list_column),
        sg.VSeparator(),
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(buttons_column),
        sg.VSeparator(),
        sg.Column(diagramm_viewer_column),
    ]
]

window = sg.Window('Nassi Viewer', layout, resizable=True)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-OUTPUT FOLDER-':
        output_path = values['-OUTPUT FOLDER-']
        try:
            file_list = os.listdir(output_path)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(output_path, f))
            and f.lower().endswith(('.png', '.gif'))
        ]
        window['-OUTPUT FILE LIST-'].update(fnames)
    elif event == '-OUTPUT FILE LIST-':
        try:
            filename = os.path.join(
                values["-OUTPUT FOLDER-"], values["-OUTPUT FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
    if event == '-JAVA FOLDER-':
        folder = values['-JAVA FOLDER-']
        window['-JAVA FOLDER-'].update(values['-JAVA FILE-'])

    elif event == '-CREATE-':
        try:
            if values['-JAVA FOLDER-'] and values['-OUTPUT FOLDER-']:
                try:
                    file_path = os.path.join(
                    values["-JAVA FOLDER-"],
                    )
                    sg.popup_annoying('Succsessful created!' , title='Info')
                    
                except:
                    pass
                output_path = values['-OUTPUT FOLDER-']
                nassi(file_path, str(output_path))
                try:
                    file_list = os.listdir(output_path)
                except:
                    file_list = []
                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(output_path, f))
                    and f.lower().endswith(('.png', '.gif'))
                ]
                
                window['-OUTPUT FILE LIST-'].update(fnames)

            elif values['-JAVA FOLDER-']:
                print('No Output')
                sg.popup_annoying('No Output' , title='Error', auto_close_duration=5, auto_close=True)
            elif values['-OUTPUT FOLDER-']:
                print('No Input')
                sg.popup_annoying('No Input' , title='Error', auto_close_duration=5, auto_close=True)
            else:
                sg.popup_annoying('Unexpected Case!' , title='Error')
        except:
            pass

window.close()
