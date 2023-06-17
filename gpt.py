import pandas as pd

csv_file = '/623payouts/olt_ra.csv'


df = pd.read_csv(csv_file)

print(df)


print(df.dtypes)

def process_df(master):

    filtered_df = df[df['Master'] == int(master)]

    filtered_df['Tech'] = filtered_df['Tech'].replace({'\$': ''}, regex=True).astype(float)
    filtered_df['Out'] = filtered_df['Out'].replace({'\$': ''}, regex=True).astype(float)
    print(filtered_df)

    result = filtered_df.groupby('Office').agg({'Tech': 'sum', 'Out': 'sum'}).reset_index()


    result['Office'] = result['Office'].apply(lambda x: str(x).zfill(6))

    return result

result = process_df('007021')
print(result)