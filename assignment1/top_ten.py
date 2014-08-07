import sys
import json
from collections import OrderedDict
from pprint import pprint

enc = lambda x: x.encode('latin1', errors='ignore')

def hw(tweet_file):
   
    hashTagDic = {} # initialize an empty dictionary
 
    for line in tweet_file:
        data = json.loads(line)
        if 'entities' in data:
            entities = data['entities']
            hashTags = entities['hashtags']
            if len(hashTags) > 0:
                for eachHash in hashTags:
                    hashText = enc(eachHash['text'])
                    cleanHashText = hashText.replace('_','')
                    if len(cleanHashText) > 0:
                        if cleanHashText in hashTagDic.keys():
                            hashTagDic[cleanHashText] = hashTagDic[cleanHashText]+1
                        else:
                            hashTagDic[cleanHashText] =1
                            
    
    
    orderedhashTagDic = OrderedDict(sorted(hashTagDic.items(), key=lambda x: x[1], reverse=True))    
    count = 1        
    for key in orderedhashTagDic.keys():
        print key +' ' + str(orderedhashTagDic[key])
        if count >=10:
            break
        else:
           count = count +1 

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
    
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
