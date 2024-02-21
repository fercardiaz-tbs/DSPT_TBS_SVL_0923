import pandas as pd
df = pd.read_parquet('transformations_Theoretical_Hours_Worked_Ratio.parquet')
df.to_csv('transformations_Theoretical_Hours_Worked_Ratio.csv')