__author__ = "@rfaile313, @pallav_routh"
__copyright__ = "© Copyright 2020"
__credits__ = ["Rudy Faile", "Pallav Routh"]
__license__ = "GPL"
__version__ = "1.0.2"
__status__ = "Development"

#Standard lib imports
import time
#Internal imports
from settingsGUI import SettingsMenu
from requestLogic import ScanForResults
from browseGUI import BrowseGUI
from constants import Constants
from CustomProgressMeter import CustomProgressMeter

#instantiate RequestLogic object to handle requests
scan = ScanForResults()

#instantiate BrowserGUI object in order to insert journals into layout:
browse = BrowseGUI()

# Helper functions for the main loop. Can probably be teased out into other files
# But would need to use the created objects above in a different way
def search_and_append(keys, loop):
    #Value[0] is search string / 1-8 are journals/9 is year/10 is sort
    scan.search_sort(keys[0], Constants.journal_abbrv_list[loop-1], keys[9], keys[10])
    journal = scan.get_max_results(scan.journal)
    browse.append_journal(journal, Constants.j_title_list[loop-1], Constants.journal_keys[loop-1])
    
def parse_selections(keys):
    #create progress bar
    progress = CustomProgressMeter(8, 'Checking Journals')
    for i in range(1,9):
        if keys[i]:
            progress.progress_increase(i, Constants.j_title_list[i-1])
            search_and_append(keys, i)
        else:
            progress.progress_increase(i, 'Finishing up...')
            time.sleep(0.2)
    #kill window
    progress.close_window()
# End helper functions--------------

def main():
    #instantiate settings gui
    settings = SettingsMenu(__version__)
    #run settings GUI and return values into variables
    setting_event, setting_value = settings.create_settings_window()

    #check for results and append them to next gui
    parse_selections(setting_value)

    #run settings GUI and return values into variables
    browse_event, browse_value = browse.create_window()
    #browse_value doesnt return anything right now because theres no input
    #browse_event returns the -KEY- inserted in browse.append_journal above which is the journal that needs to be searched for abstracts. 
    print('Event:', browse_event)
    print('Values:', browse_value)
        
if __name__ == '__main__':
    main()

