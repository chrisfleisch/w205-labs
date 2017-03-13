import tweepy

consumer_key = "v0URSYiE7qBuYExcsa0TuTbPt";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "5PTdoFPNGApnrvPN7qBmIbYLTZLtW1EwyEe9XqPG9qVN7hWMWM";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "338459533-gZa4xb8w5ayVTPY8DRgWYLSFzMGxM3Xn0WWNkxbp";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "jr8t1wURWCePrjRbqzr6rzOBrmS9Yl8VQyd2sCjupHgzW";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



