import pandas as pd

pipe_db = pd.read_csv("Pipe Dimension DB.csv")
a = pipe_db[(pipe_db['OD (mm)'] == 10.3) & (pipe_db['Wall Thickness (mm)'] >= 1.5)]
print(pipe_db)
print(a)