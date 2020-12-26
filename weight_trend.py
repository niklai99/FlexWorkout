import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.ticker import MaxNLocator
import matplotlib

def read_data():
    '''Read data from the csv file '''

    df = pd.read_csv('D:\\GitHub\\FlexWorkout\\weight_data.csv', parse_dates=['Date'], index_col = ['Date'])

    return df

def split_data(df):
    df_y = df[df['Training'].str.contains('y')]
    df_n = df[df['Training'].str.contains('n')]
    return df_y, df_n

def compute_diff(df):
    df['Diff'] = df['Weight'].diff()
    print(df['Diff'])

def line_plot_settings(ax):

    ax.tick_params(axis = 'x', which = 'major', labelsize = 12, direction = 'out', length = 7, rotation = 15)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 12, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 12, direction = 'out', length = 3)
    ax.tick_params(axis = 'x', which = 'minor', bottom = False)
    ax.set_yticks(ticks = ax.get_yticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Date', fontsize = 15, loc = 'center')
    ax.set_ylabel('Weight (kg)', fontsize = 15, loc = 'center')
    ax.set_title('Weight trend', fontsize = 18)

def diff_plot_settings(ax):
    ax.tick_params(axis = 'x', which = 'major', labelsize = 12, direction = 'out', length = 7, rotation = 15)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 12, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 12, direction = 'out', length = 3)
    ax.tick_params(axis = 'x', which = 'minor', bottom = False)
    ax.set_yticks(ticks = ax.get_yticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Date', fontsize = 15, loc = 'center')
    ax.set_ylabel('Weight (kg)', fontsize = 15, loc = 'center')
    ax.set_title('Weight diff', fontsize = 18)

def hist_plot_settings(ax):

    ax.tick_params(axis = 'x', which = 'major', labelsize = 12, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 12, direction = 'out', length = 7)
    ax.tick_params(axis = 'x', which = 'minor', labelsize = 12, direction = 'out', length = 3)
    ax.tick_params(axis = 'y', which = 'minor', left = False)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(ticks = ax.get_xticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Weight (kg)', fontsize = 15, loc = 'center')
    ax.set_ylabel('Counts', fontsize = 15, loc = 'center')
    ax.set_title('Weight distribution', fontsize = 18)

def make_plot(df):
    '''Make the plot'''

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

    ax1.grid(axis='y', linewidth = .3)
    ax2.grid(axis='y', linewidth = .3)

    compute_diff(df)
    df_y, df_n = split_data(df)

    sns.lineplot(x = 'Date', y = 'Weight', data = df, dashes = False, ax = ax1, color = 'b', zorder = 1, label='trend')
    sns.lineplot(x = 'Date', y = 'Weight', data = df_y, marker="o", dashes = False, ax = ax1, linewidth = 0, color = 'g', zorder = 2, label='train')
    sns.lineplot(x = 'Date', y = 'Weight', data = df_n, marker="o", dashes = False, ax = ax1, linewidth = 0, color = 'r', zorder = 3, label='no train')
    ax1.legend(loc = 'best')
    line_plot_settings(ax1)
    date_form = DateFormatter("%d %b")
    ax1.xaxis.set_major_formatter(date_form)
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

    sns.lineplot(x = 'Date', y = 'Diff', data = df, dashes = False, ax = ax2, color = 'b', zorder = 1, label='trend')
    sns.lineplot(x = 'Date', y = 'Diff', data = df_y, marker="o", dashes = False, ax = ax2, linewidth = 0, color = 'g', zorder = 2, label='train')
    sns.lineplot(x = 'Date', y = 'Diff', data = df_n, marker="o", dashes = False, ax = ax2, linewidth = 0, color = 'r', zorder = 3, label='no train')
    ax1.legend(loc = 'best')
    diff_plot_settings(ax2)
    ax2.xaxis.set_major_formatter(date_form)
    ax2.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))


    sns.histplot(data = df, x = 'Weight', stat = 'count', element = 'bars', edgecolor = 'white', kde = True, ax = ax3)
    hist_plot_settings(ax3)


    plt.show()

def main():

    df = read_data()
    make_plot(df)
    sys.exit()

if __name__ == "__main__":
    main()