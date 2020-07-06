import requests
import json
import time
import cv2
import numpy as np
import datetime


url = 'http://api.open-notify.org/iss-now.json'
maps = "https://maps.googleapis.com/maps/api/staticmap?"
api_key = '&key=yourapikeyhere'
size = "&size=1280x720"

# print(data['iss_position'])
session = datetime.datetime.today()


url = "https://maps.googleapis.com/maps/api/staticmap?"
iss = "http://api.open-notify.org/iss-now.json"

while True:
    # Get position of ISS
    issreq = requests.get(iss)
    position = issreq.json()
    center = position["iss_position"]["latitude"] + \
        "," + position["iss_position"]["longitude"]
    timestamp = position["timestamp"]

    print(str(timestamp) + ': ' + center)

    # Generate query string for google maps
    marker = "&markers=" + center
    zoom = "&zoom=4"
    fullpath = url + "center=" + center + size + api_key + zoom + marker

    # Send request to google maps
    r = requests.get(fullpath)

    # Save response as png and displays it in a window
    f = open('iss.png', 'wb')
    f.write(r.content)
    f.close()
    img = cv2.imread('iss.png')
    cv2.imshow('iss', img)
    cv2.waitKey(1)
    time.sleep(5)
cv2.destroyAllWindows()
