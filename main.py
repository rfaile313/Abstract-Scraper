__author__ = "@pallav_routh, @rfaile313"
__copyright__ = "© Copyright 2020"
__credits__ = ["Pallav Routh", "Rudy Faile"]
__license__ = "GPL"
__version__ = "1.0.1"

__email__ = "pallav.routh@utsa.edu"
__status__ = "Development"

from settingsGUI import SettingsMenu
from requestLogic import ScanForResults

def settings():
    #instantiate settings gui
    settings = SettingsMenu(__version__)
    #run settings GUI and return values into variables
    setting_event, setting_value = settings.create_settings_window()

    #instantiate RequestLogic Object
    scan = ScanForResults()

    #Value[0] is search string / 1-8 are journals/9 is year/10 is sort
    if setting_value[1] == True:
        scan.search_sort(setting_value[0], 'jams', setting_value[9], setting_value[10])
        jams = scan.get_max_results(scan.journal)
        print(jams)#returned value for use #debugging
    if setting_value[2] == True:
        scan.search_sort(setting_value[0], 'jm', setting_value[9], setting_value[10])
        jm = scan.get_max_results(scan.journal)
        print(jm)#returned value for use #debugging
    if setting_value[3] == True:
        scan.search_sort(setting_value[0], 'jmr', setting_value[9], setting_value[10])
        jmr = scan.get_max_results(scan.journal)
        print(jmr)#returned value for use #debugging
    if setting_value[4] == True:
        scan.search_sort(setting_value[0], 'mktsc', setting_value[9], setting_value[10])
        mktsc = scan.get_max_results(scan.journal)
        print(mktsc)#returned value for use #debugging
    if setting_value[5] == True:
        scan.search_sort(setting_value[0], 'mgmtsc', setting_value[9], setting_value[10])
        mgmtsc = scan.get_max_results(scan.journal)
        print(mgmtsc)#returned value for use #debugging
    if setting_value[6] == True:
        scan.search_sort(setting_value[0], 'asq', setting_value[9], setting_value[10])
        asq = scan.get_max_results(scan.journal)
        print(asq)#returned value for use #debugging
    if setting_value[7] == True:
        scan.search_sort(setting_value[0], 'aomj', setting_value[9], setting_value[10])
        aomj = scan.get_max_results(scan.journal)
        print(aomj)#returned value for use #debugging
    if setting_value[8] == True:
        scan.search_sort(setting_value[0], 'aomr', setting_value[9], setting_value[10])
        aomr = scan.get_max_results(scan.journal)
        print(aomr)#returned value for use #debugging
        

def main():
    settings()

if __name__ == '__main__':
    main()

