import os
import tkinter
from tkinter import filedialog

import pandas
from pandas import DataFrame
import numpy

processing_num = 0
root = tkinter.Tk()  # select the file-folder with data files
root.withdraw()
path = filedialog.askdirectory(title="Please select the path where the file stored")  # the path
filename_list = os.listdir(path)  # "filename.csv" list
new_path = input("Please input the new path where the new processed file stored, if you input nothing, the new file "
                 "will stored in C:/Users/14488/Desktop/Calibrated as default") or "C:\\Users\\14488\\Desktop\\Calibrated"

for i in range(0, len(filename_list)):
    file_path = os.path.join(path, filename_list[i])
    file = pandas.read_csv(rf'{file_path}', sep=',', header=0)
    new_file = file.replace(numpy.nan, 0)
    # new_file = new_file.select_dtypes(exclude=['object', 'datetime','int64']) * 1e15
    new_file = new_file.iloc[:,2:]*1e15 #前面的冒号是行，后面冒号是列

    new_file.to_csv(os.path.join(new_path, f"{filename_list[i].split('.')[0]}.csv"), index=False)

