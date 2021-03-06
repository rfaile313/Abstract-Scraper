import PySimpleGUI as sg
from constants import Constants

class SettingsMenu:

    def __init__(self, version):

        self.version = version
        #GreenTan
        #BrownBlue
        sg.theme('LightGrey5')

    def create_settings_window(self):
        #inline comments with ## are returned dictionary values
        layout = [
            
            [sg.Text('Abstract Search Settings', size=(30, 1), justification='center', font=("Helvetica", 20), relief=sg.RELIEF_RIDGE)],
            [sg.Text('Enter search term:')],
            [sg.InputText('')], ##0 - string

            #Marketing Journal Checkboxes
            [sg.Frame(layout=[
            [sg.Checkbox(Constants.j_title_list[0], default=True),##1 True/False
            sg.Checkbox(Constants.j_title_list[1])],##2 True/False
            [sg.Checkbox(Constants.j_title_list[2]),##3 True/False
            sg.Checkbox(Constants.j_title_list[3]),##4 True/False
            sg.Checkbox(Constants.j_title_list[4])],##5 True/False
            
            ], title='Marketing Journals',title_color='black', relief=sg.RELIEF_SUNKEN)],
            
            #Management Journal Chckboxes
            [sg.Frame(layout=[
            [sg.Checkbox(Constants.j_title_list[5]),##6 True/False  
            sg.Checkbox(Constants.j_title_list[6])],##7 True/False
            [sg.Checkbox(Constants.j_title_list[7])],##8 True/False
            
            ], title='Management Journals',title_color='black', relief=sg.RELIEF_SUNKEN)],
            
            [sg.Text('Search from which year until today?')],
            [sg.Frame('    Year        From',[[
            sg.Slider(range=(1959, 2019), orientation='v', size=(5, 30), default_value=2016, tick_interval=20)]])],##9 ayeartag

            [sg.Frame(layout=[
            [sg.Radio('Most Relevant', "sortBy",default=True), sg.Radio('Date', "sortBy")]], title='Sort by',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Sort by Most Relevant(Default) or by Date')], ##10 True (MR)/ 11 False(Date)
        

            [sg.Text('_' * 29)],

            [sg.Submit(tooltip='Click to Submit'), sg.Cancel()]]

        #Make Window
        window = sg.Window('Abstract Scraper v{}'.format(self.version), layout, default_element_size=(40, 1), grab_anywhere=False, icon=None)
        event, values = window.read()

        #Means they clicked X or Cancel
        if event is None or event is 'Cancel':
            exit()

        #Means they didn't enter a search value
        if values[0] is '':
            sg.Popup('Wait!', 'Please Enter a Search Value')
            SettingsMenu.create_settings_window(self.version)
        
        window.close()

        return event, values