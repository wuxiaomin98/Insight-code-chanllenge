# Insight Data Engineering code challenge
# Python code to calculate the number of tweets cleaned, 
# by removing the non-ASCII unicode and escape characters

# import packages for further usage
import sys
import json
import re

# Set the default encoding to be utf8, to avoid the error caused by system encoding
reload(sys)
sys.setdefaultencoding('utf8')

# Check the input format
if len(sys.argv) != 3:
    print('Incorrect input format, try to use the format in README!')
    sys.exit(1)

# Take input file as parameter 1 and read it
input_file = sys.argv[1]
tweetInput = open(input_file, 'r')

# Take output file as parameter 2 and write it
output_file = sys.argv[2]
ft1 = open(output_file, 'w')

# Number of tweets containing unicode
numTweetsWithUnicode = 0

# To save cleaned twitter after cleaning
cleaned_tweets = []

# Clean the twitter file process
# Read the input file line by line
for line in tweetInput:
	tweets = json.loads(line)
	# Check the existence of 'created_at' and 'text'
	if (len(re.findall('created_at', line)) != 0) and (len(re.findall('text', line)) != 0):
	    timestamp = tweets["created_at"]
	    content = tweets["text"]

	    for escape in ['\a', '\b', '\f', '\r', '\n', '\t', '\v', '\/', '\\', '\'', '\"']:
	        content = content.replace(escape, '')

            realContent = content.encode().decode('ascii', 'ignore')
            if realContent != content:
        	numTweetsWithUnicode += 1

            cleaned_tweets.append(realContent + '(timestamp: ' + timestamp + ')')

# Write the cleaned tweets into file
for line in cleaned_tweets:
	ft1.write(line + '\n')
ft1.write('\n' + str(numTweetsWithUnicode) + ' tweets contained unicode')	
