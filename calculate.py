import pandas as pd
df = pd.read_csv('Sample_Task1.csv')

(df.loc[df['client'] == 1616]).to_csv('results.csv', index=False)