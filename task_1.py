import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from CSV file
df = pd.read_csv("C:/Users/akash/OneDrive/Documents/dsa laksh/Internship/Sales_Dataset.csv") #add ur required filepath

# Display first few rows
print(df.head())

# Convert 'Order Date' to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract year and month
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Aggregate monthly sales
monthly_sales = df.groupby(["Year", "Month"])['Amount'].sum().reset_index()

# Plot sales trends
def plot_sales_trends():
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x="Month", y="Amount", hue="Year", marker="o")
    plt.title("Monthly Sales Trend Over Years", fontsize=14)
    plt.xlabel("Month", fontsize=11)
    plt.ylabel("Total Sales Amount", fontsize=11)
    plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.legend(title="Year")
    plt.grid(True)
    plt.show()
plot_sales_trends()

# Seasonal effects
seasonal_sales = df.groupby("Month")["Amount"].mean().reset_index()

def plot_seasonal_effects():
    plt.figure(figsize=(12, 6))
    sns.barplot(data=seasonal_sales, x="Month", y="Amount",hue="Month",palette="coolwarm",legend=False)
    plt.title("Average Monthly Sales (Seasonal Effect)", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Average Sales Amount", fontsize=12)
    plt.xticks(range(0, 12), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.grid(axis="y")
    plt.show()

plot_seasonal_effects()

# Category-wise sales and profit
category_performance = df.groupby("Category")[['Amount', 'Profit']].sum().reset_index()

def plot_category_performance():
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    sns.barplot(data=category_performance, x="Category", y="Amount", ax=ax[0],hue="Category", palette="Blues",legend=False)
    ax[0].set_title("Total Sales by Category", fontsize=14)
    ax[0].set_xlabel("Category", fontsize=12)
    ax[0].set_ylabel("Total Sales Amount", fontsize=12)
    ax[0].grid(axis="y")
    sns.barplot(data=category_performance, x="Category", y="Profit", ax=ax[1], palette="Greens",hue="Category",legend=False)
    ax[1].set_title("Total Profit by Category", fontsize=14)
    ax[1].set_xlabel("Category", fontsize=12)
    ax[1].set_ylabel("Total Profit", fontsize=12)
    ax[1].grid(axis="y")
    plt.tight_layout()
    plt.show()
plot_category_performance()

# Sub-category performance
subcategory_performance = df.groupby("Sub-Category")[['Amount', 'Profit']].sum().reset_index()
subcategory_performance = subcategory_performance.sort_values(by="Profit", ascending=False)

def plot_subcategory_performance():
    plt.figure(figsize=(14, 6))
    sns.barplot(data=subcategory_performance, x="Profit", y="Sub-Category",hue="Sub-Category",legend=False, palette="magma")
    plt.title("Profit by Sub-Category", fontsize=14)
    plt.xlabel("Total Profit", fontsize=12)
    plt.ylabel("Sub-Category", fontsize=12)
    plt.grid(axis="x")
    plt.show()
plot_subcategory_performance()
