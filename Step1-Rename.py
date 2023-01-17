"""1 step: Rename the .csv data files obtained by TOFPilot software, as the file name is too long to further processing"""

import os
import tkinter
from tkinter import filedialog

root = tkinter.Tk()  # select the file-folder with data files
root.withdraw()
path = filedialog.askdirectory()
filename_list = os.listdir(path)

for i in range(0, len(filename_list)):
    if len(filename_list[i].split("_")) > 2:
        if filename_list[i].split("_")[1] == "masses" or filename_list[i].split("_")[1] == "intensities":
            filepath = os.path.join(path, filename_list[i])
            filetype = filename_list[i].split(".")[-1]
            newname = filename_list[i].split("_")[0] + "_" + filename_list[i].split("_")[1] + "_" + \
                      filename_list[i].split("_")[2] + "." + filetype
            filepath_new = os.path.join(path, newname)
            os.rename(filepath, filepath_new)
