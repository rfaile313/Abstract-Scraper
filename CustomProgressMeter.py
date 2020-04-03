import PySimpleGUI as sg

class CustomProgressMeter:

    def __init__(self, max_value, title):
        # (int max_value, string title)
        #Set params and values
        self.max_value = max_value
        self.title = title
        self.layout = [[sg.Text('Searching:                                                                       ', key='progtext')],
                      [sg.ProgressBar(self.max_value, orientation='h', size=(40, 20), key='progbar')],
                      [sg.Cancel()]]

        #Create the Window
        self.window = sg.Window(self.title, self.layout, size=(400,100))

    def progress_increase(self, amount, text):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = self.window.read(timeout=0)
        if event == 'Cancel' or event is None:
            exit()
        #update bar with set amount
        self.window['progbar'].update_bar(amount)
        self.window['progtext'].update('Searching: {}'.format(text))

    def close_window(self):
        self.window.close()


