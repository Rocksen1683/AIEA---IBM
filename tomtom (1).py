import configparser
import requests
import json
import sys
import time
import datetime

from urllib.request import urlopen

# URL to the tomtom api
apiURL      = "https://api.tomtom.com/routing/1/calculateRoute/"
# apiKey
apiKey      = "MUAVy3N4eped1SgJto6PEAKg2fvYGRKC"

# function that returns ETA when source and destination coordinates are given as parameters

def get_ETA(source, dest):
    tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % (apiURL,source[0], source[1], dest[0], dest[1],apiKey)

    getData = urlopen(tomtomURL).read()
    jsonTomTomString = json.loads(getData)

    totalTime = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']

    return totalTime
