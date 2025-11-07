# data_generator.py
import pandas as pd
import numpy as np

def generate_customer_data(num_customers=20, seed=42):
    np.random.seed(seed)

    # Gender and Occupation categories
    genders = np.random.choice(["Male", "Female"], size=num_customers)
    occupations = np.random.choice(
        ["Student", "Engineer", "Doctor", "Teacher", "Business", "Artist", "Manager"],
        size=num_customers
    )

    # Define customer groups (Budget, Regular, Premium)
    num_budget = num_customers // 3
    num_regular = num_customers // 3
    num_premium = num_customers - (num_budget + num_regular)

    # Budget group: low income & spending
    budget = {
        "Age": np.random.randint(18, 40, num_budget),
        "Annual_Income(k$)": np.random.normal(30, 5, num_budget).astype(int),
        "Spending_Score(1-100)": np.random.normal(35, 10, num_budget).astype(int),
    }

    # Regular group: mid income & spending
    regular = {
        "Age": np.random.randint(25, 50, num_regular),
        "Annual_Income(k$)": np.random.normal(60, 10, num_regular).astype(int),
        "Spending_Score(1-100)": np.random.normal(60, 10, num_regular).astype(int),
    }

    # Premium group: high income & spending
    premium = {
        "Age": np.random.randint(30, 55, num_premium),
        "Annual_Income(k$)": np.random.normal(100, 10, num_premium).astype(int),
        "Spending_Score(1-100)": np.random.normal(85, 10, num_premium).astype(int),
    }

    # Combine all groups
    data = {
        "Age": np.concatenate([budget["Age"], regular["Age"], premium["Age"]]),
        "Annual_Income(k$)": np.concatenate([budget["Annual_Income(k$)"], regular["Annual_Income(k$)"], premium["Annual_Income(k$)"]]),
        "Spending_Score(1-100)": np.concatenate([budget["Spending_Score(1-100)"], regular["Spending_Score(1-100)"], premium["Spending_Score(1-100)"]]),
    }

    df = pd.DataFrame(data)
    df["CustomerID"] = range(1, num_customers + 1)
    df["Gender"] = genders
    df["Occupation"] = occupations

    # Reorder columns for readability
    df = df[["CustomerID", "Gender", "Occupation", "Age", "Annual_Income(k$)", "Spending_Score(1-100)"]]

    # Keep spending score within bounds
    df["Spending_Score(1-100)"] = df["Spending_Score(1-100)"].clip(1, 100)

    return df
