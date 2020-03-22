import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg

def search_sort(search_string, journal, aytag, srt_by):

    #Search String
    search_tag = search_string

    journal = journal

    print(journal) #debugging

    #Year Tag
    after_year_tag = aytag

    if srt_by:
        #MR
        sort_by_tag = 'relevancy'
        sort_by_tag_jams = 'relevance'
    else:
        #date
        sort_by_tag = 'Ppub'
        sort_by_tag_jams = 'newestFirst'

    
    journal_title = {# marketing journals
                    'jams': 'Journal of Academy of Marketing Science',
                    'jm': 'Journal of Marketing',
                    'jmr': 'Journal of Marketing Research',
                    'mktsc': 'Marketing Science',
                    'mgmtsc': 'Management Science',
                    # management journals
                    'asq':'Administrative Science Quarterly',
                    'aomj':'Academy of Management Journal',
                    'aomr':'Academy of Management Review'}

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

    base_urls = {# marketing journals
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
        return (requests.get(base_urls[journal], params=payload[journal]).url)

    #Get result count for website

    def get_max_results(journal):
        url = url_builder(journal, search_tag, after_year_tag, sort_by_tag)
        html = requests.get(url).text
        soup = BeautifulSoup(html, features="html.parser")

        # marketing journals
        if journal == 'mktsc' or journal == 'mgmtsc':
            if soup.find('span', {'class': 'result__count'}) is not None:
                total_hits = soup.find('span', {'class': 'result__count'}).text
                return 'Total number of hits returned for {} in {} is {}'.format(search_tag, journal_title[journal], total_hits)
            else:
                total_hits = '0'
                return 'There were 0 total results'
        
        elif journal == 'jm' or journal == 'jmr':
            if soup.find('div', {'class': 'paginationStatus'}) is not None:
                total_hits = soup.find('div', {'class': 'paginationStatus'}).text
                return 'Total number of hits returned for {} in {} is {}'.format(search_tag, journal_title[journal], total_hits[-1])
            else:
                total_hits = '0'
                return 'There were 0 total results'
            
        elif journal == 'jams':
            if soup.find('div', {'class': 'header'}) is not None:
                total_hits = soup.find('div', {'class': 'header'}).text
                #idk why this journal string slice is so weird -- we need to fix all of these PALLAV
                return 'Total number of hits returned for {} in {} is {}'.format(search_tag, journal_title[journal], total_hits[2:9])
            else:
                total_hits = '0'
                return 'There were 0 total results' 

        # management journals
        elif journal == 'aomj' or journal == 'aomr':
            if soup.find('span', {'class': 'result__count'}) is not None:
                total_hits = soup.find('span', {'class': 'result__count'}).text
                return 'Total number of hits returned for {} in {} is {}'.format(search_tag, journal_title[journal], total_hits)
            else:
                total_hits = '0'
                return 'There were 0 total results'

        elif journal == 'asq':
            if soup.find('div', {'class': 'paginationStatus'}) is not None:
                total_hits = soup.find('div', {'class': 'paginationStatus'}).text.split()
                return 'Total number of hits returned for {} in {} is {}'.format(search_tag, journal_title[journal], total_hits[-1])
            else:
                total_hits = '0'
                return 'There were 0 total results'

    result_string = get_max_results(journal)
    return result_string

      

