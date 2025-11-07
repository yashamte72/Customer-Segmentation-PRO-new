# app.py
import streamlit as st
from data_generator import generate_customer_data
from model import perform_clustering
from visualize import plot_clusters, plot_gender_distribution, plot_occupation_distribution

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

st.title("🧠 Customer Segmentation using K-Means")
st.markdown("This app generates realistic customer data (with Gender & Occupation) and segments them based on income and spending patterns.")

# Sidebar
st.sidebar.header("⚙️ Settings")
num_customers = st.sidebar.slider("Number of Customers", 15, 60, 20)
n_clusters = st.sidebar.slider("Number of Clusters (K)", 2, 6, 3)
seed = st.sidebar.number_input("Random Seed", 0, 999, 42)

# Generate data
st.subheader("📋 Generated Customer Data")
df = generate_customer_data(num_customers, seed)
st.dataframe(df, use_container_width=True)

# Perform clustering
st.subheader("🔍 K-Means Clustering Result")
clustered_df, model = perform_clustering(df, n_clusters)
st.dataframe(clustered_df, use_container_width=True)

# Visualization
st.subheader("📊 Cluster Visualization")
fig = plot_clusters(clustered_df)
st.plotly_chart(fig, use_container_width=True)

# Gender & Occupation Insights
col1, col2 = st.columns(2)
with col1:
    st.subheader("🚻 Gender Distribution")
    st.plotly_chart(plot_gender_distribution(clustered_df), use_container_width=True)
with col2:
    st.subheader("💼 Occupation Distribution")
    st.plotly_chart(plot_occupation_distribution(clustered_df), use_container_width=True)

# Cluster summary
st.subheader("📈 Cluster Summary")
summary = clustered_df.groupby("Cluster")[["Age", "Annual_Income(k$)", "Spending_Score(1-100)"]].mean()
st.dataframe(summary.style.format("{:.1f}"))

# Download button
csv = clustered_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Clustered Data as CSV", data=csv, file_name="customer_segments.csv", mime="text/csv")

# app.py (add after imports)
st.markdown("""
    <style>
    /* Global background */
    body {
        background-color: #0A192F;
        color: #FFFFFF;
    }

    /* Title */
    h1 {
        color: #00B4D8;
        text-align: center;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #112240;
    }

    /* Dataframe styling */
    .stDataFrame {
        border: 1px solid #00B4D8;
        border-radius: 8px;
    }

    /* Download button */
    .stDownloadButton button {
        background-color: #00B4D8;
        color: white;
        border-radius: 10px;
        border: none;
    }
    .stDownloadButton button:hover {
        background-color: #0077B6;
    }

    /* Metric labels */
    .css-1xarl3l, .css-10trblm {
        color: #00B4D8;
    }
    </style>
""", unsafe_allow_html=True)
