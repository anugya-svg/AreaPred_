import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

df=pd.read_excel('project_dataset.xlsx')
df.rename(columns={'Residence.Level':'Resi','Is.Bar':'Bar','Is.Police_Station':'Police','People.Frequency':'People'},inplace=True)
df.Time[df.Time=='Morning']=0
df.Time[df.Time=='Afternoon']=1
df.Time[df.Time=='Evening']=2
df.Time[df.Time=='Night']=3
df.Class[df.Class=='Safe']=0
df.Class[df.Class=='Unsafe']=1
df.People[df.People=='Low']=0
df.People[df.People=='Medium']=1
df.People[df.People=='High']=2
df.Police[df.Police=='Yes']=0
df.Police[df.Police=='No']=1
df.Resi[df.Resi=='Low']=0
df.Resi[df.Resi=='Medium']=1
df.Resi[df.Resi=='High']=2
df.Tier[df.Tier=='Inner']=0
df.Tier[df.Tier=='Middle']=1
df.Tier[df.Tier=='Outer']=2
df.Bar[df.Bar=='Yes']=0
df.Bar[df.Bar=='No']=1
regressor=LogisticRegression()
df = df.replace(np.nan, 0)
lst=df[[ 'Time', 'People', 'Police','Bar', 'Tier', 'Resi']]
l=np.array(lst)
t=np.array(df['Class'])
y = list(t)
regressor.fit(l,y)
pickle.dump(regressor,open('model.pkl','wb'))

