import matplotlib.pyplot as plt 
from die import Die

die_1 = Die()
die_2 = Die()
max_size = die_1.num_sides + die_2.num_sides
results = [die_1.roll()+die_2.roll() for i in range(1000)]
frequencies = [results.count(value) for value in 
    range(2, max_size+1)]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(x=list(range(2, max_size+1)), height=frequencies, bottom=1, tick_label=list(range(2, max_size+1)))

plt.show()

