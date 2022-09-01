import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime
import pytz

#jank sorting algorithnm
useful = ['agreed', 'deal', 'cleanse', 'jersey', 'signing', 'sign', 'trading', 'claimed', 'extension', 'finalizing', 'returning', 'return', 'sending', 'landing']
garbage = ['investing', 'attract', 'matched.', 'espn story', 'prepare', 'wish', 'confirms', 'expected', 'also in the deal', 'declined', 'declining', 'discussing', 'negotiate', 'ruled out', 'staff', 'https', 'female', 'eventually']
utc = pytz.UTC
date = datetime.datetime(2022, 6, 30)
date = utc.localize(date)
date3 = datetime.datetime(2022, 10, 19)


#Uses snscrape to scrape shams and woj tweets and convert them to CSVs
def tweets_to_csv(user):
    tweets = []

    for tweet in sntwitter.TwitterUserScraper(user).get_items():
        # print(vars(tweet))
        date2 = tweet.date
        content = tweet.content.lower()
        good = False

        for word in useful:
            if content.find(word) == -1:
                good = False
            else:
                good = True
                break
        
        for word in garbage:
            if content.find(word) != -1:
                good = False
                break

        if date > date2:
            break
        else:
            if good == True:
                tweets.append([tweet.date, tweet.user, tweet.content])

    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Content'])
    df.to_csv(df.to_csv (fr'C:\Users\User\Desktop\code\personal\wojvshams webscraping\{user}.csv', index = False, header=True))


shams = tweets_to_csv('ShamsCharania')
woj = tweets_to_csv('wojespn')
