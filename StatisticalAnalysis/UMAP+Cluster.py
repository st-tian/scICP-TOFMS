import os

import pandas
import numpy
import umap

import tkinter
from tkinter import filedialog

from matplotlib import pyplot as plt
import scipy.cluster.hierarchy as sch


'''对话框选择获取文件路径和文件名,用于后续读取和命名'''
root = tkinter.Tk()  # 打开选择文件夹对话框
root.withdraw()
path = filedialog.askdirectory()  # 获得选择好的文件夹
all_file_list = os.listdir(path)  # all file under the path including folder, xlsx...


def file_filter(f):  # select csv files
    if f.split(".")[-1] == "csv":
        return True
    else:
        return False


filename_list = list(filter(file_filter, all_file_list))  # "filename.csv" list
label = ['23Na','24Mg','25Mg','27Al','31P','39K','43Ca','44Ca','51V','52Cr','55Mn','56Fe','58Ni','60Ni','63Cu','65Cu','66Zn','68Zn','78Se','85Rb','88Sr','107Ag','137Ba','197Au','208Pb']
distance = [1.5, 2, 3]
output = [[],[],[]]

for i in range(0, len(filename_list)):
    print(f"Processing {i + 1} ...")
    file_name = filename_list[i].split(".")[0]
    filepath = os.path.join(path, filename_list[i])

    data0 = pandas.read_csv(filepath)
    data1 = data0.transpose()

    d_embedding = umap.UMAP().fit_transform(data1)
    data = pandas.DataFrame(d_embedding)
    data.to_csv(f"UMAP-{file_name}.csv")
    # data = data.transpose()
    data = data.values
    print(data)

    # dendrogram = sch.dendrogram(sch.linkage(data , method = 'ward'),labels=label) # 使用树状图找到最佳聚类数
    Z = sch.linkage(data, method = 'ward')

    for index in range(0,len(distance)):
        f = list(sch.fcluster(Z, t=distance[index], criterion="distance"))
        dendrogram = sch.dendrogram(Z, labels=label)  # 使用树状图找到最佳聚类数
        print(f)
        # plt.axhline(y=1.5, color='r', linestyle = '-')
        # plt.title('Dendrogram') # 标题
        # plt.xlabel('Customers') # 横标签
        # plt.ylabel('Euclidean distances') # 纵标签
        # plt.show()

        cluster_num = max(list(f))
        cluster = [None]*(cluster_num+1)
        cluster[0] = file_name
        for i in range(0,len(f)):
            if cluster[f[i]] is None:
                cluster[f[i]] = label[i]
            else:
                cluster[f[i]] = f"{cluster[f[i]]} {label[i]}"

        output[index].append(cluster)

for i in range(0,len(output)):
    df = pandas.DataFrame(output[i])
    df.to_excel(f"UMAP+Cluster_distance{distance[i]}.xlsx")
