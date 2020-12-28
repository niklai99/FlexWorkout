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
    #df.at[2020-11-24, 'Diff'] = 0
    #print(df['Diff'])

def line_plot_settings(ax):

    ax.tick_params(axis = 'x', which = 'major', labelsize = 11, direction = 'out', length = 7, rotation = 15)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 11, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 11, direction = 'out', length = 3)
    ax.tick_params(axis = 'x', which = 'minor', bottom = False)
    ax.set_yticks(ticks = ax.get_yticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Date', fontsize = 0, loc = 'center')
    ax.set_ylabel('Weight (kg)', fontsize = 12, loc = 'center')
    #ax.set_title('Weight trend', fontsize = 18)

def diff_plot_settings(ax):
    ax.tick_params(axis = 'x', which = 'major', labelsize = 11, direction = 'out', length = 7, rotation = 15)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 11, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 11, direction = 'out', length = 3)
    ax.tick_params(axis = 'x', which = 'minor', bottom = False)
    ax.set_yticks(ticks = ax.get_yticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Date', fontsize = 0, loc = 'center')
    ax.set_ylabel('Weight difference (kg)', fontsize = 12, loc = 'center')
    #ax.set_title('Daily weight difference', fontsize = 18)

def hist_plot_settings(ax):

    ax.tick_params(axis = 'x', which = 'major', labelsize = 11, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 11, direction = 'out', length = 7)
    ax.tick_params(axis = 'x', which = 'minor', labelsize = 11, direction = 'out', length = 3)
    ax.tick_params(axis = 'y', which = 'minor', left = False)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(ticks = ax.get_xticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Weight (kg)', fontsize = 12, loc = 'center')
    ax.set_ylabel('Counts', fontsize = 12, loc = 'center')
    #ax.set_title('Weight distribution', fontsize = 18)

def hist_diff_settings(ax):

    ax.tick_params(axis = 'x', which = 'major', labelsize = 11, direction = 'out', length = 7)
    ax.tick_params(axis = 'y', which = 'major', labelsize = 11, direction = 'out', length = 7)
    ax.tick_params(axis = 'x', which = 'minor', labelsize = 11, direction = 'out', length = 3)
    ax.tick_params(axis = 'y', which = 'minor', left = False)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_xticks(ticks = ax.get_xticks(), minor = True)
    ax.minorticks_on()

    ax.set_xlabel('Weight difference (kg)', fontsize = 12, loc = 'center')
    ax.set_ylabel('Counts', fontsize = 12, loc = 'center')
    #ax.set_title('Diff weight distribution', fontsize = 18)

def make_plot(df):
    '''Make the plot'''

    fig1 = plt.figure()
    
    ax1 = plt.subplot2grid((11, 61), (0, 0), rowspan=5, colspan=40)
    ax2 = plt.subplot2grid((11, 61), (6, 0), rowspan=5, colspan=40)
    ax3 = plt.subplot2grid((11, 61), (0, 45), rowspan=5, colspan=16)
    ax4 = plt.subplot2grid((11, 61), (6, 45), rowspan=5, colspan=16)

    ax1.grid(axis='y', linewidth = .3)
    ax2.grid(axis='y', linewidth = .3)

    compute_diff(df)
    df_y, df_n = split_data(df)

    MAX = df['Weight'].max() + 0.5 
    MIN = df['Weight'].min() - 0.5 

    sns.lineplot(x = 'Date', y = 'Weight', data = df, dashes = False, ax = ax1, zorder = 1, label='Trend Line')
    sns.lineplot(x = 'Date', y = 'Weight', data = df_y, marker="o", dashes = False, ax = ax1, linewidth = 0, color = 'g', zorder = 2, label='Training')
    sns.lineplot(x = 'Date', y = 'Weight', data = df_n, marker="o", dashes = False, ax = ax1, linewidth = 0, color = 'r', zorder = 3, label='Skipped Training')
    ax1.legend(loc = 'lower right')
    line_plot_settings(ax1)
    date_form = DateFormatter("%d %b")
    ax1.xaxis.set_major_formatter(date_form)
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    ax1.set_ylim(bottom = MIN, top = MAX)
    bottom1, top1 = ax1.get_ylim()

    sns.lineplot(x = 'Date', y = 'Diff', data = df, dashes = False, ax = ax2, zorder = 1, label='Trend Line')
    sns.lineplot(x = 'Date', y = 'Diff', data = df_y, marker="o", dashes = False, ax = ax2, linewidth = 0, color = 'g', zorder = 2, label='Training')
    sns.lineplot(x = 'Date', y = 'Diff', data = df_n, marker="o", dashes = False, ax = ax2, linewidth = 0, color = 'r', zorder = 3, label='Skipped Training')
    ax2.legend(loc = 'best')
    diff_plot_settings(ax2)
    ax2.xaxis.set_major_formatter(date_form)
    ax2.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    bottom2, top2 = ax2.get_ylim()

    sns.histplot(data = df, x = 'Weight', stat = 'count', element = 'bars', edgecolor = 'white', kde = True, ax = ax3)
    hist_plot_settings(ax3)
    ax3.set_xlim(left = bottom1, right = top1)

    sns.histplot(data = df, x = 'Diff', hue = 'Training', stat = 'count', element = 'bars', edgecolor = 'white', kde = True, ax = ax4)
    hist_diff_settings(ax4)
    ax4.set_xlim(left = bottom2, right = top2)

    plt.show()

def main():

    df = read_data()
    make_plot(df)
    sys.exit()

if __name__ == "__main__":
    main()