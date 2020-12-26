from gui.utils import nassi, output
import PySimpleGUI as sg
import os.path
import random
import logging


class gui:

    def __init__(self, theme: str, debug_mode: bool):
        self.get_debug_mode(mode=debug_mode)
        window = self.init_gui(theme=theme)
        self.show_gui(window=window)

    def get_debug_mode(self, mode: bool):
        loging_level = logging.INFO
        if mode:
            loging_level = logging.DEBUG
        logging.basicConfig(level=loging_level)

    def init_gui(self, theme: str):
        sg.theme(theme)
        logging.info(('Theme = ' + theme))

        java_file_list_column = [
            [
                sg.Text('Java File'),
                sg.In(size=(25, 1), enable_events=True, key="-JAVA FOLDER-"),
                sg.FileBrowse(file_types=(('Java-File', '*.java'), ('ALL Files',
                                                                    '*.*')), key='-JAVA FILE-'),  # ('ALL Files','*.*')
            ],
        ]
        logging.info('set java_file_list_column GUI')

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
        logging.info('set file_list_column GUI')

        diagramm_viewer_column = [
            [sg.Text("Choose your Code for preview. ", size=(100, 10))],
            [sg.Text(size=(40, 1), key="-TOUT-")],
            [sg.Image(key='-IMAGE-')],
        ]
        logging.info('set diagramm_viewer_column GUI')

        buttons_column = [
            [sg.Button(button_text='Create Image', key='-CREATE-')],
            # * fun feature
            [sg.Button(button_text='Donate', key='-DONATE-')],
        ]
        logging.info('set buttons_column GUI')

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
        logging.info('init layout GUI')

        window = sg.Window('Nassi Viewer', layout, resizable=True)
        return window

    def show_gui(self, theme: str, window: sg.Window):

        while True:
            event, values = window.read()
            if event == 'Exit' or event == sg.WIN_CLOSED:
                logging.info(('event = ' + str(event)))
                break

            if event == '-DONATE-':
                logging.info(('event = ' + str(event)))
                sg.popup_notify(
                    ('You donated $' + str(random.randint(500, 100000000)) + '.'), title='Thanks')

            if event == '-OUTPUT FOLDER-':
                logging.info(('event = ' + str(event) + ' value = ' + str(values['-OUTPUT FOLDER-'])))
                fnames = output(values)
                window['-OUTPUT FILE LIST-'].update(fnames)
            elif event == '-OUTPUT FILE LIST-':
                logging.info(('event = ' + str(event) + ' value = ' + str(values['-OUTPUT FILE LIST-'])))
                try:
                    filename = os.path.join(
                        values["-OUTPUT FOLDER-"], values["-OUTPUT FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except:
                    pass
            if event == '-JAVA FOLDER-':
                logging.info(('event = ' + str(event) + ' value = ' + str(values['-JAVA FOLDER-'])))
                folder = values['-JAVA FOLDER-']
                window['-JAVA FOLDER-'].update(values['-JAVA FILE-'])

            elif event == '-CREATE-':
                logging.info(('event = ' + str(event) + 'values = ' + str(values)))
                try:
                    if values['-JAVA FOLDER-'] and values['-OUTPUT FOLDER-']:
                        logging.info(('Try create Image with values = ' + str(values)))
                        try:
                            file_path = os.path.join(
                                values["-JAVA FOLDER-"],
                            )
                            output_path = values['-OUTPUT FOLDER-']
                            nassi(file_path, output_path)

                            fnames = output(values)
                            window['-OUTPUT FILE LIST-'].update(fnames)
                            sg.popup_notify('Succsessful created!',
                                            title='Created')

                        except:
                            logging.error(('Failed to create Image with values = ' + str(values)))
                            pass

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

        window.close()
