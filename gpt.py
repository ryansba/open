import pandas as pd

csv_file = '/623payouts/olt_ra.csv'

# CSV File Copied From Notepad++ 
# Master,Office,Tech,Out
# 007021,613605, $25.00 , $15.00 
# 007021,563317, $25.00 , $15.00 
# 007021,613605, $25.00 , $15.00 
# 007021,613605, $25.00 , $15.00 
# 007021,563317, $25.00 , $15.00 
# FIG 1

df = pd.read_csv(csv_file)

print(df)
#    Master  Office      Tech       Out
# 0    7021  613605   $25.00    $15.00 
# 1    7021  563317   $25.00    $15.00 
# 2    7021  613605   $25.00    $15.00 
# 3    7021  613605   $25.00    $15.00 
# 4    7021  563317   $25.00    $15.00 

print(df.dtypes)
# Master     int64
# Office     int64
# Tech      object
# Out       object


# Hi ChatGPT Please see instructions below

# Write a function that accepts Master as arg and...
# Returns back one row per unique value in the office col also...
# Sums the values in Tech / Out and pretty please
# I need to retain the format of Master and Office as they were in # FIG 1

