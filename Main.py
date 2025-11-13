import astropy.units as u
from astropy.coordinates import EarthLocation
from termcolor import colored
from RequestManager import RequestManager

'''
    CREATED BY: BEVERLY BIALKE
    CREATED ON: 29 JUNE 2025
                            '''


#USER INFO HERE:
#Hour difference compared to UTC - Google this
offset = 0

#Latitude, Longitude, and Elevation of location - Google this
latitude = 0 #degrees North
longitude = 0 #degrees East
altitude = 0 #meters above sea level


#Nothing below needs to be edited
location = EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=altitude*u.m)

rm = RequestManager(offset, location)

rm.plot()
