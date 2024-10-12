import yfinance as yf
import pandas as pd
#from lightweight_charts import Chart
from lightweight_charts.widgets import StreamlitChart

pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display


# Example: Downloading EUR/USD data
forex_data = yf.download('EURUSD=X', start='2023-01-01', end='2023-12-31', interval= '1h')
df = forex_data

chart = StreamlitChart(width=900, height=600, toolbox= True)
chart.set(df)

chart.load()

"""
if __name__ == '__main__':
    chart = Chart(toolbox= True)

    # Columns: time | open | high | low | close | volume

    chart.set(df)

    chart.show(block=True)
"""