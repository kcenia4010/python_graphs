import csv 
from plotly.graph_objs import Scatter, Layout 
from plotly import offline

filename = 'C:/Users/Kceni/Desktop/personal_projects/math/data/earthquakes/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    heared = next(reader)

    lons, lats, squares = [], [], []
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        squares.append(float(row[2]))
    
    
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': squares,
    'marker': {
        'size': [int(square/20) for square in squares],
        'color': squares,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
   },
 }]
my_layout = Layout(title='Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='C:/Users/Kceni/Desktop/personal_projects/math/data/earthquakes/fires.html')

