import requests
from bs4 import BeautifulSoup
from constants import Constants

class ScanForResults:

    def search_sort(self, search_string, journal, aytag, srt_by):

        #Search String
        self.search_tag = search_string

        self.journal = journal

        #debugging / turn off in prod
        #########################
        print(journal)
        #########################

        #Year Tag
        self.after_year_tag = aytag

        if srt_by:
            #MR
            self.sort_by_tag = 'relevancy'
            self.sort_by_tag_jams = 'relevance'
        else:
            #date
            self.sort_by_tag = 'Ppub'
            self.sort_by_tag_jams = 'newestFirst'

        self.payload = {
        # marketing journals
        'jm': {'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag},
        'jmr': {'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag},
        'mktsc': {'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag},
        'mgmtsc': {'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag},
        'jams': {'query': self.search_tag, 'date-facet-mode': 'between', 'facet-start-year': self.after_year_tag,'previous-start-year': '1975', 'facet-end-year': '2019', 'previous-end-year': '2019','sortOrder': self.sort_by_tag_jams},
        # management journals
        'aomj': {'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag},
        'aomr':{'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag},
        'asq': {'text1': self.search_tag, 'AfterYear': self.after_year_tag, 'sortBy': self.sort_by_tag}}


    def url_builder(self, journal):
        return (requests.get(Constants.base_urls[journal], params=self.payload[journal]).url)

    #Get result count for website
    def get_max_results(self, journal):
        url = self.url_builder(self.journal)
        html = requests.get(url).text
        soup = BeautifulSoup(html, features="html.parser")

        # marketing journals
        if journal == 'mktsc' or journal == 'mgmtsc':
            if soup.find('span', {'class': 'result__count'}) is not None:
                total_hits = soup.find('span', {'class': 'result__count'}).text
                return 'Hits for: "{}" in {} is {}'.format(self.search_tag, Constants.journal_title[journal], total_hits)
            else:
                total_hits = '0'
                return 'There were 0 total results'
        
        elif journal == 'jm' or journal == 'jmr':
            if soup.find('div', {'class': 'paginationStatus'}) is not None:
                total_hits = soup.find('div', {'class': 'paginationStatus'}).text
                return 'Hits for: "{}" in {} is {}'.format(self.search_tag, Constants.journal_title[journal], total_hits[-1])
            else:
                total_hits = '0'
                return 'There were 0 total results'
            
        elif journal == 'jams':
            if soup.find('div', {'class': 'header'}) is not None:
                total_hits = soup.find('div', {'class': 'header'}).text
                #TODO idk why this journal string slice is so weird -- we need to fix all of these ~@rfaile313
                return 'Hits for: "{}" in {} is {}'.format(self.search_tag, Constants.journal_title[journal], total_hits[2:9])
            else:
                total_hits = '0'
                return 'There were 0 total results' 

        # management journals
        elif journal == 'aomj' or journal == 'aomr':
            if soup.find('span', {'class': 'result__count'}) is not None:
                total_hits = soup.find('span', {'class': 'result__count'}).text
                return 'Hits for: "{}" in {} is {}'.format(self.search_tag, Constants.journal_title[journal], total_hits)
            else:
                total_hits = '0'
                return 'There were 0 total results'

        elif journal == 'asq':
            if soup.find('div', {'class': 'paginationStatus'}) is not None:
                total_hits = soup.find('div', {'class': 'paginationStatus'}).text.split()
                return 'Hits for: "{}" in {} is {}'.format(self.search_tag, Constants.journal_title[journal], total_hits[-1])
            else:
                total_hits = '0'
                return 'There were 0 total results'


    #TODO Build below functions for abstract text request logic

    def crawler(self):
        pass

    def get_abstracts(self):
        pass

    def get_distance(self):
        pass

    def get_stats(self):
        pass