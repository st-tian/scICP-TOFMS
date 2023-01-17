"""Standard-Sample-Standard method to calibrate the instrumental drift during long-time measurements"""

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

cal_file_path = os.path.join(path,'instrumentaldrift_calibration.csv')  # calibration factor
cal_file = pandas.read_csv(rf'{cal_file_path}', sep=',', header=None)
cal_col = cal_file.values.T.tolist()

for i in range(0, len(filename_list)):
    if len(filename_list[i].split("_")) == 4:
        if filename_list[i].split("_")[2] == "masses":
            file_index = int(filename_list[i].split("_")[-1].split(".")[0])
            file_path = os.path.join(path, filename_list[i])
            file = pandas.read_csv(rf'{file_path}', sep=',', header=None)
            col = file.values.T.tolist()

            for j in range(2, len(col)):
                for k in range(1,len(col[0])):
                    if not pandas.isna(col[j][k]) or not type(col[j][k]) == float:
                        col[j][k] = float(col[j][k])
                        col[j][k] = col[j][k] / float(cal_col[j][file_index])*float(cal_col[j][40])

            new_file = DataFrame(col)
            new_file_name = "Cal-" + filename_list[i]
            new_file.T.to_csv(os.path.join(new_path, new_file_name), header=0, index=False)

            processing_num += 1
            print(f"Processing...{processing_num}")

print(f"Processing Done for {path}")