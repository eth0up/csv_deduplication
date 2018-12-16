import glob
import pandas as pd # reqs 'pip install pandas'

# glob.iglob(path) - returns List[str]
# pd.read_csv(currentFile) - returns pd.DataFrame()
# for currentFile in glob.iglob() - returns a List[DataFrames]
# pd.concat() - returns one pd.DataFrame()
# df.drop_duplicates(keep='last') - gets  unique values (rows) by retaining last row
# reset_index(drop = True) - resets the index in the unique list
df = pd.concat([pd.read_csv(currentFile, header = 0, index_col = False) for currentFile in glob.iglob(r'c:\users\user\documents\*.csv')], ignore_index = True).drop_duplicates(subset = None, keep = 'last').reset_index(drop = True)

print("df: " + str(df))
