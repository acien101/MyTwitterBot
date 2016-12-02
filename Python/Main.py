import TwitterClass
import TWITTERDATA
import time

'''The api sends a tweet every 12 hours with a picture taken from a folder with random pics'''
twitterObj = TwitterClass.TwitterClass(TWITTERDATA.CONSUMER_KEY, TWITTERDATA.CONSUMER_SECRET, TWITTERDATA.ACCESS_TOKEN, TWITTERDATA.ACCESS_TOKEN_SECRET)        #Ther twitter object of th etwitter class

while True:
    twitterObj.writeTweetWithMedia("etica.png", "Prueba con imagen")
    time.sleep(43200)