# Customer Segmentation using K-Means Clustering

## Project Overview

This project focuses on customer segmentation using the **K-Means Clustering** algorithm. It utilizes customer data such as age, annual income, and spending scores to group customers into distinct clusters. This segmentation helps businesses understand customer behaviors and tailor their marketing strategies accordingly.

---

## Dataset

The dataset used for this project is `Mall_Customers.csv`, which contains the following columns:

- **CustomerID**: Unique identifier for each customer
- **Gender**: Gender of the customer
- **Age**: Age of the customer
- **Annual Income (k$)**: Annual income of the customer in thousands of dollars
- **Spending Score (1-100)**: Score assigned based on customer spending patterns

---

## Project Workflow

### 1. Data Preprocessing

- **Handling Missing Values**: Filled missing numeric values with the column mean.
- **Encoding Categorical Variables**: Encoded the `Gender` column using `LabelEncoder`.
- **Feature Scaling**: Standardized the `Age`, `Annual Income`, and `Spending Score` columns using `StandardScaler`.

### 2. Optimal Number of Clusters

- Used the **Elbow Method** to determine the optimal number of clusters.
- Plotted the inertia values for cluster counts ranging from 1 to 10.

### 3. K-Means Clustering

- Trained the K-Means model with the optimal number of clusters.
- Assigned each data point to a cluster for both train and test datasets.

### 4. Evaluation Metrics

- **Silhouette Score**: Measures how similar an object is to its own cluster compared to other clusters.
- **Davies-Bouldin Index**: Measures the average similarity ratio of each cluster with the cluster that is most similar to it.
- **Inertia**: Measures how well the data points are clustered.

### 5. Visualizations

- **Elbow Plot**: Visualized the inertia to determine the optimal number of clusters.
- **Cluster Heatmap**: Displayed average values of features for each cluster.
- **Scatter Plot**: Showed customer distribution across clusters based on `Annual Income` and `Spending Score`.

---

## Results

- **Optimal Clusters**: Determined using the Elbow Method.
- **Cluster Insights**: Displayed feature averages for each cluster to understand customer profiles.
- **Evaluation Metrics**:
  - Train Silhouette Score: *e.g., 0.45*
  - Train Davies-Bouldin Index: *e.g., 0.78*
  - Test Silhouette Score: *e.g., 0.43*
  - Test Davies-Bouldin Index: *e.g., 0.81*

---

## Dependencies

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

