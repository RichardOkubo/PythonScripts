"""Customer segmentation using K-Means clustering."""

import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns

from sklearn.cluster import KMeans

customer_data = pd.read_csv("./data/mall_customers.csv")

X = customer_data.iloc[:,[3,4]].values

#wcss = []
#
#for i in range(1,11):
#  kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
#  kmeans.fit(X)
#
#  wcss.append(kmeans.inertia_)
#
#sns.set()
#plt.plot(range(1,11), wcss)
#plt.title('The Elbow Point Graph')
#plt.xlabel('Number of Clusters')
#plt.ylabel('WCSS')
#plt.show()

kmeans = KMeans(n_clusters=5, init="k-means++", random_state=0)

Y = kmeans.fit_predict(X)

colors = ["green", "red", "yellow", "violet", "blue"]

plt.figure(figsize=(6, 6))

for i, color in enumerate(colors):
    plt.scatter(X[Y==i, 0], X[Y==i, 1], s=50, c=color, label=f"Cluster {i + 1}")

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c="cyan", label="Centroids")

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()
