# Get into the GitHub folder and proceed to the folder labeled (your username)
#Type "source activate data" to activate data mode
# Type python3 to activate python3

# Import all needed data
import pandas as pd
import numpy as np

# Create "data" using Pokemon.csv
data = pd.read_csv('Pokemon.csv')

# Import Donut, output_file, and save from bokeh.charts
from bokeh.charts import Donut, output_file, save

# Name your ouput file with an html ending
output_file('pokemontypes.html')

# Import desired color palette from bokeh.palette
from bokeh.palettes import plasma

# Create "p" with all wanted data, titles, and desired color palette
p = Donut(data, label = 'Type 1', palette = plasma(11))

# Save "p"
save(p)