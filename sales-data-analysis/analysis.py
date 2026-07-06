import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

sales_summary = df.groupby("Product")["Sales"].sum()

print(sales_summary)

sales_summary.plot(kind="bar")

plt.title("Sales by Product")

plt.savefig("sales_chart.png")

plt.show()