import TwitterClass
import TWITTERDATA
import time
import os
import random

'''The api sends a tweet every 12 hours with a picture taken from a folder with random pics'''
twitterObj = TwitterClass.TwitterClass(TWITTERDATA.CONSUMER_KEY, TWITTERDATA.CONSUMER_SECRET, TWITTERDATA.ACCESS_TOKEN, TWITTERDATA.ACCESS_TOKEN_SECRET)        #Ther twitter object of th etwitter class

dirlist = os.listdir("../Pics/")             #Then save the paths of the pics in a aarray

while True:
    random.seed()
    twitterObj.writeTweetWithMedia(dirlist[random.randrange(0, len(dirlist))], "")
    time.sleep(43200)