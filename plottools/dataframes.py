import numpy as np
from .cyclers import NormedCmap
import matplotlib.pyplot as plt

def get_iso(df, key, tol=0, mincount=0):
    iso = {}
    for val in df[key]:
        for ival in iso:
            if ival - tol <= val <= ival + tol:
                val = ival
                break

        if val in iso.keys():
            iso[val] += 1
        else:
            iso[val] = 1

    if mincount == 0:
        return np.array(sorted(list(iso.keys())))

    isovals = []
    for val, count in iso.items():
        if count >= mincount:
            isovals.append(val)

    return np.array(sorted(isovals))

def plot_iso(df, isokey, xkey, ykeys, isocmap, x_unit=1, y_unit=1, isotol=0):
    isovals = get_iso(df, isokey)
    cmap = NormedCmap(isocmap, isovals)
    for ival in isovals:
        isodata = df[(ival - isotol <= df[isokey]) & (df[isokey] < ival + isotol)].sort_by(xkey)

        for ykey in ykeys:
            plt.plot(isodata[xkey] * x_unit, isodata[ykey] * y_unit, color=cmap(ival))

        plt.plot([], [], color=cmap(ival), label=ival)