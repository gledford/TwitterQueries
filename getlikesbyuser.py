import tweepy
from tweepy import OAuthHandler
import time
import json
from accesstokens import AccessTokens
 
token_accessor = AccessTokens()
auth = OAuthHandler(token_accessor.get_consumer_key(), token_accessor.get_consumer_secret())
auth.set_access_token(token_accessor.get_access_token(), token_accessor.get_access_secret())
 
api = tweepy.API(auth)

#TODO would be nice to have this loaded from the command line
test_user = "" #TODO enter the user name here
like_number = 1

#print out each favorite tweet a user has made
for page in tweepy.Cursor(api.favorites, id=test_user, wait_on_rate_limit=True, count=200).pages(300):
	for status in page:
		print "Like Number : " + str(like_number)
		print "Tweet ID: " +  str(status.id)
		print "Originator Name: " + status.author.screen_name.encode('utf-8') 
		print "Tweet Text: \"" + status.text.encode('utf-8') + "\"" 
		print "Date of Tweet: " + status.created_at.strftime("%Y-%m-%d %H:%M:%S")
		print "Was Retweeted by " + test_user + " : " + str(status.retweeted)
		print "Originator's Source : " + status.source.encode('utf-8')
		print "URL : https://twitter.com/statuses/" + str(status.id)
		print ""
		like_number = like_number + 1

