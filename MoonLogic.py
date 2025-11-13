import ephem

class MoonLogic:
    def __init__(self, date_str):
        self.date = date_str
        observer = ephem.Observer()
        observer.date = self.date
        moon = ephem.Moon(observer)
        self.illumination = moon.phase
        
    def get_illumination(self):
        return self.illumination
        
    def calculate_phase(self):
        if (self.illumination <= 10):
            return "New Moon"
        elif (self.illumination < 90):
            return self._waxing_or_waning(self.illumination)
        else:
            return "Full Moon"
            
    def _waxing_or_waning(self, illumination):
        if (int(self.date[8:]) < 28):
            tempDate = int(self.date[8:]) + 1
            newObs = ephem.Observer()
            newObs.date = self.date[:4] + "-" + self.date[5:7] + "-" + str(tempDate)
            if (illumination < ephem.Moon(newObs).phase):
                return "Waxing"
            elif (illumination > ephem.Moon(newObs).phase):
                return "Waning"