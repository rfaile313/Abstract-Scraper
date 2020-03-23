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
        [sg.Text(text, key=journalKey, justification='center')],
        [sg.Button('Browse Abstracts from this Journal')],
        [sg.Text('_' * 60)]
        ], title=journalName,title_color='black', relief=sg.RELIEF_SUNKEN)])
        
    def create_window(self):
        #create layout with journals from append_journal
        self.window = sg.Window('Search Results', self.layout, icon=Constants.spyglass_base_64)

        event, values = self.window.read()
        return event, values
        
    def close_window(self):
        self.window.close()
  

