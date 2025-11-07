# model.py
from sklearn.cluster import KMeans

def perform_clustering(df, n_clusters=3):
    features = df[["Annual_Income(k$)", "Spending_Score(1-100)"]]
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["Cluster"] = kmeans.fit_predict(features)
    return df, kmeans
