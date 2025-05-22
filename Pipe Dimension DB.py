#Show all pipe thickness for the selected pipe DN
import pandas as pd

pipe_db = pd.read_csv("Pipe Dimension DB.csv")

DN = int(input("Please input pipe DN: "))
sel_pipe_db = pipe_db[pipe_db['DN']==DN]

if sel_pipe_db.empty:
    print("**********No selected pipe DN**********")
else:
    print(sel_pipe_db)