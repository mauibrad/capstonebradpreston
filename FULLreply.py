import tweepy #python jewel for twitter API
from keys import * #imports twitter keys and tokens
from time import sleep #used to set tweet interval
import serial

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):
        
    def on_status(self, status):
        my_file = open('datafile.txt', 'r')
        file_lines = my_file.readlines()
        my_file.close()

        lati = float(file_lines[-3])
        longi = float(file_lines[-2])
        floatcelc = float(file_lines[-1][:-1])
        floatfahr = ((floatcelc * 9) / 5) + 32
        celc = str(floatcelc)
        fahr = str(floatfahr)
        print status.text
        print status.user.screen_name
        api.update_status("@" + status.user.screen_name + " It is " + celc + u"\u00b0" + " Celsius and " + fahr + u"\u00b0" + " Fahrenheit.", lat=lati, long=longi, in_reply_to_status_id = status.id)

    def on_error(self, status_code):
        print >> sys.stderr, 'Error with status code: ', status_code
        return True
    def on_timeout(self):
        print >> sys.stderr, 'Timeout..'
        return True

sapi = tweepy.streaming.Stream(auth, StreamListener())
sapi.filter(track=['@lattebot00'])

     
