#This code summarizes piping MTO exported from AutoCAD Report Creator.

import pandas as pd

raw_MTO = pd.read_excel('MTO.xlsx')

trim_MTO = raw_MTO.iloc[:-1,2:9]    #remove last row of MTO

trim_MTO = trim_MTO.dropna()        #delete N/A row
trim_MTO['Unit'] = trim_MTO['Unit'].apply(lambda x: 'pcs.' if isinstance(x, str) and x.strip() == '' else x)    #fill blank cell in Unit column with 'pcs.'

sum_MTO = trim_MTO.groupby(['Type','Description','DN','OD','Unit'])['Q\'ty'].sum().reset_index()  #Summarize MTO

print(sum_MTO)