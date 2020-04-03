from datetime import datetime
import requests
from bs4 import BeautifulSoup
import itertools
import re

while True:
    print('\n***********************************************************************')
    print('*************************Abstract Fetcher 3.0**************************')
    print('***********************************************************************')
    print('Written with love by Pallav Rt. Python Version: 3.7.3')
    print('Report bugs at: pallav.routh@utsa.edu')

    ''' Search query '''
    input_search_term = input('\nEnter search term: ')

    search_tag = input_search_term

    ''' Filtering '''
    input_after_year = input('\nEnter year after: ')

    if len(input_after_year) == 0:
        print('Error! Wrong input...defaulting to 1935')
        after_year_tag = str(1935)
    else:
        if int(input_after_year) < 1935:
            print('Minimum input date is 1935...defaulting to this value')
            after_year_tag = str(1935)
        elif int(input_after_year) > datetime.today().year:
            print('Maximum input date is ' + str(datetime.today().year - 1) + '...defaulting to this value')
            after_year_tag = str(2018)
        else:
            after_year_tag = input_after_year
        
    ''' Sorting Filtered results '''
    input_sort_by = input('\nWhat would you like to sort by?Please pick one of the following - mr (most relevant) or date (by date descending): ')

    allowed_sort_by = ['mr', 'date']

    if input_sort_by not in allowed_sort_by:
        print('Error! Wrong input...defaulting to relevancy')
        sort_by_tag = 'relevancy'
    elif input_sort_by == 'mr':
        sort_by_tag = 'relevancy'
        sort_by_tag_jams = 'relevance'
    elif input_sort_by == 'date':
        sort_by_tag = 'Ppub'
        sort_by_tag_jams = 'newestFirst'


    j_title_dict = {# marketing journals
                     'jams': 'Journal of Academy of Marketing Science',
                     'jm': 'Journal of Marketing',
                     'jmr': 'Journal of Marketing Research',
                     'mktsc': 'Marketing Science',
                     'mgmtsc': 'Management Science',
                     # management journals
                     'asq':'Administrative Science Quarterly',
                     'aomj':'Academy of Management Journal',
                     'aomr':'Academy of Management Review'}

    allowed_journal_tags = ['jm', 'jmr', 'mktsc', 'mgmtsc', 'jams', 'asq', 'aomj','aomr']

    payload = {# marketing journals
               'jm': {'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag},
               'jmr': {'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag},
               'mktsc': {'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag},
               'mgmtsc': {'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag},
               'jams': {'query': search_tag, 'date-facet-mode': 'between', 'facet-start-year': after_year_tag,'previous-start-year': '1975', 'facet-end-year': '2019', 'previous-end-year': '2019','sortOrder': sort_by_tag_jams},
               # management journals
               'aomj': {'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag},
               'aomr':{'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag},
               'asq': {'text1': search_tag, 'AfterYear': after_year_tag, 'sortBy': sort_by_tag}}

    base_url_dict = {# marketing journals
                 'jm': 'https://journals.sagepub.com/action/doSearch?&publication=jmxa',
                 'jmr': 'https://journals.sagepub.com/action/doSearch?&publication=mrja',
                 'mktsc': 'https://pubsonline.informs.org/action/doSearch?&publication[]=mksc',
                 'mgmtsc': 'https://pubsonline.informs.org/action/doSearch?&publication[]=mnsc',
                 'jams': 'https://link.springer.com/search?search-within=Journal&facet-journal-id=11747',
                 # management journals
                 'aomj': 'https://journals.aom.org/action/doSearch?&publication[]=amj',
                 'aomr': 'https://journals.aom.org/action/doSearch?&publication[]=amr',
                 'asq': 'https://journals.sagepub.com/action/doSearch?&publication=asqa'}


    def url_builder(journal, search_tag, after_year_tag, sort_by_tag):
        return (requests.get(base_url_dict[journal], params=payload[journal]).url)


    ''' Get max results for each website one by one '''


    def get_max_results(journal):
        url = url_builder(journal, search_tag, after_year_tag, sort_by_tag)
        html = requests.get(url).text
        soup = BeautifulSoup(html, features="html.parser")
        # marketing journals
        if journal == 'mktsc' or journal == 'mgmtsc':
            if soup.find('span', {'class': 'result__count'}) is not None:
                total_hits = soup.find('span', {'class': 'result__count'}).text
                print('Total number of results returned for', j_title_dict[journal], ' is ', total_hits)
            else:
                total_hits = '0'
                print('There was 0 total results')
            return (int(total_hits))
        elif journal == 'jm' or journal == 'jmr':
            if soup.find('div', {'class': 'paginationStatus'}) is not None:
                total_hits = soup.find('div', {'class': 'paginationStatus'}).text.split()
                print('Total number of results returned for journal', j_title_dict[journal], ' is ', total_hits[-1])
            else:
                total_hits = ['0']
                print('There was 0 total results')
            return (int(total_hits[-1]))
        elif journal == 'jams':
            if soup.find('div', {'class': 'header'}) is not None:
                total_hits = soup.find('div', {'class': 'header'}).text.split()
                print('Total number of results returned for', j_title_dict[journal], ' is ', total_hits[0])
            else:
                total_hits = ['0']
                print('There was 0 total results')
            return (int(total_hits[0]))
        # management journals
        elif journal == 'aomj' or journal == 'aomr':
            if soup.find('span', {'class': 'result__count'}) is not None:
                total_hits = soup.find('span', {'class': 'result__count'}).text
                print('Total number of results returned for', j_title_dict[journal], ' is ', total_hits)
            else:
                total_hits = '0'
                print('There was 0 total results')
            return (int(total_hits))
        elif journal == 'asq':
            if soup.find('div', {'class': 'paginationStatus'}) is not None:
                total_hits = soup.find('div', {'class': 'paginationStatus'}).text.split()
                print('Total number of results returned for journal', j_title_dict[journal], ' is ', total_hits[-1])
            else:
                total_hits = ['0']
                print('There was 0 total results')
            return (int(total_hits[-1]))
        


    ''' Get search results from other pages '''


    def crawler(journal, list_of_pages):
        ''' container for search urls '''
        search_urls = []
        ''' data for the function '''
        payload = {'query': search_tag, 'date-facet-mode': 'between', 'facet-start-year': after_year_tag,
                   'previous-start-year': '1975', 'facet-end-year': '2019', 'previous-end-year': '2019',
                   'sortOrder': sort_by_tag_jams}
        ''' Easier to build it this way for these journals'''
        if journal != 'jams':
            for page in list_of_pages:
                url = url_builder(journal, search_tag, after_year_tag, sort_by_tag) + '&startPage=' + str(page)
                search_urls.append(url)
        else:
            modified_base_url = [
                'https://link.springer.com/search/page/' + str(pg) + '?search-within=Journal&facet-journal-id=11747' for pg
                in list_of_pages]
            for link in modified_base_url:
                url = requests.get(link, params=payload).url
                search_urls.append(url)
        return search_urls


    ''' Abstract stats '''

    def get_distance(w1, w2, words):
            if w1 in words and w2 in words:
                    w1_indexes = [index for index, value in enumerate(words) if value == w1]
                    w2_indexes = [index for index, value in enumerate(words) if value == w2]
                    distances = [abs(item[0] - item[1]) for item in itertools.product(w1_indexes, w2_indexes)]
                    return ({'min': min(distances), 'avg': sum(distances)/float(len(distances))})



    def get_stats(search_tag,abstract):
            match_key = [search_tag] + re.split('[, \-!?:]+', search_tag)
            match_value = [abstract.count(search_tag)]+[abstract.count(item) for item in re.split('[, \-!?:]+', search_tag)]
            match_dict = dict(zip(match_key,match_value))
            words = re.split('[, .\-!?:]+', abstract)
            w1_w2 = re.split('[, \-!?:]+', search_tag)
            proximity_value = []
            proximity_key = list(itertools.combinations(w1_w2, 2))
            for item in proximity_key:
               result = get_distance(item[0],item[1], words)
               proximity_value.append(result)
            proximity_dict = dict(zip(proximity_key,proximity_value))
            return ((match_dict,proximity_dict))

    ''' Get abstract '''


    def get_abstracts(journal, page_urls):
        if max_results > 0:
            print('\nFetching abstracts from ' + j_title_dict[journal] + '\n')
            journal_links = []
            for url in page_urls:
                html = requests.get(url).text
                soup = BeautifulSoup(html, features="html.parser")
                # marketing journals 
                if journal == 'jm' or journal == 'jmr' or journal == 'asq':
                    for element in soup.find_all('a', {'class': 'ref nowrap'}):
                        full_link = 'https://journals.sagepub.com' + element.get('href')
                        journal_links.append(full_link)
                elif journal == 'mgmtsc' or journal == 'mktsc':
                    for element in soup.find_all('h5', {'class': 'hlFld-Title meta__title meta__title__margin'}):
                        full_link = 'https://pubsonline.informs.org' + element.a.get('href')
                        journal_links.append(full_link)
                elif journal == 'jams':
                    for element in soup.find_all('a', {'class': 'title'}):
                        full_link = 'https://link.springer.com' + element.get('href')
                        journal_links.append(full_link)
                # management journals
                elif journal == 'aomj' or journal == 'aomr':
                    for element in soup.find_all('h4', {'class': 'meta__title meta__title__margin'}):
                        full_link = 'https://journals.aom.org' + element.a.get('href')
                        journal_links.append(full_link)
                elif journal == 'asq':
                    for element in soup.find_all('a', {'class': 'ref nowrap'}):
                        full_link = 'https://journals.sagepub.com' + element.get('href')
                        journal_links.append(full_link)
            
            journal_links_required = journal_links[(lo-1):(hi)]
            count = (lo-1)
            for link in journal_links_required:
                count += 1
                html = requests.get(link).text
                soup = BeautifulSoup(html, features="html.parser")
                # marketing journals
                if journal == 'jm' or journal == 'jmr' or journal == 'asq':
                    if soup.find('div', {'class': 'abstractSection abstractInFull'}) is not None:
                        abs_result = soup.find('div', {'class': 'abstractSection abstractInFull'}).text
                        title = soup.find('div', {'class': 'publicationContentTitle'}).text
                elif journal == 'mgmtsc' or journal == 'mktsc' or journal == 'aom':
                    if soup.find('div', {'class': 'abstractSection abstractInFull'}) is not None:
                        abs_result = soup.find('div', {'class': 'abstractSection abstractInFull'}).text
                        title = soup.find('h1', {'class': 'citation__title'}).text
                elif journal == 'jams':
                    if soup.find('section', {'class': 'Abstract'}) is not None:
                        abs_result = soup.find('section', {'class': 'Abstract'}).text
                        title = soup.find('h1', {'class': 'ArticleTitle'}).text
                # management journals
                elif journal == 'aomj' or journal == 'aomr':
                    if soup.find('div', {'class': 'abstractSection abstractInFull'}) is not None:
                        abs_result = soup.find('div', {'class': 'abstractSection abstractInFull'}).text
                        title = soup.find('h1', {'class': 'citation__title'}).text
                elif journal == 'asq':
                    if soup.find('div', {'class': 'abstractSection abstractInFull'}) is not None:
                        abs_result = soup.find('div', {'class': 'abstractSection abstractInFull'}).text
                        title = soup.find('div', {'class': 'publicationContentTitle'}).text
                        
                if journal_links_required.index(link) == 0:
                    print('\nArticle number: ' + str(count))
                    print('\n'+title)
                    print('\nAbstract:')
                    print (abs_result)
                    print('\nStats:')
                    print('\nMatch results: ',get_stats(search_tag,abstract = abs_result)[0])
                    print('\nProximity results: ',get_stats(search_tag,abstract = abs_result)[1])
                    print('\nFind article here: ' + link)
                    print('===================================================================================================================\n')
                else:
                    next_answer = input('Print next entry?(y/n): ')
                    if next_answer == 'y':
                        print('\nArticle number: ' + str(count))
                        print('\n' + title)
                        print('\nAbstract:')
                        print (abs_result)
                        print('\nStats:')
                        print('\nMatch results: ', get_stats(search_tag, abstract=abs_result)[0])
                        print('\nProximity results: ', get_stats(search_tag, abstract=abs_result)[1])
                        print('\nFind article here: ' + link)
                        print('===================================================================================================================\n')
                    else:
                        break
                all_matches.append(get_stats(search_tag, abstract=abs_result)[0])
        else:
            print('\nThere was 0 searches in ' + j_title_dict[journal])




    journals_to_print = input('\nEnter the list of journal you want to search separated by comma (jm,jmr,mktsc,mgmtsc,jams,asq,aomj,aomr): ')

    journals_to_print_list = [x.strip() for x in journals_to_print.split(',')]

    for journal in journals_to_print_list:
        all_matches = []    
        if journal in allowed_journal_tags:
            print('\nLooking up ' + j_title_dict[journal] + '\n')
            max_results = get_max_results(journal)
            if max_results > 0:
                range_needed = input('\nEnter range of results needed separated by - (dash): ')
                lo = int(range_needed.split('-')[0])
                hi = int(range_needed.split('-')[1])
                number_needed = hi
                if max_results > 20 and int(number_needed) > 20:
                    page_number_needed = int(((int(number_needed) - int(number_needed) % 10) / 20) + 1)
                    if journal == 'jams':
                        page_nos = [x + 1 for x in list(range(1, page_number_needed))]
                        page_urls = [url_builder(journal, search_tag, after_year_tag, sort_by_tag)] + crawler(journal,page_nos)
                        get_abstracts(journal, page_urls)
                    else:
                        page_nos = list(range(1, page_number_needed))
                        page_urls = [url_builder(journal, search_tag, after_year_tag, sort_by_tag)] + crawler(journal,page_nos)
                        get_abstracts(journal, page_urls)
                else:
                    page_urls = [url_builder(journal, search_tag, after_year_tag, sort_by_tag)]
                    get_abstracts(journal, page_urls)
                print('\nSearch summary:')
                print('You searched for the word(s): '+search_tag)
                print('You searched the for results: '+str(lo)+'-'+str(hi))
                match_keys = list(all_matches[0].keys())
                for key in match_keys:
                    print('The total matches for '+key+' is '+str(sum(item[key] for item in all_matches)))
            else:
                print('\nDid you mean something else? Enter a more relevant search term')
        else:
            print ('\nThe following input is not valid: ' + journal + '. Please enter a valid value next time. Moving on to the next journal')
    while True:
        answer = input('\nDo you want to start again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print ('\nInvalid input.')
    if answer == 'y':
        continue
    else:
        print ('\nTerminating searcher.....')
        break


