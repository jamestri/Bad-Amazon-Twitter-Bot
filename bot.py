import tweepy
import time
import amazon_reviews


CONSUMER_KEY = 'get your own'
CONSUMER_SECRET = 'get your own'

ACCESS_KEY = 'get your own'
ACESS_SECRET = 'get your own'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

print("starting bot")
def RetrieveLastID(fname):
    fread = open(fname, 'r')
    id = int(fread.read().strip())
    fread.close()
    return id


def StoreLastID(id, fname):
    frite = open(fname, 'w')
    frite.write(str(id))
    frite.close()
    return


def TweetReply():
    id = RetrieveLastID('id.txt')

    mentions = api.mentions_timeline(id, tweet_mode="extended")
    
    for mention in reversed(mentions):
        id = mention.id
        StoreLastID(id, 'id.txt')
        mentionText = mention.full_text.lower()
        mentionText = mentionText.encode("utf-8")
        print(mentionText)
        url = ""
        for urll in mention.entities['urls']:
            expanded_url = urll['expanded_url']
            if 'amazon.com' in expanded_url:
                url = expanded_url


        if 'amazon.com' in url:
            print('fetching Amazon Listing...')
            print(url)
            if '/dp/' in url:
                index = url.index("/dp/")
                url = url[index:]
                url = url[4:]
                asin = url[:10]
                print(asin)
                review = amazon_reviews.ReadAsin(asin)
                #check if review is good
                tweetMessage = ParseDict(review)
                tweet = '@' + mention.user.screen_name + " " + tweetMessage + "\""
                tweet = tweet[:280]
                api.update_status(tweet, mention.id)


def ParseDict(dict):
    message = "By: " + dict['review_author']
    message += " Rated: " + dict['review__rating'] + ' stars'
    message += " \"" + dict['review_text'] + "\""
    return message

while True:
    TweetReply()
    time.sleep(15)

