import tweepy #python jewel for twitter API
from keys import * #imports twitter keys and tokens
from time import sleep #used to set tweet interval

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
    

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text
        print status.user.screen_name
        api.update_status("@" + status.user.screen_name + " Go to Maui Coffee Attic.", in_reply_to_status_id = status.id)

    def on_error(self, status_code):
        print >> sys.stderr, 'Error with status code: ', status_code
        return True
    def on_timeout(self):
        print >> sys.stderr, 'Timeout..'
        return true

sapi = tweepy.streaming.Stream(auth, StreamListener())
sapi.filter(track=['@lattebot00'])

     
