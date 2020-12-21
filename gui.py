
from to_nassi import nassi

import PySimpleGUI as sg
import os.path

#sg.theme_previewer()
sg.theme('DarkGrey11')

java_file_list_column = [
    [  
        sg.Text('Java Folder'),
        sg.In(size=(25, 1), enable_events=True, key="-JAVA FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-JAVA FILE LIST-"
        )
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
    [sg.Text("Choose your Code from the left. ")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key='-IMAGE-')],
]



layout = [
    [
        sg.Column(java_file_list_column),
        sg.VSeparator(),
        sg.Column(file_list_column),
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
        folder = values['-OUTPUT FOLDER-']
        print(folder)
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
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
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith(('.java', '.txt'))
        ]
        window['-JAVA FILE LIST-'].update(fnames)
    elif event == '-JAVA FILE LIST-':
        try:
            filename = os.path.join(
                values["-JAVA FOLDER-"], values["-JAVA FILE LIST-"][0]
            )

            window["-TOUT-"].update(filename)
            nassi(filename)

        except:
            pass
    

window.close()
