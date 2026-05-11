import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("expenses.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Category Analysis
category_total = df.groupby("Category")["Amount"].sum()

# Monthly Analysis
df["Month"] = df["Date"].dt.month_name()
monthly_total = df.groupby("Month")["Amount"].sum()

# Payment Method Analysis
payment_total = df.groupby("Payment_Method")["Amount"].sum()

# Highest Spending Category
highest_category = category_total.idxmax()

# Average Daily Spending
daily_spending = df.groupby("Date")["Amount"].sum()
average_daily = daily_spending.mean()

# Total Spending
total_spending = df["Amount"].sum()

# Print Results
print("Category-wise Spending")
print(category_total)

print("\nMonthly Spending")
print(monthly_total)

print("\nPayment Method Analysis")
print(payment_total)

print("\nHighest Spending Category:", highest_category)
print("Average Daily Spending:", average_daily)
print("Total Spending:", total_spending)

# Bar Chart
category_total.plot(kind="bar")
plt.title("Category-wise Spending")
plt.savefig("charts.png")
plt.show()

# Report Generation
report = pd.DataFrame({
    "Metric": [
        "Highest Spending Category",
        "Average Daily Spending",
        "Total Spending"
    ],
    "Value": [
        highest_category,
        average_daily,
        total_spending
    ]
})

report.to_csv("expense_report.csv", index=False)

print("\nReport Generated Successfully")
