import tweepy #python jewel for twitter API
from time import sleep #used to set tweet interval
import serial

consumer_key = 'ZQnIqEMoaPposO'
consumer_secret ='QtOPS0TMfLq1ZgrkIZ2UVviJ'
access_token = '8223288Ov0GEHi'
access_token_secret = 'dCqe1gY1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):
        
    def on_status(self, status):
        #while True:  
        ser = serial.Serial('/dev/ttyACM0',9600)
        s = [0]
        read_serial=ser.readline()
        s[0] = str(str (ser.readline()))
        #print s[0]
        #print read_serial
        print status.text
        print status.user.screen_name
        api.update_status("@" + status.user.screen_name + " " + s[0], in_reply_to_status_id = status.id)

    def on_error(self, status_code):
        print >> sys.stderr, 'Error with status code: ', status_code
        return True
    def on_timeout(self):
        print >> sys.stderr, 'Timeout..'
        return true

sapi = tweepy.streaming.Stream(auth, StreamListener())
sapi.filter(track=['@lattebot00'])

     
