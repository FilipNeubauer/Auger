import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe


def specif_stations_blue(*arg):
    for i in arg:
        id = sdmap.index[sdmap["id"] == i[0]]
        station = sdmap.iloc[id]
        plt.scatter(x=station.easting, y=station.northing, s=30, c="blue")
        plt.text(station.easting, station.northing, i[1], size=9, color="blue", path_effects=[pe.withStroke(linewidth=2, foreground="black")])


def specif_stations_red(*arg):
    for i in arg:
        id = sdmap.index[sdmap["id"] == i[0]]
        station = sdmap.iloc[id]
        plt.scatter(x=station.easting, y=station.northing, s=30, c="red")
        plt.text(station.easting, station.northing, i[1], size=9, color="red", path_effects=[pe.withStroke(linewidth=2, foreground="black")])


def specif_stations_green(*arg):
    for i in arg:
        id = sdmap.index[sdmap["id"] == i]
        station = sdmap.iloc[id]
        plt.scatter(x=station.easting, y=station.northing, s=30, c="green")
        plt.text(station.easting, station.northing, i[1], size=9, color="green", path_effects=[pe.withStroke(linewidth=2, foreground="black")])


sdmap = pd.read_csv("auger/sdMap.csv")

#print(sdmap.columns)

plt.figure(figsize=(8, 8))
plt.scatter(x=sdmap.easting, y=sdmap.northing, s=20, c="grey")  

# top 5 SD with most events:
specif_stations_red((735, 156), (719, 151), (722, 147), (762, 145), (578, 144))

# SD with most events
#specif_stations_red((735, 156))


plt.xlim(439000, 510000)
plt.ylim(6065000, 6140000)
plt.xlabel('UTM Easting [m]')
plt.ylabel('UTM Northing [m]')

LL= [6071871.5, 459208.3, 1416.2]
LM= [6094570.2, 498903.7, 1416.4]
LA= [6134058.4, 480743.1, 1476.7]
CO= [6114140.0, 445343.8, 1712.3]

plt.scatter(LL[1], LL[0], marker='^', s=500, label='LL')
plt.scatter(LM[1], LM[0], marker='^', s=500, label='LM')
plt.scatter(LA[1], LA[0], marker='^', s=500, label='LA')
plt.scatter(CO[1], CO[0], marker='^', s=500, label='CO')

plt.annotate('Los Leones', xy=(LL[1]+4000, LL[0]-4000), weight="bold")
plt.annotate('Los Morados', xy=(LM[1]-4000, LM[0]-5000), weight="bold")
plt.annotate('Loma Amarilla', xy=(LA[1]-16000, LA[0]), weight="bold")
plt.annotate('Coihueco', xy=(CO[1]-6000, CO[0]+5500), weight="bold")

plt.title("SD with most event occurences", size=17)

plt.show()
