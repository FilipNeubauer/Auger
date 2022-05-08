import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("auger/dataSummary.csv")

data = data.drop_duplicates("id")

data = data.loc[:, ["sd_northing", "sd_easting", "gpstime", "sd_energy", "id"]].dropna()

event_id = data["id"]
data["year"] = event_id // (10**10) + 2000

# 2004:
#data = data[data["year"] == 2004]

# 2004, 2005:
#data = data[data["year"] < 2006]

# 2004, 2005, 2006:
data = data[data["year"] < 2007]



plt.figure(figsize=(7,7))
sns.scatterplot(x=data.sd_easting, y=data.sd_northing, size=8, alpha=0.5)
plt.xlabel('UTM Easting [m]')   
plt.ylabel('UTM Northing [m]')

LL= [6071871.5, 459208.3, 1416.2] # Norhing  Easting Altitude
LM= [6094570.2, 498903.7, 1416.4]
LA= [6134058.4, 480743.1, 1476.7]
CO= [6114140.0, 445343.8, 1712.3]

plt.scatter(LL[1], LL[0], marker='^', s=500, label='LL')
plt.scatter(LM[1], LM[0], marker='^', s=500, label='LM')
plt.scatter(LA[1], LA[0], marker='^', s=500, label='LA')
plt.scatter(CO[1], CO[0], marker='^', s=500, label='CO')
plt.annotate('Los Leones', xy=(LL[1]+4000, LL[0]-2000))
plt.annotate('Los Morados', xy=(LM[1]-4000, LM[0]-5000))
plt.annotate('Loma Amarilla', xy=(LA[1]-16000, LA[0]))
plt.annotate('Coihueco', xy=(CO[1]-4000, CO[0]+5000))

plt.title("2004, 2005, 2006", size=17)

plt.show()



