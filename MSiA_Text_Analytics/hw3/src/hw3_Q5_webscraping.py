# -*- coding: utf-8 -*-
"""
@author: Xiang Li

# This Webscraping is collaborated with Steven Lin and copied mostly from the Reference
# References:
http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html

"""

from bs4 import BeautifulSoup
import re
from urllib2 import urlopen 
from __future__ import division 
import os
import json


path = '/Users/apple/Documents/MSiA/Fall 2015/Text analytics/HW/hw3'
os.chdir(path)

out_file_name = 'webscraped.json'


def processLinkByParagraph(url):
    
    html = urlopen("http://en.wikipedia.org"+url)
    bsObj = BeautifulSoup(html)
    paragraphs = bsObj.findAll('p')
    paragraphs = [p.get_text() for p in paragraphs]
    return " ".join(paragraphs)
    
          
#%% Webscraping
           
wiki_url = 'https://en.wikipedia.org/wiki/List_of_national_capitals_in_alphabetical_order'
html = urlopen(wiki_url)
bsObj = BeautifulSoup(html)
table = bsObj.find("table", { "class" : "wikitable sortable" })
n=int(len(table)/2)
pattern = re.compile(r'(legislative|declared|official|constitutional)')

results = {} #initialize a json format

i=0
for row in table.findAll("tr"):
    
    col = row.findAll("td")
    
    if len(col)>1:
        city = col[0].findAll("a")        # get hyperlinks
        descr = col[0].findAll("small") # get description
        country= col[1].find("a")         # get hyperlink
        
        # multiple capital cities, choose 1 which matches the given pattern
        if len(city)>1:
            index = [i for i, description in enumerate(descr)if pattern.search(description.get_text())][0]
            city = city[index]
        else:
            city = city[0]
            
        # attributes of tag object
        results[(city['title'],country['title'])] = {"city": processLinkByParagraph(city['href']), 
                                                     "country": processLinkByParagraph(country['href'])}       
    i+=1

                                                    
#%% Save results #############################################################

# convert tuple key to one string key : capitalName_countryName
output = {k[0] + "_" + k[1] : v for (k,v) in results.items()}        

#output webscraping data to jason file                                            
with open(out_file_name, 'w') as fp:
    json.dump(output, fp)
                    