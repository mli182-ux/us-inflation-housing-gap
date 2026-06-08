import pandas as pd
from pandas_datareader import data as pdr

START = "2000-01-01"
END = "2024-12-31"

SERIES = {
    "CPIAUCSL": "cpi_all",
    "CUSR0000SAH1": "cpi_shelter",
    "CUSR0000SEHA": "cpi_rent",
    "CUSR0000SEHC": "cpi_oer",
    "USAUCSFRCONDOSMSAMID": "zhvi_home_value",
    "MEHOINUSA646N": "median_income_nominal",
    "MEHOINUSA672N": "median_income_real",
}

def main():
    df = pdr.DataReader(list(SERIES.keys()), "fred", START, END)
    df = df.rename(columns=SERIES)
    df.to_csv("data/raw/fred_core_data.csv")
    print("Saved data/raw/fred_core_data.csv")
    print(df.tail())

if __name__ == "__main__":
    main()
