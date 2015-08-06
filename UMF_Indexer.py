import pandas as pd
import os
import urllib
import urllib2
from urlparse import parse_qsl

from sets import Set


class UMF_Indexer:
    DOCUMENT_LIST_FILENAME = "docList.csv"
    def __init__(self):
        pass

    def extractDocumentUrl(self,directory):
        urlList = Set()

        for f in os.listdir(directory):
            if f.endswith('.csv'):
                data = pd.read_csv(open(directory+'/'+f),sep='\t',names=['query','document','time'])
                s = Set(data['document'].tolist())
                urlList = urlList | s

        return urlList

    def getDocumentFromURL(self,url):
        pass
