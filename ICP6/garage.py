import matplotlib.pyplot as plt
import pandas as pd
train=pd.read_csv('train.csv')
plt.style.use('seaborn-whitegrid')
plt.plot(train['GarageArea'],train['SalePrice'],'o')
plt.show()

#train['GarageArea'].replace(to_replace=train.loc[train['GarageArea'] >1050],value=train['GarageArea'].mean)
train=train.where(train['GarageArea']<1050,train['GarageArea'].mean())
plt.plot(train['GarageArea'],train['SalePrice'],'o')
plt.show()
