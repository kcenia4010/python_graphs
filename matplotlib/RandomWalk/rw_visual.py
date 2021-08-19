import matplotlib.pyplot as plt 
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.Blues, 
        edgecolors ='none', s=15)

    #удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    #Выделение первой и последней точек
    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break