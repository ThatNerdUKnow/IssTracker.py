# IssTracker.py
An iss tracking app using the google maps static API and openCV2 for python

The way this program works is that we poll an api to get the coordinates for the international space station every few seconds. We then use the latitude and longitude returned to us to build a query string to send to the google maps api

You will have to supply your own api key, but they are freely available so long as you stay under a daily request budget
