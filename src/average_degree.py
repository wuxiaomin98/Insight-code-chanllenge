# Insight Data Engineering code challenge feature 2
# Python code to calculate the average degree of a vertex in a Twitter hashtag graph,
# update it each time a new tweet shows up

# import packages for further usage
import sys
import json
import re
import os
from re import findall
from time import strptime, mktime
from itertools import combinations
from collections import defaultdict
#from datatime import datatime
import networkx as nx

# Set the default encoding to be utf8, to avoid the error caused by system encoding
reload(sys)
sys.setdefaultencoding('utf8')

# Check the time difference
def timediff(time1, time2):
    t1 = datatime.strptime(time1, '%a %b %d %H:%M:%S +0000 %Y')
    t2 = datatime.strptime(time2, '%a %b %d %H:%M:%S +0000 %Y')
    return ((t1.days - t2.days) * 24 * 60 * 60) + (t1.seconds - t2.seconds)

# Get hashtag list
def get_hashtaglist(text):
    #return list({hashtag.strip('#') for hashtag in text.split() if hashtag.startwith('#')})
    hashtags = findall(r'#\w*', text.lower())
    return list(combinations(hashtags, 2))

# Get time
def get_time(timestamp):
    # timestamp = re.search("\(timestamp\:(.*)\)", text)
    return mktime(strptime(timestamp, '%a %b %d %H:%M:%S +0000 %Y'))

# Get average degree
def get_avg_degree(G):
    deg = G.degree(G.node()).values()
    return sum(deg) / sum(degree for degree in deg)

# Update the graph with removing the outdated edges
def update(G, hashTagList):
    for tweet in hashTagList:
        G.add_edges_from(tweet['hashtags'], {'created_at': tweet['created_at']})
        for edge in G.edges:
            if (tweet['created_at'] - edge[2]['created_at']) > 60:
                G.remove_edge(*edge[:2])
    return G

# Main function
def main():
    # Check the input format
    if len(sys.argv) != 3:
        print('Incorrect input format, try to use the format in README!')
        sys.exit(1)

    # Take input file as parameter 1 and read it
    input_file = sys.argv[1]
    tweetInput = open(input_file, 'r')

    # Take output file as parameter 2 and write it
    output_file = sys.argv[2]
    ft2 = open(output_file, 'w')

    # Initialize the graph object
    G = nx.Graph()

    # Initialize and get hashtag list
    tweets = {}
    hashTagList = []
    for tweet in tweetInput:
        tweet = json.loads(tweet)
	if 'created_at' in tweet:
            # Get timestamp and hashtag list
            tweets['created_at'] = get_time(tweet['created_at'])
            tweets['hashtags'] = get_hashtaglist(tweet['text'])

            # Get the format of hashtag list with timestamp
            hashTagList.append(tweets)

    G = update(G, tweets)
    avg_degree = round(get_avg_degree(G), 2)
    ft2.write(str(avg_degree) + '\n')

if __name__ == "__main__":
    main()
