# visualize.py

import matplotlib.pyplot as plt

def plot_sales_and_forecast(df, df_forecast):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Sales"], label="Actual Sales", marker='o')
    plt.plot(df_forecast["Date"], df_forecast["Sales"], label="Forecasted Sales", linestyle='--', marker='x')
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Sales Forecast")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
