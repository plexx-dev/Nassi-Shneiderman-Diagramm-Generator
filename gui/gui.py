from gui.utils import nassi, output
from gui.new_window_layouts import Layout_popup, Layout_std
from errors.custom import JavaSyntaxError, ScopeNotFoundException, InterpreterException, NoPathError
from interpreter.NassiShneidermann import OB

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

        layout_s = Layout_std(theme=theme)
        layoutStd = layout_s.layout()
        window = sg.Window('Nassi Viewer', layoutStd, resizable=False)

        return window

    def show_gui(self, window: sg.Window):

        font_filepath = None
        output_name = None
        exists_choice = None
        types = None
        comments = None
        modifier = None

        sg.popup('The whole program is WIP.',
                 auto_close=True, auto_close_duration=5)

        while True:
            logging.info('test')
            event, values = window.read()

            if event == 'Exit' or event == sg.WIN_CLOSED:
                logging.debug(('Exit GUI'))
                break

            # toolbar
            if event == '-CREATE-':
                logging.debug(('event = ' + str(event) +
                               'values = ' + str(values)))
                try:
                    if values['-JAVA FOLDER-'] and values['-OUTPUT FOLDER-']:
                        logging.debug(
                            ('Try create Image with values = ' + str(values)))

                        layout_p = Layout_popup()
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
                                  font_filepath=font_filepath, behaviour=exists_choice, types=types, remove_tags=modifier, comments=comments)

                            fnames = output(values['-OUTPUT FOLDER-'])
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
                        sg.popup_annoying('No Output', title='Error',
                                          auto_close_duration=5, auto_close=True)
                    elif values['-OUTPUT FOLDER-']:
                        sg.popup_annoying('No Input', title='Error',
                                          auto_close_duration=5, auto_close=True)
                    else:
                        logging.error('Unexpected Case!')
                        sg.popup_annoying('Unexpected Case!', title='Error')
                except:
                    pass

            if event == '-CREDITS-':
                sg.popup(
                    'This was made by plexx(Image generation), Weckyy702(Interpreter) and oleting(Frontend). Used Python 3.9.1, Libraries PySimpleGUI and Pillow.', title='Credits')

            if event == '-DONATE-':
                logging.debug(('event = ' + str(event)))
                sg.popup_notify(
                    ('You donated $' + str(random.randint(500, 100000000)) + '.'), title='Thanks')


            # needed Input

            if event == '-OUTPUT FOLDER-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-OUTPUT FOLDER-'])))
                fnames = output(values['-OUTPUT FOLDER-'])
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

            if event == '-OUTPUT NAME-':
                output_name = values['-OUTPUT NAME-']

            if event == '-TTF FOLDER-':
                logging.debug(('event = ' + str(event) +
                               ' value = ' + str(values['-TTF FOLDER-'])))
                folder = values['-TTF FOLDER-']
                window['-TTF FOLDER-'].update(values['-TTF FILE-'])
                font_filepath = values['-TTF FILE-']

            if event == '-TYPES-':
                # 
                raw_types = sg.popup_get_text('Enter customn keywords (int, double, ...): ', default_text=types)
                try:
                    raw_types = raw_types.replace(' ', '')
                    types = raw_types.split(',')
                except:
                    sg.popup('You do not hit "Enter"')
                
            if event == '-MODIFIER-':
                raw_modifier = sg.popup_get_text('Enter customn modifier (public, private, ...): ', default_text=modifier)
                try:
                    raw_modifier = raw_modifier.replace(' ', '')
                    modifier = raw_modifier.split(',')
                except:
                    sg.popup('You do not hit "Enter"')

            if event == '-COMMENTS-':
                raw_comments = sg.popup_get_text('Enter customn comments (//, #, ...): ', default_text=comments)
                try:
                    raw_comments = raw_comments.replace(' ', '')
                    comments = raw_comments.split(',')
                except:
                    sg.popup('You do not hit "Enter"')
            # output view

            if event == '-REFRESH-':
                try:
                    fnames = output(values['-OUTPUT FOLDER-'])
                    window['-OUTPUT FILE LIST-'].update(fnames)
                except NoPathError:
                    pass
                    sg.popup('You dont set an output path. Try again.')
                except:
                    pass

        window.close()
        if exists_choice:
            popup_3_choice.close()
