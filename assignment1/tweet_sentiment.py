import sys
import json

from pprint import pprint

enc = lambda x: x.encode('latin1', errors='ignore')

def hw(tweet_file, scores):
   
    sentiments = {} # initialize an empty dictionary
    count=1;
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data:
            #print enc(data['text'])
            sentiments[count] = sentimentEachLine(enc(data['text']), scores)
        else:
            sentiments[count] = 0;
        print sentiments[count]
        count = count+1

def sentimentEachLine(text, scores):
    sentimentScores = 0;
    for key in scores.keys():
        if key in text:
     
            sentimentScores = sentimentScores+ scores[key]
    return sentimentScores

def lines(fp):
    print str(len(fp.readlines()))


def scoresDictionay(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = scoresDictionay(sent_file)
    hw(tweet_file,scores)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
