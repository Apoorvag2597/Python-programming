import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
data = pd.read_csv("College.csv")
X_data = data.iloc[:,2:]
print(X_data.columns)
nclusters=3
seed=7
km=KMeans(n_clusters=nclusters,random_state=seed)
km.fit(X_data)
y_cluster_kmeans=km.predict(X_data)
print(y_cluster_kmeans)
wcss_data=[]
for i in range(1,5):
    kmeans_data = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10)
    y_means_data = kmeans_data.fit(X_data)
    wcss_data.append(y_means_data.inertia_)
print()
plt.plot(range(1,5),wcss_data)
plt.show()
