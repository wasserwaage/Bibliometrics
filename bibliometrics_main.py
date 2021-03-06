# PACKAGES
# =====================================================================

# Bibliometrics
# =============
import pybliometrics # For Scopus
from pybliometrics.scopus import ScopusSearch as Scopus

# File Handling
# =============

# Data Science
# ============
import pandas as pd
import collections # Required for namedtuples data type returned by the ScopusSearch function

# Service
# =======
import time
import os

# =====================================================================
# =====================================================================
# Bibliometrics API Script
# Michael Weinold 2019-2020
# University of Cambridge
# =====================================================================
# =====================================================================

# Test Query
# Tests API access by searching for my first publication.
# =====================================================================

query_test_1 = 'ABS(hematite) AND AUTH(weinold)'
print('Found', Scopus(query_test_1).get_results_size(), 'paper(s) for search query: >>', query_test_1, '<<')

# Main Query
# Takes an advanced Scopus search as input from the console.
# =====================================================================

query_main = str(input('Enter Scopus Advanced Search query:'))

# API Query
# Downloads results database for search query
# =====================================================================

# Gets number of results from Scopus
dout_tmp = Scopus(query_main,
                  refresh=False,
                  subscriber=True,
                  view=None,
                  download=False)
dout_size = dout_tmp.get_results_size()
print('Found', dout_size, 'paper(s) for search query: >>', query_main, '<<')

# Gets results from Scopus as list of namedtuples
try:
    start = time.time()
    print('Downloading data for query >>', query_main, '<<')
    dout_dld = Scopus(query_main,
                      refresh=False,
                      subscriber=True,
                      view=None,
                      download=True,
                      verbose=True)
finally:
    end = time.time()
    print('Download complete, elapsed time=', end - start, 'seconds'), print()

# Selects specific database fields to pass to pandas dataframe
fields_all = ('eid', 'doi', 'pii', 'pubmed_id', 'title', 'subtype',\
                  'creator', 'afid', 'affilname', 'affiliation_city',\
                  'affiliation_country', 'author_count', 'author_names',\
                  'author_ids', 'author_afids', 'coverDate', 'coverDisplayDate',\
                  'publicationName', 'issn', 'source_id', 'eIssn', 'aggregationType',\
                  'volume', 'issueIdentifier', 'article_number', 'pageRange',\
                  'description', 'authkeywords', 'citedby_count', 'openaccess',\
                  'fund_acr', 'fund_no', 'fund_sponsor')

# File Handling
# Writes to file
# =====================================================================

# Writes list of namedtuples to dataframe
dout_dataframe = pd.DataFrame.from_records(dout_dld.results,
                                           columns=fields_all)

# Writes data to feather file
try:
    dout_dataframe.to_feather(os.getcwd() + '/data/scopus/' + query_main)
finally:
    print('Writing complete.')