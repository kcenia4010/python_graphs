import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#изменение структуры данных
filename = 'C:/Users/Kceni/Desktop/personal_projects/math/data/earthquakes/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'C:/Users/Kceni/Desktop/personal_projects/math/data/earthquakes/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

#Нанесение данных на карту
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'YlGnBu',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    },
 }]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='C:/Users/Kceni/Desktop/personal_projects/math/data/earthquakes/global_earthquakes.html')