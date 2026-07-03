import matplotlib.pyplot as plt
import seaborn as sns

def plot_prices(df):
    plt.figure(figsize=(8,5))
    plt.bar(df["route"], df["price"])
    plt.xticks(rotation=45)
    plt.title("Flight Prices by Route")
    plt.ylabel("Price (INR)")
    plt.show()

def plot_correlation(df):
    df_numeric = df.select_dtypes(include=["number"])
    plt.figure(figsize=(6,4))
    sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()
