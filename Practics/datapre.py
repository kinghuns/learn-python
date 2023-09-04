from dataprep.datasets import load_dataset
from dataprep.eda import create_report
import pandas as pd

# df = load_dataset("titanic")
# create_report(df).show_browser()

from dataprep.eda import plot
from dataprep.datasets import load_dataset
import numpy as np
# df = load_dataset('adult')

# df = pd.read_csv(r"d:\downloads\MOCK_DATA.csv")

# create_report(df).show_browser()


# import connectorx as cx

# conn = 'mssql://sa:Test@admin!@192.192.192.214\TEST'         # connection token
# query = 'SELECT TOP (100) *  FROM [CDR_ADT].[dbo].[ADT_IP_PatientAcount]'                                   # query string
# cx.read_sql(conn, query)                                        # read data from MsSQL


import pymssql 
conn = pymssql.connect(
    host = r'192.192.192.214\TEST',
    database='CDR_ADT',
    user='sa',
    password='Test@admin!'
)

cursor = conn.cursor()
sql = 'SELECT TOP (100) *  FROM [CDR_ADT].[dbo].[ADT_IP_PatientAcount]' 
cursor.execute(sql)

rows = cursor.fetchone()  

for row in rows:
    print('PatientID = %d, Name = %s, Age = %d ' % (row['PatientID'][1],row['PatientName'],row['PatientAge']))
    # print('PatientID = %d' % (row['PatientID'][1]))
    # print(row[0],row[1],row[2])
