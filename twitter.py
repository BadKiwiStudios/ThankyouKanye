import random
import tweepy

auth = tweept.0AuthHandler("accesskeys","secretkey")
auth.set_access_token(,)
api = tweepy.API(auth)

def memify(text):
    new = []
    b = '.. ok boomer'
    for i in range(len(lext)-len(b)):
        c = text[i]
        r = random.randint(0,1)
        if r:
            new.append(c.upper())
        else:
            new.append(c.lower())
        return''.join(new + [b])

tweets = api.user_timeline(screen_name="kanyewest")
first_tweet = tweets[0]
api.update_status("Thank you @kanyewest, very cool")
