from settingsGUI import settings_menu
from requestLogic import search_sort

VERSION='1.0'




def main():
    event, value = settings_menu(VERSION)
    print(event, value)
    search_sort(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10])
    
if __name__ == '__main__':
    main()