import tweepy #python jewel for twitter API
from time import sleep #used to set tweet interval
import serial

consumer_key = 'ZQnIqEMo98yRSfHAaPposO'
consumer_secret ='QtOPd0rv5AoXkTMfLq1ZgrkIZ2UVviJ'
access_token = '8032-VPuIk19SMb8zfNTozvw0zkOv0GEHi'
access_token_secret = '3y7bL8CMPq2ARsKpKge1TT1gY1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#open text file, read lines, close
#my_file = open('testtweets.txt', 'r')
#file_lines = my_file.readlines()
#my_file.close()

while True:
    ser = serial.Serial('/dev/ttyACM0',9600)
    s = [0]
    read_serial=ser.readline()
    s[0] = str(str (ser.readline()))
    print s[0]
    # print read_serial
    
def textTweet():
    #for s[0] in read_serial:
        try:
            #prints to terminal for debugging
            print(s[0])

            #makes sure line is not blank
            if s[0] != '\n':
                print(s[0])
                api.update_status(s[0])
                sleep(10) #10 sec timer
            else:
                pass
            
        #handles exceptions
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(2)
        
textTweet()            




     




