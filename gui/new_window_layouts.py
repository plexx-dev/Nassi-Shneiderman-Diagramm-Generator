import PySimpleGUI as sg

class layout_popup:
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