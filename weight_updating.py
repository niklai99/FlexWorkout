import pandas as pd
import datetime as dt


def get_data():
    date = dt.date.today()
    training = input('\nHai fatto allenamento oggi? ( y / n )\n')
    weight = input('\nInserisci il peso di oggi\n')
    return date, weight, training

def make_df(date, weight, training):
    df = pd.DataFrame(data = [[date, weight, training]])
    return df


def main():
    date, weight, training = get_data()
    df = make_df(date, weight, training)
    df.to_csv('D:\\GitHub\\FlexWorkout\\weight_data.csv', mode='a', index=False, header=False)


if __name__ == "__main__":
    main()