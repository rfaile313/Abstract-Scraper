class Constants:

    journal_titles = [
    'Journal of Academy of Marketing Science',
    'Journal of Marketing',
    'Journal of Marketing Research',
    'Marketing Science',
    'Management Science',
    'Administrative Science Quarterly',
    'Academy of Management Journal',
    'Academy of Management Review']

    journal_keys = [
        '-JAMS-',
        '-JM-',
        '-JMR-',
        '-MKTSC-',
        '-MGMTSC-',
        '-ASQ-',
        '-AOMJ-',
        '-AOMR-']

    journal_title = {
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

    base_urls = {
            # marketing journals
            'jm': 'https://journals.sagepub.com/action/doSearch?&publication=jmxa',
            'jmr': 'https://journals.sagepub.com/action/doSearch?&publication=mrja',
            'mktsc': 'https://pubsonline.informs.org/action/doSearch?&publication[]=mksc',
            'mgmtsc': 'https://pubsonline.informs.org/action/doSearch?&publication[]=mnsc',
            'jams': 'https://link.springer.com/search?search-within=Journal&facet-journal-id=11747',
            # management journals
            'aomj': 'https://journals.aom.org/action/doSearch?&publication[]=amj',
            'aomr': 'https://journals.aom.org/action/doSearch?&publication[]=amr',
            'asq': 'https://journals.sagepub.com/action/doSearch?&publication=asqa'}