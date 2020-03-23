__author__ = "@pallav_routh, @rfaile313"
__copyright__ = "© Copyright 2020"
__credits__ = ["Pallav Routh", "Rudy Faile"]
__license__ = "GPL"
__version__ = "1.0.1"

__email__ = "pallav.routh@utsa.edu"
__status__ = "Development"

from settingsGUI import SettingsMenu
from requestLogic import ScanForResults
from browseGUI import BrowseGUI
from constants import Constants
from pleaseWaitGUI import *

def main():
    #instantiate settings gui
    settings = SettingsMenu(__version__)
    #run settings GUI and return values into variables
    setting_event, setting_value = settings.create_settings_window()

    #TODO Please wait window probably a nice thing to have here:
    show_loading()
    #instantiate RequestLogic Object
    scan = ScanForResults()

    #instantiate BrowserGUI in order to insert journals into layout:
    browse = BrowseGUI()

    #Value[0] is search string / 1-8 are journals/9 is year/10 is sort
    if setting_value[1] == True:
        scan.search_sort(setting_value[0], 'jams', setting_value[9], setting_value[10])
        jams = scan.get_max_results(scan.journal)
        browse.append_journal(jams, Constants.journal_titles[0], Constants.journal_keys[0])
    if setting_value[2] == True:
        scan.search_sort(setting_value[0], 'jm', setting_value[9], setting_value[10])
        jm = scan.get_max_results(scan.journal)
        browse.append_journal(jm, Constants.journal_titles[1], Constants.journal_keys[1])
    if setting_value[3] == True:
        scan.search_sort(setting_value[0], 'jmr', setting_value[9], setting_value[10])
        jmr = scan.get_max_results(scan.journal)
        browse.append_journal(jmr, Constants.journal_titles[2], Constants.journal_keys[2])
    if setting_value[4] == True:
        scan.search_sort(setting_value[0], 'mktsc', setting_value[9], setting_value[10])
        mktsc = scan.get_max_results(scan.journal)
        browse.append_journal(mktsc, Constants.journal_titles[3], Constants.journal_keys[3])
    if setting_value[5] == True:
        scan.search_sort(setting_value[0], 'mgmtsc', setting_value[9], setting_value[10])
        mgmtsc = scan.get_max_results(scan.journal)
        browse.append_journal(mgmtsc, Constants.journal_titles[4], Constants.journal_keys[4])
    if setting_value[6] == True:
        scan.search_sort(setting_value[0], 'asq', setting_value[9], setting_value[10])
        asq = scan.get_max_results(scan.journal)
        browse.append_journal(asq, Constants.journal_titles[5], Constants.journal_keys[5])
    if setting_value[7] == True:
        scan.search_sort(setting_value[0], 'aomj', setting_value[9], setting_value[10])
        aomj = scan.get_max_results(scan.journal)
        browse.append_journal(aomj, Constants.journal_titles[6], Constants.journal_keys[6])
    if setting_value[8] == True:
        scan.search_sort(setting_value[0], 'aomr', setting_value[9], setting_value[10])
        aomr = scan.get_max_results(scan.journal)
        browse.append_journal(aomr, Constants.journal_titles[7], Constants.journal_keys[7])
    
    remove_loading()
    #run settings GUI and return values into variables
    browse_event, browse_value = browse.create_window()
    #browse_value doesnt return anything right now because theres no input
    #browse_event returns the -KEY- inserted in browse.append_journal above.
    print('Event:', browse_event)
    print('Values:', browse_value)
        

if __name__ == '__main__':
    main()

