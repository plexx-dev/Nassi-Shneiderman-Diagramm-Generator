
import PySimpleGUI as sg
import os.path

java_file_list_column = [
    [  
        sg.Text('Image Folder'),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

file_list_column = [
    [  
        sg.Text('Image Folder'),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

diagramm_viewer_column = [
    [sg.Text("Choose your Code from the left: ")],
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

window = sg.Window('Nassi Viewer', layout)

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-FOLDER-':
        folder = values['-FOLDER-']
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
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            pass

window.close()
