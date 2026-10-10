import pandas as pd
import numpy as np

np.random.seed(42)

student_ids = [f"S{i:03d}" for i in range(1, 51)]

completion_rate = np.random.randint(40, 101, 50)

avg_submission_time = np.round(
    np.random.uniform(1, 7, 50), 1
)

quiz_score = np.random.randint(40, 101, 50)

data = {
    "Student_ID": student_ids,
    "Completion_Rate": completion_rate,
    "Avg_Submission_Time": avg_submission_time,
    "Quiz_Score": quiz_score
}

df = pd.DataFrame(data)

print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

features = [
    "Completion_Rate",
    "Avg_Submission_Time",
    "Quiz_Score"
]

X = df[features]

print("\nFeatures used for clustering:")
print(X.head())

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Features:")
print(X_scaled[:5])

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

inertia_values = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia_values.append(kmeans.inertia_)

print("\nInertia Values:")
print(inertia_values)

plt.plot(range(1, 11), inertia_values, marker="o")

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Choosing K")

plt.show()

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nStudent Clusters:")
print(df[["Student_ID", "Completion_Rate",
          "Avg_Submission_Time", "Quiz_Score", "Cluster"]])

labels = kmeans.labels_
print(labels)

df["Cluster"] = labels

print(df)

cluster_summary = df.groupby("Cluster").mean(numeric_only=True)

print(cluster_summary)

for cluster in cluster_summary.index:
    print(f"\nCluster {cluster}")
    print(cluster_summary.loc[cluster])

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Completion_Rate"],
    df["Quiz_Score"],
    c=df["Cluster"],
    s=100
)

plt.xlabel("Completion Rate")
plt.ylabel("Quiz Score")
plt.title("Student Performance Clusters")
plt.show()

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Completion_Rate"],
    df["Quiz_Score"],
    c=df["Cluster"],
    s=100
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 2],
    s=300,
    marker="X"
)

plt.xlabel("Completion Rate")
plt.ylabel("Quiz Score")
plt.title("Student Performance Clusters with Centroids")
plt.show()

df.to_csv("student_clusters.csv", index=False)

print("Clustered data saved successfully!")

print("\nFinal Clustered Data:")
print(df)