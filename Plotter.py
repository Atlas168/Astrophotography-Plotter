import matplotlib.pyplot as plt
import astropy.units as u
from astropy.visualization import astropy_mpl_style, quantity_support
from MoonLogic import MoonLogic
import numpy as np

class Plotter:
    def __init__(self, delta_midnight, sun_altaz, moon_altaz, date):
        plt.style.use(astropy_mpl_style)
        quantity_support()
        self.delta_midnight = delta_midnight
        self.sun_altaz = sun_altaz
        self.moon_altaz = moon_altaz
        self.date = date
        self.ml = MoonLogic(date)
        
    def _plot_basics(self, ax):
        ax.fill_between(self.delta_midnight, 0*u.deg, 90*u.deg, self.sun_altaz.alt < -0*u.deg, color="0.5", zorder=0)
        ax.fill_between(self.delta_midnight, 0*u.deg, 90*u.deg, self.sun_altaz.alt < -18*u.deg, color="k", zorder=0)
        ax.plot(self.delta_midnight, self.sun_altaz.alt, color='#FFBF00', ls="dashed", label="Sun")
        ax.plot(self.delta_midnight, self.moon_altaz.alt, color="#d0d0d0", ls="dotted", label="Moon")
        ax.set_xlim(-12 * u.hour, 12 * u.hour)
        ax.set_xticks((np.arange(13) * 2 - 12) * u.hour)
        ax.set_ylim(0 * u.deg, 90 * u.deg)
        ax.set_xlabel('Hours from Midnight')
        ax.set_ylabel('Altitude (degrees)')
        ax.set_title(f"Night of {self.date}")
        ax.legend()
        
    def plot_single(self, coord, label):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7), gridspec_kw={'width_ratios': [12, 1]})
        fig.canvas.manager.set_window_title("Space Plotter")
        ax1.scatter(self.delta_midnight, coord.alt, c=coord.az.value, label=label, lw=0.01, cmap="winter")
        self._plot_basics(ax1)
        self._plot_maxes(coord, ax1)
        self._plot_moon(ax2)
        plt.show()
        
    def plot_multiple(self, coords, labels):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 7), gridspec_kw={'width_ratios': [12, 1]})
        fig.canvas.manager.set_window_title("Space Plotter")
        colors = [
        "lightcoral", "maroon", "tomato", "chocolate", "sandybrown", "gold", "goldenrod",
        "olivedrab", "palegreen", "teal", "skyblue", "mediumpurple", "darkviolet", "plum"
        ]
        for i, (coord, label) in enumerate(zip(coords, labels)):
            ax1.scatter(self.delta_midnight, coord.alt, lw = 0.01, c=colors[i % len(colors)],  label=label)
            self._plot_maxes(coord, ax1)
        
        self._plot_basics(ax1)
        self._plot_moon(ax2)
        plt.show()
        
    def _plot_moon(self, ax):
        phase = self.ml.calculate_phase()
        illumination = self.ml.get_illumination()
        if not phase == None:
            ax.bar(f"Moon\nIllumination\n({phase})", illumination, color="gray", width = 0.6)
        else:
            ax.bar(f"Moon\nIllumination", illumination, color="gray", width = 0.6)
        ax.set_ylabel('% Illuminated', fontsize = 12)
        ax.set_ylim(0, 100)
        ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        ax.grid(axis = "x")
        
    def _plot_maxes(self, coord, ax):
        max_index = np.argmax(coord.alt)
        xmax = self.delta_midnight[max_index]
        ymax = coord.alt[max_index]
        ax.scatter(xmax, ymax, c="white", zorder=5, alpha = .65)