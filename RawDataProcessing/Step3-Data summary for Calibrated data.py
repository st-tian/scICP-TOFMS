"""Summarizing the filtered (based on 31P) data: positive rate, mean, etc.
For calibrated mass data"""
import copy
import os
import tkinter
from tkinter import filedialog

import numpy
import pandas
from pandas import DataFrame

processing_num = 0
root = tkinter.Tk()  # select the file-folder with data files
root.withdraw()
path = filedialog.askdirectory()  # the path
all_file_list = os.listdir(path)  # all file under the path including folder, xlsx...


def file_filter(f):  # select csv files
    if f.split(".")[-1] == "csv":
        return True
    else:
        return False

filename_list = list(filter(file_filter, all_file_list))  # "filename.csv" list

file_path = os.path.join(path, "Cal-P_particle_masses_1.csv")
file = pandas.read_csv(rf'{file_path}', sep=',', header=None)
col = file.values.T.tolist()
mean_mass = [[None] * 50 for i in range(0, len(col))]
positive_percentage = [[None] * 50 for i in range(0, len(col))]
positive_percentage[1][0] = 'SampleIndex'
mean_mass[1][0] = 'SampleIndex'
positive_percentage[0][0] = 'TotalEvent'
mean_mass[0][0] = 'TotalEvent'

for i in range(0, 40):
    print(f"Processing {i+1} ...")
    file_path = os.path.join(path, filename_list[i])
    file = pandas.read_csv(rf'{file_path}', sep=',', header=None)
    col = file.values.T.tolist()
    total_event_num = len(col[0]) - 1
    row_index = int(filename_list[i].split("_")[3].split(".")[0])

    if filename_list[i].split("_")[2] == "masses":
        mean_mass[1][row_index] = row_index
        mean_mass[0][row_index] = total_event_num
        positive_percentage[1][row_index] = row_index
        positive_percentage[0][row_index] = total_event_num
        for j in range(2, len(mean_mass)):
            positive_percentage[j][0] = col[j][0]
            mean_mass[j][0] = col[j][0]
            filter_col = []
            for k in col[j][1:]:
                if not pandas.isna(k):
                    filter_col.append(float(k))

            if total_event_num > 0:
                percentage = len(filter_col) / total_event_num
                if len(filter_col) != 0:
                    mean = numpy.average(filter_col)*1e15
                else:
                    mean = None
            elif total_event_num == 0:
                percentage = None
                mean = None
            positive_percentage[j][row_index] = percentage
            mean_mass[j][row_index] = mean

pp = DataFrame(positive_percentage)
mm = DataFrame(mean_mass)
pp.T.to_excel(os.path.join(path, "Sum_Positive_percentage.xlsx"), header=0, index=False)
mm.T.to_excel(os.path.join(path, "Sum_Mass.xlsx"), header=0, index=False)
print(f"Processing Done for {path}")