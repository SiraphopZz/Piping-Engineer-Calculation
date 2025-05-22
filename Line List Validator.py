#this program compares new line list with old line list and checks if there are any changes in the line list

import pandas as pd

line_list_old = pd.read_excel("Line List Rev.A.xlsx")   #----------> Path of old line list
line_list_new = pd.read_excel("Line List Rev.B.xlsx")   #----------> Path of new line list

line_list_old.set_index('Line No.', inplace=True)
line_list_new.set_index('Line No.', inplace=True)

added_lines = line_list_new.index.difference(line_list_old.index)
deleted_lines = line_list_old.index.difference(line_list_new.index)

print("-"*20 + "New Lines" + "-"*20)
print(list(added_lines))

print("-"*20 + "Removed Lines" + "-"*16)
print(list(deleted_lines))
