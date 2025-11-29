import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Read data from file
df = pd.read_csv("epa-sea-level.csv")


def draw_plot():
    """Creates a scatter plot with two lines of best fit predicting sea level rise.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The resulting matplotlib figure.
    """

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit using all data
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(1880, 2051))
    sea_level_all = res_all.slope * years_all + res_all.intercept
    ax.plot(years_all, sea_level_all, "r", label="Best fit line (1880-2050)")

    # Line of best fit using data from year 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = res_recent.slope * years_recent + res_recent.intercept
    ax.plot(years_recent, sea_level_recent, "g", label="Best fit line (2000-2050)")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    ax.legend()

    # Save plot
    fig.savefig("sea_level_plot.png")

    return fig
