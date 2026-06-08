import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "data/processed/annual_panel.csv"

def save_line_plot(df, columns, labels, title, ylabel, filename):
    plt.figure(figsize=(10, 6))

    for col, label in zip(columns, labels):
        plt.plot(df["year"], df[col], marker="o", linewidth=2, label=label)

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"Saved {filename}")

def main():
    df = pd.read_csv(DATA_PATH)

    # Figure 1: Normalized indices, 2000 = 100
    save_line_plot(
        df,
        [
            "cpi_all_index_2000",
            "cpi_shelter_index_2000",
            "cpi_rent_index_2000",
            "zhvi_home_value_index_2000",
            "median_income_nominal_index_2000",
        ],
        [
            "Overall CPI",
            "Shelter CPI",
            "Rent CPI",
            "Zillow Home Value Index",
            "Median Household Income",
        ],
        "Inflation, Housing Costs, and Income Growth, 2000–2024",
        "Index, 2000 = 100",
        "figures/fig1_normalized_trends.png",
    )

    # Figure 2: Home value to income ratio
    save_line_plot(
        df,
        ["home_value_to_income"],
        ["Home value / median income"],
        "U.S. Home Value-to-Income Ratio, 2000–2024",
        "Ratio",
        "figures/fig2_home_value_to_income.png",
    )

    # Figure 3: Year-over-year growth
    save_line_plot(
        df.dropna(subset=["cpi_all_yoy", "cpi_shelter_yoy", "zhvi_home_value_yoy", "median_income_nominal_yoy"]),
        [
            "cpi_all_yoy",
            "cpi_shelter_yoy",
            "zhvi_home_value_yoy",
            "median_income_nominal_yoy",
        ],
        [
            "Overall CPI YoY",
            "Shelter CPI YoY",
            "Home Value YoY",
            "Income YoY",
        ],
        "Year-over-Year Growth: Inflation, Housing, and Income",
        "Annual growth rate (%)",
        "figures/fig3_yoy_growth.png",
    )

if __name__ == "__main__":
    main()
