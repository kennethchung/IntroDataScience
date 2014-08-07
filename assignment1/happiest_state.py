import sys
import json
from collections import OrderedDict
from pprint import pprint

enc = lambda x: x.encode('latin1', errors='ignore')

def hw(tweet_file, scores):
   
    termFrequency = {} # initialize an empty dictionary
    stateSentDic = {} # initialize an empty dictionary
    count=1;
    for line in tweet_file:
        data = json.loads(line)
        stateName = retrieveState(data)
        if len(stateName) >0:
            if 'text' in data:
            #print enc(data['text'])
                sentScores = sentimentEachLine(enc(data['text']), scores)
                if stateName in stateSentDic.keys():
                    stateSentDic[stateName] = sentScores + stateSentDic[stateName]
                else:
                     stateSentDic[stateName] = sentScores
        
    
    orderedstateSentDic = OrderedDict(sorted(stateSentDic.items(), key=lambda x: x[1], reverse=True))   

    
    for key in orderedstateSentDic.keys():
        print key 
        break
    for line in tweet_file:
        data = json.loads(line)
        if 'place' in data and  str(data['place']) <> 'None':
            place = data['place']
            country_code = place['country_code']
            if country_code == 'US':
                fullname = place['full_name']
                #print fullname[-2:]
        #if 'coordinates' in data:
        #    print data['coordinates']
   
def retrieveState(data):
    stateName =''
    if 'place' in data and  str(data['place']) <> 'None':
        place = data['place']
        country_code = place['country_code']
        if country_code == 'US':
            fullname = place['full_name']
            stateName = fullname[-2:]
    return stateName  

def sentimentEachLine(text, scores):
    sentimentScores = 0;
    for key in scores.keys():
        if key in text:
     
            sentimentScores = sentimentScores+ scores[key]
    return sentimentScores

def lines(fp):
    print str(len(fp.readlines()))


def scoresDictionay(afinnfile):
    scoresDic = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scoresDic[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scoresDic

def main():
    #dict = {}
    #dict['a'] = (10,1)
    #print dict['a'][0]
    #dict['a'] = (10+10,20+1)
    #print dict['a'][0]
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = scoresDictionay(sent_file)
    hw(tweet_file,scores)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
