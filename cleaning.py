import pandas as pd
df = pd.read_csv('data/all.csv')

#selecting on values that are necessary
desired_columns = ['S.N.', 'Candidate', 'Party', 'EVM Votes', 'Postal Votes', 'Total Votes', '% of Votes']
df_selected = df[desired_columns]

# Save the new CSV
df_selected.to_csv('data/all.csv', index=False)

#checking for null values
null_values = df_selected.isnull().sum()
print(null_values)

