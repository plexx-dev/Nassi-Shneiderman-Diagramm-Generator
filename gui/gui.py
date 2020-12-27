from gui.utils import nassi, output, file_there
from interpreter.interpret_source import JavaSyntaxError, ScopeNotFoundException

import PySimpleGUI as sg
import os.path
import random
import logging
import time


class Gui:

    def __init__(self, theme: str, debug_mode: bool):
        self.debug_mode = debug_mode
        window = self.init_gui(theme=theme)
        self.show_gui(window=window)

    def get_debug_mode(self, mode: bool):
        loging_level = logging.INFO
        if mode:
            loging_level = logging.DEBUG
        logging.basicConfig(level=loging_level)

    def init_gui(self, theme: str):
        self.get_debug_mode(self.debug_mode)

        sg.theme(theme)
        logging.debug(('Theme = ' + theme))

        java_file_list_column = [
            [
                sg.Text('Java File'),
                sg.In(size=(25, 1), enable_events=True, key="-JAVA FOLDER-"),
                sg.FileBrowse(file_types=(('Java-File', '*.java'), ('ALL Files',
                                                                    '*.*')), key='-JAVA FILE-'),  # ('ALL Files','*.*')
            ],
        ]
        logging.debug('set java_file_list_column GUI')

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
        logging.debug('set file_list_column GUI')

        diagramm_viewer_column = [
            [sg.Text("Choose your Code for preview. ", size=(100, 10))],
            [sg.Text(key="-TOUT-", auto_size_text=True)],
            [sg.Image(key='-IMAGE-')],
        ]
        logging.debug('set diagramm_viewer_column GUI')

        font_Input = [
            [
                sg.Text('TTF File'),
                sg.In(size=(25, 1), enable_events=True, key="-TTF FOLDER-"),
                sg.FileBrowse(file_types=(('TTF-File', '*.ttf'), ('ALL Files',
                                                                  '*.*')), key='-TTF FILE-'),  # ('ALL Files','*.*')
            ],
        ]

        buttons_column = [
            [sg.Button(button_text='Create Image', key='-CREATE-')],
            [sg.Button(button_text='Credits', key='-CREDITS-')],
            # * fun feature
            [sg.Button(button_text='Donate', key='-DONATE-')],
        ]
        logging.debug('set buttons_column GUI')

        layout = [
            [
                sg.Column(font_Input),
                sg.Column(java_file_list_column),
                sg.VSeparator(),
                sg.Column(file_list_column),
                sg.VSeparator(),
                sg.Column(buttons_column),
                sg.VSeparator(),
                sg.Column(diagramm_viewer_column),
            ]
        ]
        logging.debug('init layout GUI')

        window = sg.Window('Nassi Viewer', layout, resizable=True)
        return window

    def show_gui(self, window: sg.Window):

        font_filepath = None
        output_name = 'unnamed'

        sg.popup('The Interpreter is WIP and cannot interpret classes or function definitions as those do not exist in Nass-Shneidermann Diagrams. A fix is in the making.',
                auto_close=True, auto_close_duration=5)

        while True:
            event, values = window.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                logging.debug(('Exit GUI'))
                break
            
            if event == '-CREDITS-':
                sg.popup('This is made by Plexx, Weckyy and Oleting. Used PySimpleGUI and Pillow', title='Credits')

            if event == '-DONATE-':
                logging.debug(('event = ' + str(event)))
                sg.popup_notify(
                    ('You donated $' + str(random.randint(500, 100000000)) + '.'), title='Thanks')

            if event == '-OUTPUT FOLDER-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-OUTPUT FOLDER-'])))
                fnames = output(values)
                window['-OUTPUT FILE LIST-'].update(fnames)
            elif event == '-OUTPUT FILE LIST-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-OUTPUT FILE LIST-'])))
                try:
                    filename = os.path.join(
                        values["-OUTPUT FOLDER-"], values["-OUTPUT FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except:
                    pass
            if event == '-JAVA FOLDER-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-JAVA FOLDER-'])))
                folder = values['-JAVA FOLDER-']
                window['-JAVA FOLDER-'].update(values['-JAVA FILE-'])

            if event == '-CREATE-':
                logging.debug(('event = ' + str(event) +
                               'values = ' + str(values)))
                try:
                    if values['-JAVA FOLDER-'] and values['-OUTPUT FOLDER-']:
                        logging.debug(
                            ('Try create Image with values = ' + str(values)))
                        try:
                            file_path = os.path.join(
                                values["-JAVA FOLDER-"],
                            )

                            

                            output_path = values['-OUTPUT FOLDER-']
                            
                            if file_there((output_path + '/' + output_name)) is False:
                                proceed = sg.popup_yes_no('File already exist! Continue?', title='File alreday exist!')
                                print(proceed)
                                if proceed == 'Yes':
                                    nassi(filepath=file_path, output_path=output_path, outputname=output_name, gui=self,
                                                        font_filepath=font_filepath)

                                    fnames = output(values)
                                    sg.popup_annoying('Successful created!', title='Created',
                                                    auto_close_duration=2, auto_close=True, text_color='green')
                                    window['-OUTPUT FILE LIST-'].update(fnames)
                                else:
                                    pass
                        except JavaSyntaxError as JsE:
                            logging.error(
                                ('||SyntaxError in Java File|| Failed to create Image with values = ' + str(values)))
                            sg.popup_error((str(JsE)))
                        except ScopeNotFoundException as SnFe:
                            logging.error(
                                ('||ScopeNotFoundExeption|| Failed to create Image with values = ' + str(values)))
                            sg.popup_error((str(SnFe)))
                        except FileNotFoundError as FnFe:
                            logging.error(
                                ('||FileNotFoundError|| Failed to create Image with values = ' + str(values)))
                            sg.popup_error(
                                (str(FnFe) + 'File ' + str(file_path) + ' or ' + str(output_path) + ' or ' + str(font_filepath) + ' is not reachable.'))
                        except:
                            logging.error(
                                ('Failed to create Image with values = ' + str(values)))
                            sg.popup_error(('Failed to create an image. '))
                            raise

                    elif values['-JAVA FOLDER-']:
                        logging.error('No Output')
                        sg.popup_annoying('No Output', title='Error',
                                          auto_close_duration=5, auto_close=True)
                    elif values['-OUTPUT FOLDER-']:
                        logging.error('No Input')
                        sg.popup_annoying('No Input', title='Error',
                                          auto_close_duration=5, auto_close=True)
                    else:
                        logging.error('Unexpected Case!')
                        sg.popup_annoying('Unexpected Case!', title='Error')
                except:
                    pass

            if event == '-TTF FOLDER-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-TTF FOLDER-'])))
                folder = values['-TTF FOLDER-']
                window['-TTF FOLDER-'].update(values['-TTF FILE-'])
                font_filepath = values['-TTF FILE-']

        window.close()
