import PySimpleGUI as sg

class Layout_std:

    def __init__(self, theme: str):
        self.theme = theme

    def layout(self):
        sg.theme(self.theme)
        toolbar = [
            [
                sg.Button(button_text='Create Image', key='-CREATE-'),
                sg.Button(button_text='Credits', key='-CREDITS-'),
                # * fun feature
                sg.Button(button_text='Donate', key='-DONATE-'),
            ]
        ]

        input_column = [
            [
                sg.Text('Java File'),
                sg.In(size=(25, 1), enable_events=True, key="-JAVA FOLDER-"),
                sg.FileBrowse(file_types=(('Java-File', '*.java'), ('ALL Files',
                                                                    '*.*')), key='-JAVA FILE-'),
            ],
            [
                sg.Text('Output Folder'),
                sg.In(size=(25, 1), enable_events=True, key="-OUTPUT FOLDER-"),
                sg.FolderBrowse(),
            ],
            [
                sg.Text('Output name'),
                sg.In(size=(25, 1), enable_events=True, key='-OUTPUT NAME-'),
                #sg.Button('Confirm', key='-SET OUTPUT NAME-'),
            ],
            [
                sg.HSeparator(),
            ],
            [
                sg.Text('Optional: choose custom font.'),
            ],
            [
                sg.Text('TTF  File'),
                sg.In(size=(25, 1), enable_events=True, key="-TTF FOLDER-"),
                sg.FileBrowse(file_types=(('TTF-File', '*.ttf'), ('ALL Files',
                                                                    '*.*')), key='-TTF FILE-'),
            ],
            [
                sg.Button(button_text='Add costum types', key='-TYPES-')
            ],
            [
                # modifier
                sg.Button(button_text='Add costum modifier', key='-MODIFIER-')
                # comments
            ],
            [
                sg.Button(button_text='Add costum comments', key='-COMMENTS-')
                # comments
            ],

        ]

        file_list_column = [
            [
                sg.Text('Output folder'),

                sg.Button(button_text='Refresh', key='-REFRESH-')
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key="-OUTPUT FILE LIST-",
                )
            ],
        ]

        diagramm_viewer_column = [
            [sg.Text("Choose your code for preview. ", auto_size_text=True)],
            [sg.Text(key="-TOUT-", auto_size_text=True)],
            [sg.Image(key='-IMAGE-')],
        ]

        execute_column = [
            [sg.Button(button_text='Create Image', key='-CREATE-')],
            [sg.Button(button_text='Credits', key='-CREDITS-')],
            # * fun feature
            [sg.Button(button_text='Donate', key='-DONATE-')],
        ]

        layout = [
            [
                sg.Column(input_column),
                sg.VSeparator(),
                #sg.Column(execute_column),
                sg.VSeparator(),
                sg.Column(file_list_column),
                sg.VSeparator(),
                sg.VSeparator(),
                sg.Column(diagramm_viewer_column),
            ]
        ]

        layout_with_toolbar = [
            [
                sg.Column(toolbar)
            ],
            [
                sg.HSeparator(),
            ], 
            [
                sg.Column(layout)
            ]
        ]

        return layout_with_toolbar

class Layout_popup:
    def __init__(self):
        text_column = [
            [
                sg.Text('What should the program do if a file already exist?')
            ]
        ]

        choices = [
            [
                sg.Button(button_text='skip', key='-SKIP-'),
                sg.Button(button_text='overwrite', key='-OVERWRITE-'),
                sg.Button(button_text='create expicit name', key='-EXPICIT-'),
            ]
        ]
        self.layout = [
            [
                sg.Column(text_column),
                sg.Column(choices),
            ]
        ]

