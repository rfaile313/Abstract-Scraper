import PySimpleGUI as sg


class ResultSelector:

    def __init__(self):
        sg.theme('LightGrey5')


    def create_window(self, jname, jkey):
        
        self.jname = jname
        self.jkey = jkey
        self.layout = [ 
        
        [sg.Frame(layout=[
        [sg.Text('Results Found:', justification='center')], 
        [sg.Text('Loading....', key=jkey, justification='center')],
        ], title=jname,title_color='black', relief=sg.RELIEF_SUNKEN)],

        ]

        #self.count = 0
        self.window = sg.Window('Checking for results', self.layout, grab_anywhere=False)



    def update_window(self, key, update):
        pass
'''
count = 0

while True:             # Event Loop
    event, values = window.read(timeout=20)
    if event is None:
        break
    count += 1 
    window['-JAMS-'].update(count)
'''

find_results_GUI = ResultSelector()

find_results_GUI.create_window('Journal of X', '-JAMS-')


while True:             # Event Loop
    event, values = find_results_GUI.window.read(timeout=20)
    if event is None:
        break
    #find_results_GUI.count += 1 
    #find_results_GUI.window[find_results_GUI.jkey].update(find_results_GUI.count)

'''
# marketing journals
                        'jams': 'Journal of Academy of Marketing Science',
                        'jm': 'Journal of Marketing',
                        'jmr': 'Journal of Marketing Research',
                        'mktsc': 'Marketing Science',
                        'mgmtsc': 'Management Science',
                        # management journals
                        'asq':'Administrative Science Quarterly',
                        'aomj':'Academy of Management Journal',
                        'aomr':'Academy of Management Review'}
'''