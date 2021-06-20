"""Plotting CPU and Ram data in real time."""

from collections import deque

import matplotlib.pyplot as plt
import numpy as np
import psutil

from matplotlib.animation import FuncAnimation


def update(i):
    """Update the data."""
    # get data
    cpu.popleft()
    cpu.append(psutil.cpu_percent())
    ram.popleft()
    ram.append(psutil.virtual_memory().percent)

    # clear axis
    ax.cla()
    ax1.cla()

    # plot cpu
    ax.plot(cpu)
    ax.scatter(len(cpu)-1, cpu[-1])
    ax.text(len(cpu)-1, cpu[-1]+2, "{}%".format(cpu[-1]))
    ax.set_ylim(0,100)

    # plot memory
    ax1.plot(ram)
    ax1.scatter(len(ram)-1, ram[-1])
    ax1.text(len(ram)-1, ram[-1]+2, "{}%".format(ram[-1]))
    ax1.set_ylim(0,100)


if __name__ == "__main__":

    # start collections with zeros
    cpu = deque(np.zeros(10))
    ram = deque(np.zeros(10))

    # define and adjust figure
    fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')
    ax = plt.subplot(121)
    ax1 = plt.subplot(122)
    ax.set_facecolor('#DEDEDE')
    ax1.set_facecolor('#DEDEDE')

    # animate
    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()
