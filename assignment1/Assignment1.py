'''
Created on Dec 4, 2013

@author: 222185
'''
import urllib
import json


response = urllib.urlopen("https://search.twitter.com/search.json?q=yahoo")
print json.load(response)