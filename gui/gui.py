from gui.utils import nassi, output, file_there
from interpreter.interpret_source import JavaSyntaxError, ScopeNotFoundException, InterpreterException

import PySimpleGUI as sg
import os.path
import random
import secrets
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
                sg.Button('Confirm', key='-SET OUTPUT NAME-'),
            ],
            [
                sg.HSeparator(),
            ],
            [
                sg.Text('Optional: choose custom font and name.'),
            ],
            [
                sg.Text('TTF  File'),
                sg.In(size=(25, 1), enable_events=True, key="-TTF FOLDER-"),
                sg.FileBrowse(file_types=(('TTF-File', '*.ttf'), ('ALL Files',
                                                                  '*.*')), key='-TTF FILE-'),  
            ],

        ]

        file_list_column = [
            [
                sg.Text('Output folder')
            ],
            [ 
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key="-OUTPUT FILE LIST-"
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
        logging.debug('set buttons_column GUI')

        layout = [
            [
                sg.Column(input_column),
                sg.VSeparator(),
                sg.Column(execute_column),
                sg.VSeparator(),
                sg.Column(file_list_column),
                sg.VSeparator(),
                sg.Column(diagramm_viewer_column),
            ]
        ]
        logging.debug('init layout GUI')

        window = sg.Window('Nassi Viewer', layout, resizable=True)
        return window

    def show_gui(self, window: sg.Window):

        font_filepath = None
        output_name = None

        sg.popup('The Interpreter is WIP and cannot interpret classes or function definitions as those do not exist in Nass-Shneidermann Diagrams. A fix is in the making.',
                 auto_close=True, auto_close_duration=5)

        while True:
            logging.info('test')
            event, values = window.read()

            if event == 'Exit' or event == sg.WIN_CLOSED:
                logging.debug(('Exit GUI'))
                break
            
            # execute Column
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
                            if output_name is None:
                                        sg.popup_auto_close('You didn\'t set a name for the image, it will be named randomly.')
                                        output_name = secrets.token_hex(16)
                            if file_there((output_path + '/' + output_name)) is True:
                                proceed = sg.popup_yes_no(
                                    'File already exists! Continue?', title='File alreday exists!')
                                if proceed == 'Yes':
                                    nassi(filepath=file_path, output_path=output_path, outputname=output_name, gui=self,
                                          font_filepath=font_filepath)
                                    

                                    fnames = output(values)
                                    sg.popup_annoying('Successfully created!', title='Created',
                                                      auto_close_duration=2, auto_close=True, text_color='green')
                                    window['-OUTPUT FILE LIST-'].update(fnames)
                                elif proceed == 'No':
                                    logging.warning('Cancelled. No image created')
                                else:
                                    logging.warning(
                                        'You did not make a decision! Try again!')
                                    sg.popup_annoying('You did not make a decision! Try again!', title='FAIL',
                                                      auto_close_duration=2, auto_close=True, text_color='orange')
                            else:                             
                                nassi(filepath=file_path, output_path=output_path, outputname=output_name, gui=self,
                                          font_filepath=font_filepath)

                                fnames = output(values)
                                sg.popup_annoying('Successfully created!', title='Created',
                                                    auto_close_duration=2, auto_close=True, text_color='green')
                                window['-OUTPUT FILE LIST-'].update(fnames)

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
                        except InterpreterException:
                            logging.error(
                                ('||InterpreterException|| Failed to create Image with values = ' + str(values)))
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

            if event == '-CREDITS-':
                sg.popup(
                    'This was made by Plexx, Weckyy702 and Oleting. Libraries used are PySimpleGUI and Pillow', title='Credits')

            if event == '-DONATE-':
                logging.debug(('event = ' + str(event)))
                sg.popup_notify(
                    ('You donated $' + str(random.randint(500, 100000000)) + '.'), title='Thanks')
            
            # needed Input

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

            # optional Input

            if event == '-SET OUTPUT NAME-':
                output_name = values['-OUTPUT NAME-']

            if event == '-TTF FOLDER-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-TTF FOLDER-'])))
                folder = values['-TTF FOLDER-']
                window['-TTF FOLDER-'].update(values['-TTF FILE-'])
                font_filepath = values['-TTF FILE-']

        window.close()
