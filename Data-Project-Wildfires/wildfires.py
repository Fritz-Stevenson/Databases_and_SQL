import os
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def create_concat_csv():
    "concatenates yearly csv files into a single file for insertion into a database"
    csv_folder = '.\\yearly_OR_fires\\'
    full_set_csv = pd.concat([pd.read_csv(csv_folder+file, sep=';') for file in os.listdir(csv_folder)])
    print(full_set_csv.head(5))
    full_set_csv.to_csv('OR_Fires.csv', index=False)
    return full_set_csv

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

#print(plot_df.head(20))