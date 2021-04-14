import pandas as pd
import pathlib

all_provinces = ['bangkok','chanthaburi','chiangmai','kanchanaburi','khonkaen','songkhla']

df = pd.DataFrame(columns=['datetime','Temp(C)','lat','long','WindDir','Wind Speed(km/h)','PM2.5'])

for it in all_provinces :
    t_df = pd.read_csv(str(pathlib.Path(__file__).parent.parent)+'/data/train/'+it+'.csv')
    df = df.append(t_df)

df = df.sort_values('datetime')
df.to_csv(str(pathlib.Path(__file__).parent.parent)+'/data/train/all_provinces.csv', index=False)