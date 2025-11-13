class TargetLogic:
    def __init__(self, date_str):
        self.date = date_str
        self.targets = self._get_targets()
        
    def get_seasonal_targets(self):
        month = int(self.date[5:7])
        
        if month >= 3 and month <= 5:
            return self.targets["spring_targets"]
        elif month >= 6 and month <= 8:
            return self.targets["summer_targets"]
        elif month >= 9 and month <= 11:
            return self.targets["autumn_targets"]
        elif month == 12 or month >= 1 and month <= 2:
            return self.targets["winter_targets"]
        
    def _get_targets(self):
        return {
            "spring_targets" : [
                "Whirlpool Galaxy", "Bode's Galaxy", "Pinwheel Galaxy", "M106",
                "M66", "Virgo Cluster", "Black Eye Galaxy", "M81", "M63", "M100",
                "Cigar Galaxy"
            ],
            "summer_targets" : [
                "Lagoon Nebula", "Dumbbell Nebula", "M13", "M22",
                "Alpha Centauri", "Butterfly Nebula", "Ring Nebula", "Triangulum Galaxy",
                "Pelican Nebula", "Veil Nebula", "Crescent Nebula"
            ],
            "autumn_targets" : [
                "Andromeda Galaxy", "Triangulum Galaxy", "NGC 6914", "NGC 6910", "NGC 2244",
                "NGC 869", "NGC 884", "Iris Nebula", "Cocoon Nebula", "Bubble Nebula", "Dumbbell Nebula"
            ],
            "winter_targets" : [
                "Rosette Nebula", "Flaming Star Nebula", "Flame Nebula", "Orion Nebula", "M81", "Pleiades",
                "Horsehead Nebula", "NGC 2174", "Cone Nebula", "Crab Nebula", "IC 342"
            ]
        }