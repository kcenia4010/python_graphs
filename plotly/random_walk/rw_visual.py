from plotly.graph_objs import Bar, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

data = []