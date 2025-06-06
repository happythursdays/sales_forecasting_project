import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def forecast_sales(data, forecast_period=3):
    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Convert dates to ordinal (integer) for regression
    data['date_ordinal'] = data['Date'].apply(lambda date: date.toordinal())

    # Features (X) and target (y)
    X = data['date_ordinal'].values.reshape(-1, 1)
    y = data['Sales'].values

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Prepare future dates for forecasting (monthly steps)
    last_date = data['Date'].max()
    future_dates = [last_date + pd.DateOffset(months=i) for i in range(1, forecast_period + 1)]
    future_date_ordinal = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)

    # Forecast sales for future dates
    forecast = model.predict(future_date_ordinal)

    # Create dataframe for forecast results
    forecast_df = pd.DataFrame({
        'Date': future_dates,
        'Sales': forecast
    })

    # Combine original data with forecasted data
    combined_data = pd.concat([data[['Date', 'Sales']], forecast_df], ignore_index=True)

    # Evaluate model on training data
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    metrics = {'MSE': mse, 'R2': r2}

    return combined_data, metrics
