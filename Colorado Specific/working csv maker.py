import os
import lxml
from lxml import html
from lxml import etree
import pandas as pd
import numpy as np
import json
import requests as rq
import io
from io import StringIO, BytesIO
import urllib2 as url
from urllib2 import urlopen
import re

'''Welcome to this humble python script that can be used to search for terms in the API. 
Let me know if you are not as familiar with python and need any help using it.'''

save_dir=os.getcwd()

indis=rq.get('http://codataengine.org/api/dataset.json?key=49a19ed77c416266d2370caeb7f280d9.33105')
jindis=indis.json()
'''jindis is just JSON inicators - that is, it is a list of dictionaries from which we can extract the ID for each data set in the database'''

def metadata_csv():
    '''returns a list of indicaators as a csv'''
    final_df=pd.DataFrame.from_records(jindis)
    final_df.to_csv('indicator_list'+'.csv')
#during the hackathon, I hope to extend this to produce csvs from actual data sets and not just the indicator list


def getAPIcallForTerm(term, start=0, limit=100):
    '''returns an API call based on the term suppied'''
    sterm=str(term)
    regsterm=re.compile('.*'+sterm+'.*', re.IGNORECASE)
    for i, item in enumerate(jindis):
        indic_title = str(jindis[i]['title'])
        if regsterm.match(indic_title):
            eyed=str(jindis[i]['id'])
            call='http://codataengine.org/api/dataset/'+indic_id+'.json?start='+start+'&limit='+limit+'&key=49a19ed77c416266d2370caeb7f280d9.33105'
            
            return call


def mk_indic_req(indic_id):
    '''returns a json object based on a derived indicator id'''
    indic_id=str(indic_id)
    call='http://codataengine.org/api/dataset/'+indic_id+'.json?start=0&limit=100&key=49a19ed77c416266d2370caeb7f280d9.33105'
    print call
    jay=rq.get(call)
    pjay=jay.json()

    return pjay


def getterm(term):
    '''returns a json object based on the term suppied'''
    sterm=str(term)
    regsterm=re.compile('.*'+sterm+'.*', re.IGNORECASE)
    for i, item in enumerate(jindis):
        indic_title = str(jindis[i]['title'])
        if regsterm.match(indic_title):
            eyed=str(jindis[i]['id'])
            pjay_term=mk_indic_req(eyed)
            
            return pjay_term
