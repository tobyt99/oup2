import os
import pandas as pd

df=pd.DataFrame()
folder_path = "new"
for file_ in os.listdir(folder_path):
    temp=pd.read_csv(folder_path+'/'+file_,header=None,skiprows=1,error_bad_lines=False)
    df=pd.concat([df,temp],ignore_index=True)

df.columns=["Created Date","Created By","Work Status","Work Sort Title","Updated Date","Updated By"]
df.to_csv('new_works.csv',index=False)

df=pd.DataFrame()
folder_path = "wip"
for file_ in os.listdir(folder_path):
    temp=pd.read_csv(folder_path+'/'+file_,header=None,skiprows=1)
    df=pd.concat([df,temp],ignore_index=True)

df.columns=["Updated" "Date","Updated By","Cover Title (Work or Edition level)","Impression Impression Stage","Edition Product Type","Created By","Created Date","Impression Description","Impression Number"]
df.to_csv('wip.csv',index=False)

df=pd.DataFrame()
folder_path = "logins"
for file_ in os.listdir(folder_path):
    temp=pd.read_csv(folder_path+'/'+file_,header=None,skiprows=1)
    df=pd.concat([df,temp],ignore_index=True)

df.columns=["User", "Email", "Login_Date"]
df.to_csv('logins.csv',index=False)