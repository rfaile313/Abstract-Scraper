import PySimpleGUI as sg

#GreenTan
#BrownBlue
sg.ChangeLookAndFeel('LightGrey5')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

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
'aomr':'Academy of Management Review'
'''

version='1.0'


layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Abstract Scraper v{}'.format(version), size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Enter search term:')],
    [sg.InputText('')],

    #Marketing Journal Checkboxes
    [sg.Frame(layout=[
    [sg.Checkbox('Journal of Academy of Marketing Science', default=True),  
    sg.Checkbox('Journal of Marketing'),
    sg.Checkbox('Journal of Marketing Research'),
    sg.Checkbox('Marketing Science'),
    sg.Checkbox('Management Science')],
    
    
    ], title='Marketing Journals',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    
    #Management Journal Chckboxes
    [sg.Frame(layout=[
    [sg.Checkbox('Administrative Science Quarterly', default=True),  
    sg.Checkbox('Academy of Management Journal'),
    sg.Checkbox('Academy of Management Review')],
    

    ], title='Management Journals',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    

    [sg.Text('Year range to Search')],
    [sg.Frame('    Year         From              To',[[
     sg.Slider(range=(1970, 2020), orientation='v', size=(5, 20), default_value=1970, tick_interval=20),
     sg.Slider(range=(1970, 2020), orientation='v', size=(5, 20), default_value=2020)]])],

    [sg.Frame(layout=[
    [sg.Radio('Most Relevant', "sortBy",default=True), sg.Radio('Date', "sortBy")]], title='Sort by',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='tooltip text')],
   


    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder to Save the results to')],
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to search'), sg.Cancel()]]

window = sg.Window('Abstract Scraper', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
window.close()

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)