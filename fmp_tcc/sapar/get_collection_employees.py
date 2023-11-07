import pandas as pd

from .get_info import get_employees_number



def get_employees_counts(apikey: str='apikey', ticks: list=['AAPL', 'MSFT'], period: str = 'annual', 
           with_progress: bool = False):
    
    if with_progress:
        n = len(ticks)
        i=0

    employees = []

    for ticker in ticks:
        ticker_data = get_employees_number(apikey=apikey, symbol=ticker)
        employees.append(pd.DataFrame(ticker_data))
        if with_progress:
            print(f"For {ticker}: {i} / {n}")

    employees_df = pd.concat(employees, axis=0)

    return employees_df