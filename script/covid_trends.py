import pandas as pd
import matplotlib.pyplot as plt

def load_data(path="data/covid_data.csv"):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def plot_country_trend(df, country):
    country_df = df[df['country'] == country]

    plt.figure()
    plt.plot(country_df['date'], country_df['confirmed'], label='Confirmed Cases')
    plt.plot(country_df['date'], country_df['deaths'], label='Deaths')
    plt.plot(country_df['date'], country_df['vaccinated'], label='Vaccinated')

    plt.title(f'COVID-19 Trend - {country}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()
    plot_country_trend(df, "Indonesia")