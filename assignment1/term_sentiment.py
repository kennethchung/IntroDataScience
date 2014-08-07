import sys
import json

from pprint import pprint

enc = lambda x: x.encode('latin1', errors='ignore')

def hw(tweet_file, scoresDic):
   
    sentiments = {} # initialize an empty dictionary
    termSentimentsDic = {}
    count=1;
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data:
            #print enc(data['text'])
            score = sentimentEachLine(enc(data['text']), scoresDic)
            termSentiment(score, enc(data['text']),scoresDic,termSentimentsDic )
            
    for term in termSentimentsDic.keys():
        diff = termSentimentsDic[term][0] - termSentimentsDic[term][1]
        print term  +' ' +  str(diff)
            
def termSentiment(sentimentScore, sentimentText,scoresDic,termSentimentsDic ):
    
    for term in sentimentText.split():
        if (term in scoresDic.keys()) is False:
            if (sentimentScore > 0):
                updateTermSentimentsDic(termSentimentsDic, term, 1,0)
            else:
                updateTermSentimentsDic(termSentimentsDic, term, 0,1)
            
    
   
def updateTermSentimentsDic(termSentimentsDic, term,pos, neg):
    if term in termSentimentsDic.keys():
        curPos = termSentimentsDic[term][0] 
        curNeg = termSentimentsDic[term][1]
        termSentimentsDic[term] = (curPos + pos, curNeg + neg)
        #print term + ', ' + str(curPos + pos) +', ' +str(curNeg + neg)
    else:
        termSentimentsDic[term] = (pos, neg)
        #print '2: ' +term + ', ' + str( termSentimentsDic[term][0]) +', ' +str(termSentimentsDic[term][1])

def sentimentEachLine(text, scoresDic):
    sentimentScores = 0;
    for key in scoresDic.keys():
        if key in text:
            sentimentScores = sentimentScores+ scoresDic[key]
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
    scoresDic = scoresDictionay(sent_file)
    hw(tweet_file,scoresDic)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
