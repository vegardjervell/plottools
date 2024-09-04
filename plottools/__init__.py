from . import cyclers, style, layouts

set_style = style.set_style
get_figsize = style.get_figsize

NormedCmap = cyclers.NormedCmap
MarkerCycler = cyclers.MarkerCycler
ColorCycler = cyclers.ColorCycler
LinestyleCycler = cyclers.LinestyleCycler
LinestyleGradient = cyclers.LinestyleGradient

shared_cbar = layouts.shared_cbar