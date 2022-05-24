import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
import os


base_dir = "/Users/filipneubauer/Desktop/Python/auger/data/"

id_list = []

for file in os.listdir(base_dir):
    f = open(base_dir + file)
    data = json.load(f)
    f.close()
    try:
        for stat in data["sdrec"]["recstations"]:
            id_list.append(stat)
    except:
        pass        # fdrec

unique_bins = len(set(id_list))
print("Unique stations: ", unique_bins)

counts = pd.Series(id_list).value_counts()
print(counts.head(10))

plt.figure(figsize=(12, 7))
plt.hist(id_list, bins=1900)
plt.xlabel("Station id", fontsize=17)
plt.ylabel("Occurrence of events", fontsize=17)

plt.show()