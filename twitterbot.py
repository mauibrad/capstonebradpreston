import tweepy #python jewel for twitter API
from keys import * #imports twitter keys and tokens
from time import sleep #used to set tweet interval

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#open text file, read lines, close
my_file = open('testtweets.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

def textTweet():
#loop to iterate over text file
    for line in file_lines:
        try:
            #prints to terminal for debugging
            print(line)

            #makes sure line is not blank
            if line != '\n':
                api.update_status(line)
                sleep(7200) #one hour timer
            else:
                pass

        #handles exceptions
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(2)

textTweet()


    

searchTWeet = api.search(q="@lattebot00")

t = ['@LATTEbot00',
     'LATTEbot00',
     '@lattebot00',
     'lattebot00',
     'lattebot']

for reply in searchTweet:
    for i in t:
        if i == reply.text:
            screenName = s.user.screen_name
            m = "@%s Be quiet." % (screenName)
            reply = api.update_status(m, s.id)


     




