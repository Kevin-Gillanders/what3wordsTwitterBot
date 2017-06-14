import requests
import pprint as pp
import json
import time
import tweepy
import urllib.request

consumer_key = ""
consumer_secret = ""


access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


count = 0
wordnikAPIKey = ''
w3WAPIKey = ''
googleMapsAPIKey = ''
staticMapAPIKey = ''
# for status in tweepy.Cursor(api.user_timeline).items():
#     try:
#         api.destroy_status(status.id)
#         print( "Deleted:", status.id)
#     except:
#         print("Failed to delete:", status.id)





while count < 100:
    count += 1
    words = []
    try :
        r = requests.get("http://api.wordnik.com:80/v4/words.json/randomWords?hasDictionaryDef=true&minCorpusCount=60&minLength=5&maxLength=15&limit=3&api_key=" + wordnikAPIKey)
        # print(r.json())
        r = json.loads(str(r.json()).replace("'", '"').replace("-", ""))
        # print(r)
    except json.decoder.JSONDecodeError:
        print("funny word")
        time.sleep(2)


    for word in r:
        print("=======================")
        print(word['word'])
        words.append(word['word'])


    # words = ['swaps','string','bland']
    r = requests.get("https://api.what3words.com/v2/autosuggest?addr=" + ".".join(words) + "&key=" + w3WAPIKey + "&lang=en&format=json&display=full")

    try:
        print("===============================")
        r = json.loads(str(r.json()).replace("'", '"'))
        r = json.loads(str(r['suggestions']).replace("'", '"'))
        print("+++++++++++++++++++++++++++++++++")

        for x in r:
            x = json.loads(str(x).replace("'", '"'))
            print("Words : {}".format(x['words']))
            print("Place : {}, Country : {}".format(x['place'], x['country']))
            print('Longtitude : {}, Latitude : {}'.format(x['geometry']['lng'], x['geometry']['lat']))
            print("+++++++++++++++++++++++++++++++++")
            #                                   lat          long
            # https://www.google.ie/maps/search/5.487589,+100.583049
            # https://google.com/maps/?q=-15.623037,18.388672
            lat = x['geometry']['lat']
            longtitude = x['geometry']['lng']
            sign = ''
            if longtitude > 0:
                sign = '+'
            else:
                sign = ''
            tweet = str('Words : '+ ', '.join(x['words'].split('.')) + '\nPlace : ' + x['place'] + ', Country : ' + x['country']+ '\nhttps://google.com/maps/?q=' + str(lat) + ',' + sign + str(longtitude) )

            mapsURL = 'https://maps.googleapis.com/maps/api/staticmap?center=' + str(lat) + ',' + sign + str(longtitude) + '&zoom=6&markers=size:mid|color:red|' + str(lat) + ',' + sign + str(longtitude) + '&size=400x400&key=AIzaSyCXZwf5m5mM6dSa2FCvT63hdRp9JCXT_W8'
            urllib.request.urlretrieve(mapsURL, './test.png')
            # + \nLat : ' + str(x['geometry']['lat']) + ', Long : ' + str(x['geometry']['lng']))
            print("\ntweet : \n{}\n".format(tweet))
            api.update_with_media('/home/kevin/twitterBot/test.png', status = tweet, lat = lat , long = longtitude)
            time.sleep(600)
            break
        print("===============================\n")

    except KeyError:
        time.sleep(2)
        print("Nuh uh")
    except json.decoder.JSONDecodeError:
        time.sleep(2)
        print("Funny word 2")



