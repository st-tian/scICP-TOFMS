"""2 step: After Rename.py processing. Filtering the events based on P signals"""
import os
import tkinter
from tkinter import filedialog

import pandas
from pandas import DataFrame

processing_num = 0
root = tkinter.Tk()  # select the file-folder with data files
root.withdraw()
path = filedialog.askdirectory(title="Please select the path where the file stored")  # the path
filename_list = os.listdir(path)  # "filename.csv" list
new_path = input("Please input the new path where the new processed file stored, if you input nothing, the new file "
                 "will stored in C:/Users/14488/Desktop/Calibrated as default") or "C:\\Users\\14488\\Desktop\\Calibrated"

title = ['Sample Index', 'Total events', 'P events', 'P event rate', 'Debris rate']
debris_rate = [[None] * (len(filename_list)+1) for i in range(0, len(title))]
for i in range(0, len(title)):
    debris_rate[i][0] = title[i]

for i in range(0, len(filename_list)):
    if len(filename_list[i].split("_")) == 3:
        if filename_list[i].split("_")[1] == "masses" or filename_list[i].split("_")[1] == "intensities":
            file_path = os.path.join(path, filename_list[i])
            file = pandas.read_csv(rf'{file_path}', sep=',', header=None)
            col = file.values.T.tolist()
            total_events = len(col[0])-1
            row_index = int(filename_list[i].split("_")[2].split(".")[0])

            for j in range(0,len(col)):
                col[j][0] = col[j][0].split("]")[0].split("[")[-1]

            if filename_list[i].split("_")[1] == "intensities":
                P_col = col[7]
            elif filename_list[i].split("_")[1] == "masses":
                P_col = col[6]

            new_col = [[] for i in range(0, len(col))]
            for j in range(0, len(col[0])):
                if not pandas.isna(P_col[j]) or not type(P_col[j]) == float:
                    for k in range(0, len(col)):
                        new_col[k].append(col[k][j])
            P_events = len(new_col[0])-1  # event number according to 31P

            if filename_list[i].split("_")[1] == "intensities":
                debris_rate[0][row_index] = row_index
                debris_rate[1][row_index] = total_events
                debris_rate[2][row_index] = P_events
                debris_rate[3][row_index] = f"{P_events / total_events:.2%}"
                debris_rate[4][row_index] = f"{1 - (P_events / total_events):.2%}"

            new_file = DataFrame(new_col)
            new_file_name = "P_" + filename_list[i]
            new_file.T.to_csv(os.path.join(new_path, new_file_name), header=0, index=False)

            processing_num += 1
            print(f"Processing...{processing_num}")
dr = DataFrame(debris_rate)
dr.T.to_excel(os.path.join(new_path, "Debris_rate.xlsx"), header=0, index=False)
print(f"Processing Done for {path}")
