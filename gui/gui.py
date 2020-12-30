from gui.utils import nassi, output
from errors.custom import JavaSyntaxError, ScopeNotFoundException, InterpreterException, NoPathError
from interpreter.NassiShneidermann import OB

import PySimpleGUI as sg
import os.path
import random
import secrets
import logging
import time

# new popup


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

       
                    

        toolbar = [
            [
                sg.Button(button_text='Create Image', key='-CREATE-'),
                sg.Button(button_text='Credits', key='-CREDITS-'),
                # * fun feature
                sg.Button(button_text='Donate', key='-DONATE-'),
                #sg.ButtonMenu('', menu_def),
                
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
                sg.Button('Confirm', key='-SET OUTPUT NAME-'),
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
        logging.debug('set buttons_column GUI')

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

        logging.debug('init layout GUI')

        window = sg.Window('Nassi Viewer', layout_with_toolbar, resizable=False)

        return window

    def show_gui(self, window: sg.Window):

        font_filepath = None
        output_name = None
        exists_choice = None

        sg.popup('The whole program is WIP.',
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

                        layout_p = layout_popup()
                        popup_3_choice = sg.Window(
                            title='', no_titlebar=True, layout=layout_p.layout, resizable=False)
                        event_popup, values_popup = popup_3_choice.read()

                        while event_popup != '-OVERWRITE-' or event_popup != '-EXPICIT-' or event_popup != '-SKIP-':
                            if event_popup == '-OVERWRITE-':
                                exists_choice = OB.OVERWWRITE
                                break
                            if event_popup == '-EXPICIT-':
                                exists_choice = OB.RANDOM_NAME
                                break
                            if event_popup == '-SKIP-':
                                exists_choice = OB.SKIP
                                break
                            if event == sg.WIN_CLOSED or event == 'Quit':
                                break
                        popup_3_choice.close()
                        try:
                            file_path = os.path.join(
                                values["-JAVA FOLDER-"],
                            )
                            output_path = values['-OUTPUT FOLDER-']
                            if output_name is None:
                                sg.popup_auto_close(
                                    'You didn\'t set a name for the image, it will be named randomly.')
                                output_name = secrets.token_hex(16)

                            nassi(input_path=file_path, output_path=output_path, outputname=output_name, gui=self,
                                  font_filepath=font_filepath, behaviour=exists_choice)

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
                        except Exception as e:
                            logging.error(
                                ('Failed to create Image with values = ' + str(values)))
                            sg.popup_error(('Failed to create an image of one funktion correctly. ' + str(e)) + 'There may be some images created. ')
                        except:    
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
                except FileNotFoundError:
                    sg.popup_error('FileNotFoundError',
                                   title='FileNotFoundError',)
                except Exception as e:
                    sg.popup_cancel(str(e), title='Error')
                    logging.error('Try to open a .png. {e}')
                except:
                    logging.error('Try to open a .png. Unknown error.')
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

            # output view

            if event == '-REFRESH-':
                try:
                    fnames = output(values)
                    window['-OUTPUT FILE LIST-'].update(fnames)
                except NoPathError:
                    pass
                    sg.popup_error('You dont set an output path. Try again.')
                except:
                    pass

        window.close()
        if exists_choice:
            popup_3_choice.close()
