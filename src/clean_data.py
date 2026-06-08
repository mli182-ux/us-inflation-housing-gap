import pandas as pd

RAW_PATH = "data/raw/fred_core_data.csv"
OUT_PATH = "data/processed/annual_panel.csv"

def main():
    df = pd.read_csv(RAW_PATH, parse_dates=["DATE"])
    df = df.set_index("DATE")

    # Convert monthly series to annual averages.
    annual = df.resample("YE").mean()
    annual["year"] = annual.index.year

    # Normalize selected variables to 2000 = 100.
    base_year = 2000
    cols_to_index = [
        "cpi_all",
        "cpi_shelter",
        "cpi_rent",
        "cpi_oer",
        "zhvi_home_value",
        "median_income_nominal",
        "median_income_real",
    ]

    for col in cols_to_index:
        base_value = annual.loc[annual["year"] == base_year, col].iloc[0]
        annual[col + "_index_2000"] = annual[col] / base_value * 100

    # Year-over-year growth rates.
    growth_cols = [
        "cpi_all",
        "cpi_shelter",
        "cpi_rent",
        "zhvi_home_value",
        "median_income_nominal",
    ]

    for col in growth_cols:
        annual[col + "_yoy"] = annual[col].pct_change() * 100

    # Main affordability metric.
    annual["home_value_to_income"] = (
        annual["zhvi_home_value"] / annual["median_income_nominal"]
    )

    annual.to_csv(OUT_PATH, index=False)
    print(f"Saved {OUT_PATH}")
    print(annual.tail())

if __name__ == "__main__":
    main()
