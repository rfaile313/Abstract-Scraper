import PySimpleGUI as sg

class ProgressGUI:

    def __init__(self):
    # layout the Window
        self.layout = [[sg.Text('A custom progress meter')],
                      [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
                      [sg.Cancel()]]

        # create the Window
        self.window = sg.Window('Custom Progress Meter', self.layout)

    def progress_event_loop(self):
        # loop that would normally do something useful
        for i in range(1000):
            # check to see if the cancel button was clicked and exit loop if clicked
            event, values = self.window.read(timeout=10)
            if event == 'Cancel' or event is None:
                break
                # update bar with loop value +1 so that bar eventually reaches the maximum
            self.window['progbar'].update_bar(i + 1)
        # done with loop... need to destroy the window as it's still open
        self.window.close()
