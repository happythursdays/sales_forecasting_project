import pandas as pd
import matplotlib.pyplot as plt
from forecast_model import forecast_sales

def main():
    # Load data | Do ensure that your CSV path is correct
    data = pd.read_csv('data/sales_data.csv')

    forecast_period = 3  # forecast next 3 months

    # Get combined data and metrics from forecasting function
    combined_data, metrics = forecast_sales(data, forecast_period)

    # Print metrics
    print("Model Performance:")
    print(f"Mean Squared Error: {metrics['MSE']:.2f}")
    print(f"R-squared: {metrics['R2']:.2f}")

    # Plot original + forecasted sales
    plt.figure(figsize=(10,6))
    plt.plot(combined_data['Date'], combined_data['Sales'], marker='o', label='Historical + Forecast')
    plt.axvline(x=data['Date'].max(), color='red', linestyle='--', label='Forecast Start')
    plt.title('Sales Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
