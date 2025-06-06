# Sales Forecasting Project

A simple Python-based project that demonstrates how to forecast monthly sales using basic machine learning. Built with a traditional coding structure and minimalistic logic for clarity and learning purposes.

## Project Overview

This project uses **linear regression** to forecast future monthly sales based on a provided CSV dataset (`sales_data.csv`). It’s designed to showcase:

- Reading and processing data with `pandas`
- Building and training a linear model with `scikit-learn`
- Generating future predictions
- Displaying results with matplotlib

> ✅ Designed in a way that’s easy to follow and modify — especially for learners or aspiring data analysts.

---

## Project Structure


```text
sales_forecasting_project/
│
├── data/
│   └── sales_data.csv         # Sample input data (Date, Sales)
│
├── main.py                    # Main driver program
├── forecast_model.py          # Forecast logic and metrics calculation
├── plot.py                    # Handles plotting actual vs predicted sales
└── README.md                  # This file
```

---

## How to Run

1. Open the project in PyCharm.
2. Make sure the virtual environment is activated.
3. Install dependencies (if not done yet):

```bash
pip install pandas matplotlib scikit-learn
```
4. Run main.py and follow the prompt to enter how many months to forecast.

---

## Output Example
- Forecast for future months (based on input)
- Combined plot of actual vs predicted sales
- Simple model metrics: MAE, MSE, RMSE

---

## What I Learned
- Structuring Python projects with multiple modules
- Implementing basic machine learning logic manually
- Visualizing results with simple plotting
- Keeping code readable and logical (my own style preference)

---

## Tools Used
- Program Language: Python
    - pandas
    - scikit-learn
    - matplotlib
- PyCharm IDE

---

## Author Notes
This project was built using my preferred coding style — concise variables, clean structure, and traditional logic without shortcuts — to ensure it’s easy to understand and extend.

Feel free to fork, modify, or use it as a base for your own forecasting experiments.

**Future Improvements or Suggestions:**
- **Support multiple forecasting models**  
  Add options to switch between models like ARIMA, Prophet, or Random Forest for more accurate results on different types of data.

- **Advanced visualizations**  
  Include confidence intervals, seasonal trends, or interactive charts using Plotly or Dash.

- **User input or GUI support**  
  Build a simple Tkinter or web interface where users can upload their own CSV and get forecasts visually.

- **Export forecast results**  
  Allow exporting predictions and metrics as Excel or CSV reports for business sharing.

- **Monthly/Weekly/Yearly forecast toggle**  
  Let users choose the forecasting granularity depending on their sales cycles.

- **Unit testing**  
  Add test coverage using `unittest` or `pytest` to ensure accuracy and stability.

- **Deploy as a web app**  
  Host the model on a cloud service (e.g., Streamlit Cloud, Flask on Heroku, or FastAPI) for public access.


---

## About Me
    Jamie Nicole Benwick
    Aspiring data scientist | Software enthusiast
    📍 Las Piñas, Metro Manila
    📫 jamienicolevillelabenwick@gmail.com

