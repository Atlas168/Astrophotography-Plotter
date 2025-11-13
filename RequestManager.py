from PlotterDataPrep import PlotterDataPrep
from Plotter import Plotter
from TargetLogic import TargetLogic
from astropy.coordinates import SkyCoord
from astropy.time import Time
from termcolor import colored

class RequestManager:
    def __init__(self, offset, location):
        print(colored("--Space Plotter created by Beverly Bialke on 29 June, 2025--\n", "light_cyan"))
        self.offset = offset
        self.location = location
        self.date = None
        
    def _setup(self):
        self.tl = TargetLogic(self.date)
        self.pdp = PlotterDataPrep(self.date, self.offset, self.location)
        self.p = Plotter(self.pdp.get_delta_midnight(), self.pdp.get_sun_data(), self.pdp.get_moon_data(), self.date)
        
    def plot(self):
        choice = self._get_user_choice()
        self._setup()
        
        if choice == "M":
            print(colored(f"Preparing data for multiple targets...", "yellow"))
            target = self.tl.get_seasonal_targets()
            self.p.plot_multiple(self.pdp.get_target_coords(target), target)
        elif choice == "S":
            while True:
                target = [input("Enter the name of the object you would like to plot (ex. M33): ")]
                try:
                    SkyCoord.from_name(target[0])
                except:
                    print(colored("That input is not valid.", "red"))
                else:
                    break
            print(colored(f"Preparing data for {target[0]}...", "yellow"))
            self.p.plot_single(self.pdp.get_target_coords(target), target[0])

    def _get_user_choice(self):
        while True:
            self.date = input("Enter a date in the following format: YYYY-MM-DD: ")
            try:
                test = Time(f"{self.date} 00:00:00")
            except ValueError:
                print(colored("That input is not valid.", "red"))
                continue
            else:
                break
        choice = ""
        while not choice == "M" and not choice == "S":
            choice = input("Please type \"M\" to plot multiple objects or \"S\" to plot one: ")
        return choice