import tweepy
from tweepy import OAuthHandler
import time
import json
import re
import sys
from accesstokens import AccessTokens

token_accessor = AccessTokens()
auth = OAuthHandler(token_accessor.get_consumer_key(), token_accessor.get_consumer_secret())
auth.set_access_token(token_accessor.get_access_token(), token_accessor.get_access_secret())
 
api = tweepy.API(auth)

#Read URLs from file to get Tweet IDs
url_list = open("favorites_url.txt", "r")
tweet_id_list_of_list = list()
tweet_ids = list()
private_tweets = list()
like_number = 1

#Fetch all the tweet IDs and put them into chucks of 100 IDs
#which is required by the Twitter API
for line in url_list:
    if re.match("https:\/\/twitter\.com*", line):
    	tweet_id = line.split("/")
        tweet_ids.append(tweet_id[-1].split("\n")[-2])
        if len(tweet_ids) is 100:
        	tweet_id_list_of_list.append(list(tweet_ids))
        	tweet_ids[:] = []

# print(len(tweet_id_list_of_list))

# for slot in tweet_id_list_of_list:
# 	try:
# 		page = api.statuses_lookup(slot)
# 		for status in page:
# 			print "Like Number : " + str(like_number)
# 			print "Tweet ID: " +  str(status.id)
# 			print "Originator Name: " + status.author.screen_name.encode('utf-8') 
# 			print "Tweet Text: \"" + status.text.encode('utf-8') + "\"" 
# 			print "Date of Tweet: " + status.created_at.strftime("%Y-%m-%d %H:%M:%S")
# 			print "Originator's Source : " + status.source.encode('utf-8')
# 			print "URL : https://twitter.com/statuses/" + str(status.id)
# 			print ""
# 			like_number = like_number + 1
# 	except tweepy.error.TweepError:
# 		time.sleep(15 * 60)
# 	except KeyboardInterrupt:
#     	sys.exit()
# 	except:
# 		#keep a list of tweets the script cannot parse
# 		print("Exception: ", sys.exc_info()[0])

