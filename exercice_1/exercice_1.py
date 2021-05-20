# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:53:14 2021

@author: felix
"""

from qiskit import IBMQ, BasicAer

from qiskit import QuantumCircuit, execute

# import basic plot tools
from qiskit.visualization import plot_histogram

import matplotlib.pyplot as plt


def show_figure(fig):
    new_fig = plt.figure()
    new_mngr = new_fig.canvas.manager
    new_mngr.canvas.figure = fig
    fig.set_canvas(new_mngr.canvas)
    plt.show(fig)
    