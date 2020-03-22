import PySimpleGUI as sg


class ResultSelector:

    def __init__(self):
        sg.theme('LightGrey5')

        self.journal_titles = [
            'Journal of Academy of Marketing Science',
            'Journal of Marketing',
            'Journal of Marketing Research',
            'Marketing Science',
            'Management Science',
            'Administrative Science Quarterly',
            'Academy of Management Journal',
            'Academy of Management Review']

        self.journal_keys = [
            '-JAMS-',
            '-JM-',
            '-JMR-',
            '-MKTSC-',
            '-MGMTSC-',
            '-ASQ-',
            '-AOMJ-',
            '-AOMR-']

    def create_window(self):
        
        self.layout = []

        for i in range(8):
            self.layout.append([sg.Frame(layout=[
            [sg.Text('Results Found:', justification='center')], 
            [sg.Text('Loading....', key=self.journal_keys[i], justification='center')],
            [sg.Text('_' * 30)]
            ], title=self.journal_titles[i],title_color='black', relief=sg.RELIEF_SUNKEN)])


        self.count = 1
        self.viewport = sg.Window('Checking for results', self.layout, grab_anywhere=False)


#test in file:


'''
result_selector = ResultSelector()

result_selector.create_window()


while True:             # Event Loop
    event, values = result_selector.viewport.read(timeout=1000)
    if event is None:
        break
    result_selector.viewport['-AOMR-'].update(result_selector.count)
    result_selector.count += 1
'''
    
## end test

'''
count = 0

while True:             # Event Loop
    event, values = window.read(timeout=20)
    if event is None:
        break
    count += 1 
    window['-JAMS-'].update(count)
'''

'''
        self.layout = [

            [sg.Frame(layout=[
            [sg.Text('Results Found:', justification='center')], 
            [sg.Text('Loading....', key=self.jkey, justification='center')],
            ], title=self.jname,title_color='black', relief=sg.RELIEF_SUNKEN)]

            ]
'''