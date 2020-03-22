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
        print(jams)#returned value for use #debugging
    if setting_value[2] == True:
        jm = search_sort(setting_value[0], 'jm', setting_value[9], setting_value[10])
        print(jm)#returned value for use #debugging
    if setting_value[3] == True:
        jmr = search_sort(setting_value[0], 'jmr', setting_value[9], setting_value[10])
        print(jmr)#returned value for use #debugging
    if setting_value[4] == True:
        mktsc = search_sort(setting_value[0], 'mktsc', setting_value[9], setting_value[10])
        print(mktsc)#returned value for use #debugging
    if setting_value[5] == True:
        mgmtsc = search_sort(setting_value[0], 'mgmtsc', setting_value[9], setting_value[10])
        print(mgmtsc)#returned value for use #debugging
    if setting_value[6] == True:
        asq = search_sort(setting_value[0], 'asq', setting_value[9], setting_value[10])
        print(asq)#returned value for use #debugging
    if setting_value[7] == True:
        aomj = search_sort(setting_value[0], 'aomj', setting_value[9], setting_value[10])
        print(aomj)#returned value for use #debugging
    if setting_value[8] == True:
        aomr = search_sort(setting_value[0], 'aomr', setting_value[9], setting_value[10])
        print(jams)#returned value for use #debugging
    

if __name__ == '__main__':
    main()

'''
# marketing journals
setting_value[1] 'jams': 'Journal of Academy of Marketing Science',
setting_value[2] 'jm': 'Journal of Marketing',
setting_value[3] 'jmr': 'Journal of Marketing Research',
setting_value[4] 'mktsc': 'Marketing Science',
setting_value[5] 'mgmtsc': 'Management Science',
# management journals
setting_value[6] 'asq':'Administrative Science Quarterly',
setting_value[7] 'aomj':'Academy of Management Journal',
setting_value[8] 'aomr':'Academy of Management Review'}
'''