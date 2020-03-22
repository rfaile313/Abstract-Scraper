__author__ = "@pallav_routh, @rfaile313"
__copyright__ = "© Copyright 2020"
__credits__ = ["Pallav Routh", "Rudy Faile"]
__license__ = "GPL"
__version__ = "1.0.1"

__email__ = "pallav.routh@utsa.edu"
__status__ = "Development"

from settingsGUI import settings_menu
from requestLogic import search_sort

def main():
    setting_event, setting_value = settings_menu(__version__) #events,values from settingsGUI.py returned in dictionary
    #print(event, value) #debugging dictionary results returned from settingsGUI.py
    #Value[0] is search string / 1-8 are journals/9 is year/10 is sort
    if setting_value[1] == True:
        jams = search_sort(setting_value[0], 'jams', setting_value[9], setting_value[10])
    if setting_value[2] == True:
        jm = search_sort(setting_value[0], 'jm', setting_value[9], setting_value[10])
    if setting_value[3] == True:
        jmr = search_sort(setting_value[0], 'jmr', setting_value[9], setting_value[10])
    if setting_value[4] == True:
        mktsc = search_sort(setting_value[0], 'mktsc', setting_value[9], setting_value[10])
    if setting_value[5] == True:
        mgmtsc = search_sort(setting_value[0], 'mgmtsc', setting_value[9], setting_value[10])
    if setting_value[6] == True:
        asq = search_sort(setting_value[0], 'asq', setting_value[9], setting_value[10])
    if setting_value[7] == True:
        aomj = search_sort(setting_value[0], 'aomj', setting_value[9], setting_value[10])
    if setting_value[8] == True:
        aomr = search_sort(setting_value[0], 'aomr', setting_value[9], setting_value[10])
    

if __name__ == '__main__':
    main()

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