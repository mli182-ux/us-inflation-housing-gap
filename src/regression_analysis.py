import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

DATA_PATH = "data/processed/annual_panel.csv"
OUT_PATH = "report/regression_summary.txt"

def main():
    df = pd.read_csv(DATA_PATH)

    # Model 1: Does housing affordability gap increase over time?
    gap_df = df.dropna(subset=["home_value_to_income"]).copy()
    gap_df["log_home_value_to_income"] = np.log(gap_df["home_value_to_income"])
    gap_df["year_centered"] = gap_df["year"] - gap_df["year"].min()

    model1 = smf.ols(
        "log_home_value_to_income ~ year_centered",
        data=gap_df
    ).fit()

    # Model 2: Does home value growth differ from inflation and income growth?
    growth_df = df.dropna(subset=[
        "zhvi_home_value_yoy",
        "cpi_all_yoy",
        "median_income_nominal_yoy"
    ]).copy()

    growth_df["post2020"] = (growth_df["year"] >= 2020).astype(int)

    model2 = smf.ols(
        "zhvi_home_value_yoy ~ cpi_all_yoy + median_income_nominal_yoy + post2020",
        data=growth_df
    ).fit()

    with open(OUT_PATH, "w") as f:
        f.write("Regression Analysis Summary\n")
        f.write("===========================\n\n")

        f.write("Model 1: Housing affordability gap over time\n")
        f.write("Dependent variable: log(home value / median household income)\n\n")
        f.write(str(model1.summary()))
        f.write("\n\n")

        f.write("Model 2: Home value growth vs inflation and income growth\n")
        f.write("Dependent variable: Zillow Home Value YoY growth\n\n")
        f.write(str(model2.summary()))
        f.write("\n\n")

        f.write("Interpretation notes:\n")
        f.write("- Model 1 tests whether the home value-to-income ratio increased over time.\n")
        f.write("- Model 2 compares home value growth with general inflation and income growth.\n")
        f.write("- These regressions are descriptive, not causal.\n")

    print(f"Saved {OUT_PATH}")
    print(model1.summary())
    print(model2.summary())

if __name__ == "__main__":
    main()