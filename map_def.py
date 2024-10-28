import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LatitudeFormatter,LongitudeFormatter
import cartopy.feature as cfeature
import matplotlib.ticker as mticker

def mapping(south,north,west,east,fs,dx,dy,cres,lc):
    proj = ccrs.PlateCarree(central_longitude=180)
    
    # Projection
    ax = plt.axes(projection=proj)

    # 枠線（spines）の太さを変更
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)  
        
    ax.tick_params(axis='both', width=1.5)
    
    # Set ticks interval
    dlon,dlat=dx,dy
    #xticks=np.arange(west+0.5,east+0.01,dlon) #ori
    #yticks=np.arange(south+0.5,north+0.01,dlat) #ori
    xticks=np.arange(west,east,dlon)
    yticks=np.arange(south,north,dlat)
    ax.set_xticks(xticks,crs=proj)
    ax.set_yticks(yticks,crs=proj)
    ax.tick_params(axis='both',which='major', pad=10, labelsize=fs)

    # Land Color
#    ax.add_feature(cfeature.LAND.with_scale(cres),color=lc,zorder=0)
    ax.add_feature(cfeature.GSHHSFeature(scale='high', levels=None),color=lc,zorder=3)
#    ax.add_feature(cfeature.OCEAN.with_scale(cres),color=lc,zorder=3)
#    ax.add_feature(cfeature.OCEAN.with_scale(cres),color='gray')
#    ax.add_feature(cfeature.LAND.with_scale(cres),color=lc)

    #Add country borders
    ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=1, edgecolor='black', zorder=4)

    # Label defines
    latfmt=LatitudeFormatter()
    lonfmt=LongitudeFormatter(zero_direction_label=True)
    ax.xaxis.set_major_formatter(lonfmt)
    ax.yaxis.set_major_formatter(latfmt)
    ax.axes.tick_params(labelsize=fs)

    # Costal resolution & domain setting
    ax.set_extent((west, east, south, north), proj)

    return ax
