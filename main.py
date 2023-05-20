import numpy as np
import os
import pandas as pd

df_final = pd.DataFrame()
file_names = os.listdir("data_tables")
current_path = os.getcwd()
for file_name in file_names:
    real_file_name = file_name.split(".")[0]
    if ".xlsx" in file_name:
        read_file = pd.read_excel(fr"{current_path}\data_tables\{file_name}")
        read_file.to_csv(f"{current_path}\data_tables\{real_file_name}.csv", index=None, header=True)
        os.remove(fr"{current_path}\data_tables\{file_name}")
    temp_df = pd.read_csv(fr"{current_path}\data_tables\{real_file_name}.csv")

    if file_name == file_names[0]:
        row_num = 0
        df_final['code'] = np.arange((len(temp_df)) * (len(temp_df.columns[2:])))
        df_final['t'] = np.arange((len(temp_df)) * (len(temp_df.columns[2:])))
        year_num = 0
        for index, row in temp_df.iterrows():
            for t in temp_df.columns[2:]:
                df_final['t'][row_num] = t
                df_final['code'][row_num] = row[0]
                row_num += 1

    row_num = 0
    variable_name = temp_df.iloc[0, 1]
    df_final[variable_name] = np.arange((len(temp_df)) * (len(temp_df.columns[2:])))
    for index, row in temp_df.iterrows():
        column_num = 0
        for t in temp_df.columns[2:]:
            df_final[variable_name][row_num] = temp_df.iloc[:, 2:].iloc[index, column_num]
            column_num += 1
            row_num += 1

df_final.to_csv("panel_data.csv")

