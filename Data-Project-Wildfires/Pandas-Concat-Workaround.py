'''Work around for a faulty csv conversion where a column division had three seperators which caused errors when
importing to the postgresql database. Instead of floundering trying to reformat every file, this saved quite a bit of
time.'''
import os
import pandas as pd
csv_folder = '.\\yearly_OR_fires\\'
full_set_csv = pd.concat([pd.read_csv(csv_folder+file, sep=';') for file in os.listdir(csv_folder)])
print(full_set_csv.head(5))
full_set_csv.to_csv('OR_Fires.csv', index=False)
