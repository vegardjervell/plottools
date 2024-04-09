import os.path
import warnings
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import Normalize, LogNorm, SymLogNorm
from matplotlib.cm import ScalarMappable
from matplotlib import colormaps

class NormedCmap:
    def __init__(self, name, lst, norm=Normalize):
        if norm == 'log':
            norm = LogNorm
        elif norm == 'symlog':
            norm = SymLogNorm
        self.norm = norm(min(lst), max(lst))
        self.cmap = colormaps[name]

    def get_ScalarMappable(self):
        return ScalarMappable(norm=self.norm, cmap=self.cmap)

    def colorbar(self, ax=None, cax=None, **kwargs):
        plt.colorbar(self.get_ScalarMappable(), ax=ax, cax=cax, **kwargs)

    def __call__(self, val):
        return self.cmap(self.norm(val))

class MarkerCycler:

    def __init__(self):
        self.state = 0
        self.markers = ['.', 's', 'v', '|', '^', '1', 'd', '+', 'p', '*', 'P', 'x', '3', 'o', '<', '2', '>', '4', 'h',
                        'D', 'X', 'H', '8', 4]

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
    def __init__(self, lst=None):
        if lst is not None:
            self.norm = Normalize(min(lst), max(lst))
        else:
            self.norm = None
        self.default = (5.5, 5.5) # linelength, gaplength
    def __call__(self, val):
        if self.norm is not None:
            val = self.norm(val)
        elif (val < 0) or (val > 1):
            warnings.warn(RuntimeWarning, 'LineStyleGradient only accepts values between 0 and 1 unless a list to normalize to is supplied', stacklevel=2)
        return (0, (self.default[0] * val + 1, self.default[1] * (1 - val)))