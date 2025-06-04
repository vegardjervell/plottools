import matplotlib.pyplot as plt

from . import NormedCmap

def isoplot(df, xid, yid, cid, cmap, norm=None, x_pref=1, y_pref=1, c_pref=1, **plt_kwargs):
    """
    Plot isolines from a dataframe. Exctracts subsets from the dataframe for each uniqe value in df[cid],
    and plots df[xid] vs. df[yid], using the colormap and normaliser to differentiate between df[cid] values.

    Args:
        df (DataFrame) : Contains all the data
        xid (str) : Dataframe key for x-axis
        yid (str) : Dataframe key for y-axis
        cid (str) : Dataframe key for color scale (iso-values)
        cmap (str) : Colormap name
        norm (str) : Use 'log' for logarithmic normalizing of colors, default None
        x_pref (float) : Scaling of x-axis, default 1
        y_pref (float) : Scaling of y-axis, default 1
        c_pref (float) : Scaling of colorbar (forwarded to NormedCmap.scaling), default 1
        plt_kwargs (optional) : Forwarded to plt.plot
    :return:
    """
    if norm is None:
        cmap = NormedCmap(cmap, df[cid], scaling=c_pref)
    else:
        cmap = NormedCmap(cmap, df[cid], norm=norm, scaling=c_pref)

    for c in sorted(set(df[cid])):
        isodata = df[df[cid] == c]
        plt.plot(isodata[xid] * x_pref, isodata[yid] * y_pref, color=cmap(c), **plt_kwargs)

    return cmap