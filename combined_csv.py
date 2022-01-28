from msilib.schema import Directory
import pandas as pd
import glob
import os

current_dir = os.getcwd()

# setting the path for joining multiple files
files = os.path.join(current_dir, "*.csv")

# list of merged files returned
files = glob.glob(files)

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
print(df)

# crate output csv file
df.to_csv("combined.csv")