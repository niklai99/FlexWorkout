import pandas as pd
import datetime as dt


def get_data():
    date = dt.date.today()
    weight = input('Inserisci il peso di oggi\n')
    return date, weight

def make_df(date, weight):
    df = pd.DataFrame(data = [[date, weight]])
    return df


def main():
    date, weight = get_data()
    df = make_df(date, weight)
    df.to_csv('./weight_data.csv', mode='a', index=False, header=False)


if __name__ == "__main__":
    main()