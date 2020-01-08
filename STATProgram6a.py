import pylab as pl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# creating data frame from csv
df = pd.read_csv("ss13hil.csv", na_values="..")

fig=plt.figure(figsize=(18, 12))
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

frequencyHHL = df["HHL"].value_counts()

ax1.pie(frequencyHHL, startangle=-118.03474)
ax1.legend(["English Only", "Spanish", 'Other Indo-Europian', "Asian and Pacific Island languages", "Other Languages"], loc=2, prop={'size': 5})
ax1.set_aspect('equal')
ax1.set_title("Household Languages")

ax2.hist(df['HINCP'].dropna(), bins=np.logspace(1, 7, 100), density=True, linestyle=('solid'), color= ('white'), histtype='bar', fill=False)
ax2.set_xscale('log')
ax2.set_xlim([10,10**7])
df['HINCP'].dropna().plot(kind='density', linestyle='--', ax = ax2)
ax2.set_title("Distribution of Household Income")
ax2.set_xlabel("Household Income ($) - Log Scaled")


x = []
y = []
for veh in df['VEH'].drop_duplicates():
    x.append(veh)
    y.append(df["WGTP"][df['VEH'] == veh].sum() / 1000.)

ax3.set_yticks(range(0,2000,200))
ax3.bar(x,y)
ax3.set_title("Vehicles available in Households")
ax3.set_xlabel("# of Vehicles")
ax3.set_ylabel("Thousands of Households")

def convert(val):
    if(val==1):
        return 0
    if(val==2):
        return 1

    if(val<=22):
        return ((50*val)-100)

    if(val<=62):
        return((100*val)-1200)

    if(val<65):
        return((500*val)-26000)

    else:
        return((1000*val)-58000)


shortDf = df[['TAXP', 'VALP', 'WGTP', 'MRGP']].dropna()
shortDf.loc[:, "TAXP"] = shortDf['TAXP'].apply(convert)
cm = plt.cm.get_cmap('RdYlBu')
sc = ax4.scatter(x=shortDf['VALP'], y=shortDf['TAXP'], c=shortDf['MRGP'],
                 s=shortDf["WGTP"]/5., vmin=0, vmax=5000, cmap=cm, marker='o', alpha=0.3)
ax4.set_xticks(range(0,1400000,200000))
ax4.set_xlim([0,1200000])
cbar = plt.colorbar(sc, ax=ax4)

cbar.set_label("First Mortgage Payment (Monthly $)")
ax4.set_title("Property Taxes vs Property Values")
ax4.set_xlabel("Property Value ($)")
ax4.set_ylabel("Taxes ($)")

plt.savefig("pums.png")
plt.show()

