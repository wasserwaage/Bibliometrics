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
import collections # Required for namedtuples data type returned by the ScopusSearch function

# Service
# =====================================================================
import time
import os

# Database names
# ==============

tech = 'GaN' # Set technology name
scopus_dir = os.getcwd()+'/data/scopus/'
tech_dir = scopus_dir+tech

if not os.path.exists(scopus_dir+tech): # Creates subfolder for database files
    os.makedirs(scopus_dir+tech)

feather_GaN = os.getcwd()+'/data/scopus/TITLE-ABS-KEY("GaN" OR "gallium nitride")'

# Loads dataframe from feather file
GaN_raw = pd.read_feather(feather_GaN)

# Removes irrelevant metadata columns
fields_all = ('eid', 'doi', 'pii', 'pubmed_id', 'title', 'subtype',\
                  'creator', 'afid', 'affilname', 'affiliation_city',\
                  'affiliation_country', 'author_count', 'author_names',\
                  'author_ids', 'author_afids', 'coverDate', 'coverDisplayDate',\
                  'publicationName', 'issn', 'source_id', 'eIssn', 'aggregationType',\
                  'volume', 'issueIdentifier', 'article_number', 'pageRange',\
                  'description', 'authkeywords', 'citedby_count', 'openaccess',\
                  'fund_acr', 'fund_no', 'fund_sponsor')
def fields_included(field):
    included = ('doi', 'title', 'author_names', 'publicationName', 'coverDate', 'citedby_count')
    if (field in included):
        return False
    else:
        return True
fields_filtered = filter(fields_included, fields_all)
fields_excluded = tuple(i for i in fields_filtered) # Note that there is no tuple comprehension in Python

GaN = pd.DataFrame.drop(GaN_raw, axis='columns', columns=list(fields_excluded))

# =====================
# Database Manipulation
# =====================

# Searches for year range in coverDate column
year_max = int(GaN['coverDate'].max()[0:4]) # Gets only year from string
year_min = int(GaN['coverDate'].min()[0:4]) # Gets only year from string

# Writes all column entries from a single year to a new dataframe
for year in range(year_max - year_min):

    year = year + year_min # Sets correct start year
    dbname = tech + '_year=' + str(year) # Sets database name

    GaN_tmp = GaN.loc[(GaN['coverDate'] <= str(year)+'-12-31') & (GaN['coverDate'] >= str(year)+'-01-01')]
    GaN_tmp = GaN_tmp.sort_values(by=['coverDate'], inplace=True) # Sorts by citations
    GaN_tmp.reset_index(drop=True, inplace=True) # Resets index for writing to feather files
    GaN_tmp.to_feather(os.getcwd() + '/data/scopus/' + dbname) # Writes to feather file

#Reads all single-year databases for inspection
def read_all_feathers(absdirpath):

    global db_dict = {} # Dictionary of single-year database dataframes

    flist = os.listdir(absdirpath)
    for file in flist:
        tmp_feather = pd.read_feather(absdirpath+file)
        db_dict['file'] = tmp_feather

    print('Feather files opened from path >>', absdirpath, '<<'), print()

read_all_feathers(tech_dir)

