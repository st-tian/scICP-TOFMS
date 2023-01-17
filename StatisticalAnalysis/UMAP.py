import os

import pandas
import umap

import tkinter
from tkinter import filedialog

from pandas import DataFrame

'''对话框选择获取文件路径和文件名,用于后续读取和命名'''
root = tkinter.Tk()  # 打开选择文件夹对话框
root.withdraw()
folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
filepath = filedialog.askopenfilename()  # 获得选择好的文件
file_name0 = filepath.split("/")[-1]  # 去除读取的文件路径
file_name = os.path.splitext(os.path.basename(file_name0))[0]  # 去后缀

# data = pandas.read_csv(filepath)
# data = data.transpose()
# d_embedding = umap.UMAP().fit_transform(data)


data = pandas.read_csv(filepath)
data1 = data.transpose()
# data1 = data1.iloc[:, :-2]
# label = data.iloc[:, [-1]]

d_embedding = umap.UMAP().fit_transform(data1)
# out = pandas.merge(d_embedding,label)

df = DataFrame(d_embedding)
df.to_csv(f"UMAP-{file_name}.csv")


print(d_embedding)