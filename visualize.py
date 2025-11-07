# visualize.py
import plotly.express as px

def plot_clusters(df):
    fig = px.scatter(
        df,
        x="Annual_Income(k$)",
        y="Spending_Score(1-100)",
        color=df["Cluster"].astype(str),
        hover_data=["CustomerID", "Age", "Gender", "Occupation"],
        title="Customer Segmentation (K-Means Clustering)",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig.update_traces(marker=dict(size=12, line=dict(width=1, color='DarkSlateGrey')))
    return fig


def plot_gender_distribution(df):
    fig = px.pie(df, names="Gender", title="Gender Distribution")
    return fig


def plot_occupation_distribution(df):
    fig = px.histogram(df, x="Occupation", color="Cluster",
                       title="Occupation Distribution by Cluster", barmode="group")
    return fig
