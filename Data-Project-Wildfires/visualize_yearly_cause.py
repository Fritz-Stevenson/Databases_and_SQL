import os
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

def visualize_yearly_fire_cause():
    """
    Visualizing the yearly cause csv to highlight the drivers of historical burn trends
    :return: The plot show function.
    Also saves a png file of the plot.
    """
    fig, ax = plt.subplots(figsize=(20,20))
    data = pd.read_csv('.\\CSV_Files\\yearly_fire_cause.csv')
    data = data.loc[data['STAT_CAUSE_DESCR'].isin(['Lightning', 'Equipment Use', 'Miscellaneous', 'Children', 'Arson'])]
    plot_df = pd.pivot_table(data,index=data['FIRE_YEAR'], columns= data['STAT_CAUSE_DESCR'])
    ax.plot(range(1992,2016), plot_df)
    ax.set_title('Yearly Burn Damage Organized by Cause')
    ax.set_xlabel('Calendar Year')
    ax.set_ylabel('Amount Burned (sq mi)')
    ax.set_xticks(range(1992,2016))
    ax.set_xticklabels(range(1992,2016))
    plt.savefig('yearly_burn_damage_by_cause.png')
    plt.xlim([1993,2015])
    ax.legend(labels=['Arson', 'Children', 'Equipment Use', 'Lightning', 'Miscellaneous'])
    return plt.show()


visualize_yearly_fire_cause()
