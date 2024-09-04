import os.path
import warnings
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize, LogNorm, SymLogNorm, LinearSegmentedColormap
from matplotlib.cm import ScalarMappable
from matplotlib import colormaps

def truncate_cmap(cmap, start, stop, n=100):
    new_cmap = LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=start, b=stop),
        cmap(np.linspace(start, stop, n)))
    return new_cmap

class NormedCmap:
    def __init__(self, name, lst, norm=Normalize, cutoff=(0, 1), scaling=1):
        if norm == 'log':
            norm = LogNorm
        elif norm == 'symlog':
            norm = SymLogNorm

        self.norm = norm(min(lst) / scaling, max(lst) / scaling)
        self.cmap = colormaps[name]
        self.scaling = scaling
        if (cutoff[0] != 0) or (cutoff[1] != 1):
            self.cmap = truncate_cmap(self.cmap, *cutoff)


    def get_ScalarMappable(self):
        return ScalarMappable(norm=self.norm, cmap=self.cmap)

    def colorbar(self, ax=None, cax=None, **kwargs):
        if (ax is None) and (cax is None):
            ax = plt.gca()
        return plt.colorbar(self.get_ScalarMappable(), ax=ax, cax=cax, **kwargs)
    
    def lined_colorbar(self, lines, ax=None, cax=None, **kwargs):
        cbar = self.colorbar(ax=ax, cax=cax, alpha=0.2, **kwargs)
        cbar.add_lines(lines, linewidths=2, colors=[self(l) for l in lines])
        return cbar

    def __call__(self, val):
        return self.cmap(self.norm(val / self.scaling))

class MarkerCycler:

    def __init__(self, markers=None, exclude_markers=None):
        self.state = 0
        if markers is None:
            markers = ['.', 's', 'v', '|', '^', '1', 'd', '+', 'p', '*', 'P', 'x', '3', 'o', '<', '2', '>', '4', 'h',
                        'D', 'X', 'H', '8', 4]
        if exclude_markers is not None:
            for exc in exclude_markers:
                markers.pop(markers.index(exc))
        self.markers = markers

    def reset(self):
        self.state = 0
    def __call__(self):
        if self.state == len(self.markers):
            warnings.warn('Cycled through all markers! Reusing old markers now.', stacklevel=2)
            self.state = 0
        m = self.markers[self.state]
        self.state += 1
        return m

class ColorCycler:
    def __init__(self):
        self.state = 0
        self.colors1 = [c.split(':')[1] for c in mcolors.TABLEAU_COLORS.keys()]
        self.colors2 = [c for c in mcolors.BASE_COLORS.keys()]
        self.colors = self.colors1 + self.colors2[:-1]

    def reset(self):
        self.state = 0

    def set_cmap(self, name, maxcount):
        cmap = colormaps[name]
        self.colors = [cmap(i / (maxcount + 1)) for i in range(maxcount)]
    def __call__(self):
        if self.state == len(self.colors):
            warnings.warn('Cycled through all colors! Reusing old colors now.', stacklevel=2)
            self.state = 0
        c = self.colors[self.state]
        self.state += 1
        return c

class LinestyleCycler:

    def __init__(self):
        self.state = 0
        self.styles = ['-', '--', ':', '-.', (0, (3, 1, 6, 3)), (0, (1, 3, 3, 6))]

    def __call__(self):
        if self.state == len(self.styles):
            warnings.warn('Cycled through all colors! Reusing old markers now.', stacklevel=2)
            self.state = 0
        s = self.styles[self.state]
        self.state += 1
        return s

class LinestyleGradient:
    # Accepts value between 0 and 1
    # 1 gives a solid line, 0 gives (.5, 3)
    # Intermediate values give varying line/gap length that sum to 6
    def __init__(self, lst=None, reverse=False):
        if lst is not None:
            self.norm = Normalize(min(lst), max(lst))
        else:
            self.norm = None
        self.default = (5.5, 5.5) # linelength, gaplength
        self.reverse = reverse
    def __call__(self, val):
        if self.norm is not None:
            val = self.norm(val)
            if self.reverse is True:
                val = 1 - val
        elif (val < 0) or (val > 1):
            warnings.warn(RuntimeWarning, 'LineStyleGradient only accepts values between 0 and 1 unless a list to normalize to is supplied', stacklevel=2)
        return (0, (self.default[0] * val + 2, self.default[1] * (1 - val)))
