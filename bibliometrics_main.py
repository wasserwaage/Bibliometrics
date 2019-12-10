# PACKAGES
# =====================================================================

# Bibliometrics
# =====================================================================
import pybliometrics # For Scopus
from pybliometrics.scopus import ScopusSearch as Scopus

import wos # For Web of Science

import dimcli # For Dimensions

# File Handling
# =====================================================================

# Data Science
# =====================================================================
import pandas as pd
import progress #For progress bars in the console
import collections # Required for namedtuples data type returned by the ScopusSearch function

# =====================================================================
# =====================================================================
# Bibliometrics API Script
# Michael Weinold 2019-2020
# University of Cambridge
# =====================================================================
# =====================================================================

# =====================================================================
# Scopus
# =====================================================================

# Test Query
# Tests API access by searching for my first publication
# =====================================================================

query_test_1 = 'ABS(hematite) AND AUTH(weinold)'
print('Found', Scopus(query_test_1).get_results_size(), 'paper(s) for search query: >>', query_test_1, '<<')

# Modified Query
# ==============

query_main = 'TITLE-ABS-KEY("GaN" OR "gallium nitride")'
query_ltd = 'TITLE-ABS-KEY("GaN" OR "gallium nitride") AND PUBYEAR BEF 1950'

# API Query
# ==========================================================

# Gets number of results from Scopus
dout_tmp = Scopus(query_main,
                  refresh=False,
                  subscriber=True,
                  view=None,
                  download=False)
dout_size = dout_tmp.get_results_size()
print('Found', dout_size, 'paper(s) for search query: >>', query_main, '<<')


# Gets results from Scopus as list of namedtuples
print('Downloading data for query >>', query_main, '<<')
dout_dld = Scopus(query_main,
                  refresh=False,
                  subscriber=True,
                  view=None,
                  download=True,
                  verbose=True)

# Selects specific database fields to pass to pandas dataframe
fields_all = ('eid', 'doi', 'pii', 'pubmed_id', 'title', 'subtype',\
                  'creator', 'afid', 'affilname', 'affiliation_city',\
                  'affiliation_country', 'author_count', 'author_names',\
                  'author_ids', 'author_afids', 'coverDate', 'coverDisplayDate',\
                  'publicationName', 'issn', 'source_id', 'eIssn', 'aggregationType',\
                  'volume', 'issueIdentifier', 'article_number', 'pageRange',\
                  'description', 'authkeywords', 'citedby_count', 'openaccess',\
                  'fund_acr', 'fund_no', 'fund_sponsor')
def fields_included(field):
    included = ('affiliation_country', 'coverDate')
    if (field in included):
        return False
    else:
        return True
fields_filtered = filter(fields_included, fields_all)
fields_excluded = tuple(i for i in fields_filtered) # Note that there is no tuple comprehension in Python

# Writes list of namedtuples to dataframe
dout_dataframe = pd.DataFrame.from_records(dout_dld.results,
                                           columns=fields_all,
                                           exclude=fields_excluded)

# Writes data to feather file for best performance
dout_dataframe.to_feather(os.getcwd()+'/data/scopus/'+query_main)