import sys
import json

from pprint import pprint

enc = lambda x: x.encode('latin1', errors='ignore')

def hw(tweet_file):
   
    termFrequency = {} # initialize an empty dictionary
 
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data:
                sentimentText = enc(data['text']);
                for term in sentimentText.split():
                    if term in termFrequency.keys():
                        termFrequency[term] = termFrequency[term]+1
                    else:
                        termFrequency[term]=1
                        
    for term in termFrequency:
        print term + ' ' + str(termFrequency[term])
            
    
   


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
