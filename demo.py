import matplotlib.pyplot as plt
import numpy as np
from plottools import set_style, get_figsize
from plottools.cyclers import NormedCmap, ColorCycler, MarkerCycler, LinestyleCycler, LinestyleGradient

set_style() # Sets matplotlib to use the custom matplotlibrc file fancyfonts.mpl

T_lst = np.linspace(0, 3, 5)
x_lst = np.linspace(0, 6)
cmap = NormedCmap('cool', T_lst) # matplotlib 'cool' cmap, with normalization for use with T_lst (1-100)

# NOTE: The get_figsize function bases the figure dimensions on the document textwidth or linewidth, and the golden ratio
# The document textwidth and linewidth are hardcoded into the function, and can be modified there.
# The height of the figue is computed as (width * golden_ratio), and can be modified using the height_ratio kwarg,
#   which changes the height to (width * golden_ratio * height_ratio).
plt.figure(figsize=get_figsize(textwidthfrac=1)) # Create a figure with width equal to the textwidth
for T in T_lst:
    plt.plot(x_lst, np.sin(x_lst + T), color=cmap(T))
cmap.colorbar(label='$T$') # Generates a colorbar on the current axes
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

plt.figure(figsize=get_figsize(linewidthfrac=1.5)) # Create a figure with width equal to 1.5 * the linewidth
for T in T_lst:
    plt.plot(x_lst, np.sin(x_lst + T), color=cmap(T))
cmap.lined_colorbar(T_lst, label='$T$') # Generates a "lined colorbar" on the current axes
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

plt.figure(figsize=get_figsize(textwidthfrac=.5)) # Create a figure with width equal to half the textwidth
lsg = LinestyleGradient(T_lst) # Generates linestyles based on values in T_lst
for T in T_lst:
    plt.plot(x_lst, np.sin(x_lst + T), color=cmap(T), linestyle=lsg(T), label=f'{T:.2f}')
plt.legend(title='$T$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()


plt.figure(figsize=get_figsize(linewidthfrac=1, height_ratio=2)) # Create a tall figure with width equal to the linewidth
# Custom cyclers to generate markers, colors, and linestyles
mc = MarkerCycler()
cc = ColorCycler()
lc = LinestyleCycler()
for T in T_lst:
    plt.plot(x_lst, np.sin(x_lst + T), color=cc(), linestyle=lc(), marker=mc(), label=f'{T:.2f}')
plt.legend(title='$T$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()

