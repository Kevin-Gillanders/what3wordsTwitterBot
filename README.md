# what3wordsTwitterBot
A call is made to the [wordnik API](http://developer.wordnik.com/docs.html#!/words/getRandomWord_get_4) for three random words

Those words are then given to [what3words' API](https://docs.what3words.com/api/v2/), which provides a latitude and longtitude, 

These are then given to [google maps static API](https://developers.google.com/maps/documentation/static-maps/) for the image

It is then tweeted out through [tweepy](http://tweepy.readthedocs.io/en/v3.5.0/)


This is a work in progress and as such not completed
