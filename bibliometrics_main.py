import pybliometrics
from pybliometrics.scopus import ScopusSearch as Scopus

#For progress bars in the console
import progress

import collections

import pandas as pd

# Initial Query
# =============

query_test_1 = 'ABS(hematite) AND AUTH(weinold)'

query_main = 'TITLE-ABS-KEY("GaN" OR "gallium nitride")'
query_ltd = 'TITLE-ABS-KEY("GaN" OR "gallium nitride") AND PUBYEAR BEF 1950'

# Modified Query
# ==============

# Tests API access by searching for my first publication
print('Found', Scopus(query_test_1).get_results_size(), 'paper(s) for search query: >>', query_test_1, '<<')

# API Query
# ==========================================================
# ==========================================================

# Gets results from Scopus and writes to a namedtuple
dout = Scopus(query_main, refresh=False, subscriber=True, view=None, download=False)
dout_size = dout.get_results_size()

dout_dld = Scopus(query_ltd, refresh=False, subscriber=True, view=None, download=True, verbose=True)

print('Found', dout_size, 'paper(s) for search query: >>', query_main, '<<')

# dout_tuple = dout.results

#dout_dataframe = pd.DataFrame

#results

# Uses set instead of list for lower complexity
fields_all = {'eid', 'doi', 'pii', 'pubmed_id', 'title', 'subtype',\
                  'creator', 'afid', 'affilname', 'affiliation_city',\
                  'affiliation_country', 'author_count', 'author_names',\
                  'author_ids', 'author_afids', 'coverDate', 'coverDisplayDate',\
                  'publicationName', 'issn', 'source_id', 'eIssn', 'aggregationType',\
                  'volume', 'issueIdentifier', 'article_number', 'pageRange',\
                  'description', 'authkeywords', 'citedby_count', 'openaccess',\
                  'fund_acr', 'fund_no', 'fund_sponsor'}

fields_included = {'affiliation_country', 'coverDate'}

fields_excluded = fields_all - fields_included