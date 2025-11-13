import numpy as np
from astropy.time import Time
from astropy.coordinates import AltAz, SkyCoord, get_sun, get_moon
import astropy.units as u

class PlotterDataPrep:
    def __init__(self, date_str, offset_hours, location):
        self.utcoffset = offset_hours*u.hour
        self.location = location
        self.date = date_str
        midnight = Time(f"{self.date} 00:00:00") - self.utcoffset
        self.delta_midnight = np.linspace(-12, 12, 1000) * u.hour
        self.times_night = midnight + self.delta_midnight
        self.frame_night = AltAz(obstime=midnight + self.delta_midnight, location=self.location)
        
    def get_moon_data(self):
        return get_moon(self.times_night).transform_to(self.frame_night)
    
    def get_sun_data(self):
        return get_sun(self.times_night).transform_to(self.frame_night)
    
    def get_target_coords(self, names):
        coords = [SkyCoord.from_name(name) for name in names]
        if len(names) <= 1:
            return coords[0].transform_to(self.frame_night)
        else:
            return [coord.transform_to(self.frame_night) for coord in coords]
    
    def get_delta_midnight(self):
        return self.delta_midnight