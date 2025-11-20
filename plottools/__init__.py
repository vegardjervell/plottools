from . import cyclers, style, layouts, scales

set_style = style.set_style
get_figsize = style.get_figsize

NormedCmap = cyclers.NormedCmap
MarkerCycler = cyclers.MarkerCycler
ColorCycler = cyclers.ColorCycler
LinestyleCycler = cyclers.LinestyleCycler
LinestyleGradient = cyclers.LinestyleGradient

shared_cbar = layouts.shared_cbar
shared_cbar_vertical = layouts.shared_cbar_vertical

LinearInflate = scales.LinearInflate