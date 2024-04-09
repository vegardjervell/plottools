import matplotlib.pyplot as plt
import os
import numpy as np

def set_style():
    plt.style.use(os.path.dirname(__file__) + '/fancyfonts.mplstyle')

def get_figsize(textwidthfrac=None, linewidthfrac=1, height_ratio=1):
    # for use with width = textwidthfrac * \textwidth
    # Height will be height_ratio * width / golden_ratio

    doclinewidth = 246.0 # \the\linewidth (for two-column) # 455.24411
    doctextwidth = 510.0 # 455.24411 # pt (print with \the\textwidth in Latex document)
    textwidth = 0.01389 * doctextwidth # Converting to inches (unit in matplotlib)
    linewidth = 0.01389 * doclinewidth # Converting to inches (unit in matplotlib)
    if textwidthfrac is None:
        figwidth = linewidthfrac * linewidth
    else:
        figwidth = textwidthfrac * textwidth
    golden_ratio = (1 + np.sqrt(5)) / 2
    figheight = height_ratio * figwidth / golden_ratio
    return (figwidth, figheight)