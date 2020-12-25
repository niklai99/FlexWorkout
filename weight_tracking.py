import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


def get_data():
    date = dt.datetime.today()
    weight = input('Inserisci il peso di oggi\n')
    return date, weight

def make_df(date, weight):
    today = format(date.day, '.0f') + ' - ' + format(date.month, '.0f') + ' - ' + format(date.year, '.0f')
    df = pd.DataFrame(data = [weight], index = [today])
    return df

def main():
    date, weight = get_data()
    df = make_df(date, weight)
    df.to_csv('./weight_data.csv', mode='a')


if __name__ == "__main__":
    main()