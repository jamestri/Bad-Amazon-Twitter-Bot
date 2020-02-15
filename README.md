# Bad Amazon Review Bot

This bot utilizes twitter api using [tweepy](https://github.com/tweepy/tweepy) and an html scraper found at: [https://www.scrapehero.com/how-to-scrape-amazon-product-reviews/](https://www.scrapehero.com/how-to-scrape-amazon-product-reviews/)
The scraper has been modified in order to get the worst reviews and put them in a dictionary rather than a json.

### Requirements

Needs Python 3.8 and tweepy 3.8, and anything else needed for the html scraper. You're smart, you'll figure it out.
IN ORDER TO USE TWEEPY, YOU NEED A TWITTER DEVELOPER ACCOUNT which you can get [here](https://developer.twitter.com/)

### Use

Run by using
```bash
python ./bot.py
```
and also putting in your own api keys from your twitter developer app.

If people mention you in a tweet (e.g. @twitterID) and then provide an amazon product link, the bot should tweet back the worst review for that product.

### Contributing

If you find any bugs open an issue