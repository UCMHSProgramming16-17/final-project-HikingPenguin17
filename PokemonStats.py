# Import all needed functions
import csv
import pandas as pd
import bokeh

# Create a value for the csv file
data = pd.read_csv('Pokemon.csv')

# Import needed inputs from bokeh.charts
from bokeh.charts import Scatter, output_file, save

# Import needed palette from bokeh.palettes
from bokeh.palettes import Magma

# Create "tooltips" value and add information
tooltips = [
    ('Name', '@Name'),
    ('Defense Stat', '@Defense'),
    ('Speed Stat', '@Speed')
]

# Organize data into scatter plot form
p = Scatter(data, x = 'Speed', y = 'Defense', title = 'Speed vs. Defense Stats', xlabel = 'Speed', ylabel = 'Defense', color = 'Type 1', tooltips = tooltips, palette = Magma(1))

# Create designated output file
output_file('speedvsdefense.html')

# Save the created graph to the html
save(p)