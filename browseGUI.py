import PySimpleGUI as sg
from constants import Constants

class BrowseGUI:

    def __init__(self):
        sg.theme('LightGrey5')
        self.layout = []

    def append_journal(self, text, journalName, journalKey):
        #Append Journal Text, Name, and Key specified in call to the laout
        self.layout.append([sg.Frame(layout=[
        [sg.Text('Results:', justification='center')], 
        [sg.Text(text)],
        [sg.Button('Browse Abstracts from this Journal', key=journalKey)],
        [sg.Text('_' * 60)]
        ], title=journalName,title_color='black', relief=sg.RELIEF_SUNKEN)])
        
    def create_window(self):
        
        #Append Buttom Buttons
        self.layout.append([sg.Frame(layout=[
        [sg.Button('Search a Different Term', key='anotherSearch', button_color=('white','springgreen4')), sg.Button('Quit', key='choseQuit', button_color=('white','firebrick3'))],
        ], title='More Options:', relief=sg.RELIEF_FLAT)]
        )
        
        #create layout with journals from append_journal
        self.window = sg.Window('Search Results', self.layout, icon=None)

        event, values = self.window.read()
        return event, values
        
    def close_window(self):
        self.window.close()
  

