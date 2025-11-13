# Astrophotography_Plotter
**A plotter which gets the altitudes for astrophotography targets based on a user-specified date and plotting style.**

## Features
- Computes the altitude of common astrophotography targets
- "Multiple" and "single" target modes
- Moon luminance bar
  
Users edit the Main file with their latitude, longitude, altitude, and UTC offset.

## Requirements
This project uses several Python libraries, including:
- **astropy** for unit transformations and altitude values
- **ephem** for moon luminance
- **numpy** for calculations and arrangement
- **matplotlib** for visualization
- **termcolor** for console styling

To install these libraries, run the following command in a console:

*pip install astropy ephem numpy matplotlib termcolor*

## Example Plot
Below is the "multiple" target plot for 2 December 2025.

<img width="936" height="504" alt="Plotter Example 2 (better)" src="https://github.com/user-attachments/assets/f4a2383c-ff95-437c-9b1e-859f46579546" />


This program was built using astropy's tutorial ["Determining and plotting the altitude/azimuth of a celestial object"](https://docs.astropy.org/en/latest/coordinates/example_gallery_plot_obs_planning.html) as a starting point.
