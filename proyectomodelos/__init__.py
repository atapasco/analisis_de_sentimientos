from multiprocessing.connection import Listener
from re import A
import secrets
import tweepy
from tweepy import StreamingClient
import json






class TweetsListener(StreamingClient):
    print("conectando...")
    def on_connect(self):
        print("Conectado.")
    def on_tweet(self, tweet):
        print(tweet.text)
    def on_error(self, status_code):
        print("Error", status_code)

Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAH7BgwEAAAAA98QAK4a4%2Fk6WRGx7gsNL0FgysvE%3DrWrpsOe5C9ZatftXzJsqlDsXlDPDvSZLxRFULw8wLE2q3JpZbE"

printer = TweetsListener(Bearer_Token)
#añadiendo filtro por palabra
printer.add_rules(tweepy.StreamRule("covid"))
#imprimiendo twets en tiempo real
printer.filter()