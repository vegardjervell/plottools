import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt


def grid_with_cbar(nrows, ncols, cbar_width=0.1, sharey=False, **fig_kwargs):

    fig = plt.figure(**fig_kwargs)
    ax_widths = [(1 - cbar_width) / ncols for _ in range(ncols)]
    gs = GridSpec(nrows, ncols + 1, figure=fig, width_ratios=[*ax_widths, cbar_width])
    axs = [[None for _ in range(ncols)] for _ in range(nrows)]
    for ri in range(nrows):
        for ci in range(ncols):
            if (sharey is True) and (ci > 0):
                axs[ri][ci] = fig.add_subplot(gs[ri, ci], sharey=axs[ri][0])
            else:
                axs[ri][ci] = fig.add_subplot(gs[ri, ci])

    cax = fig.add_subplot(gs[:, -1])
    return axs, cax

def shared_cbar(ncols, cbar_width=1, sharey=False, **fig_kwargs):
    widths = [10 for _ in range(ncols + 1)]
    widths[-1] = cbar_width
    # fig, axs = plt.subplots(1, ncols + 1, gridspec_kw={'width_ratios' : widths}, **fig_kwargs)
    fig = plt.figure(**fig_kwargs)
    gs = GridSpec(1, ncols + 1, width_ratios=widths)
    axs = [_ for _ in range(ncols + 1)]
    axs[0] = fig.add_subplot(gs[0])
    for i in range(1, ncols):
        axs[i] = fig.add_subplot(gs[i], sharey=(axs[0] if (sharey is True) else None))
        if sharey is True:
            plt.setp(axs[i].get_yticklabels(), visible=False)

    axs[-1] = fig.add_subplot(gs[-1])

    return fig, axs