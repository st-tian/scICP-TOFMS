import os
import pandas
import tkinter
from tkinter import filedialog
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
# from sklearn.cluster import AgglomerativeClustering

# from pandas import DataFrame

'''对话框选择获取文件路径和文件名,用于后续读取和命名'''
root = tkinter.Tk()  # 打开选择文件夹对话框
root.withdraw()
folderpath = filedialog.askdirectory()  # 获得选择好的文件夹
filepath = filedialog.askopenfilename()  # 获得选择好的文件
file_name0 = filepath.split("/")[-1]  # 去除读取的文件路径
file_name = os.path.splitext(os.path.basename(file_name0))[0]  # 去后缀

data = pandas.read_csv(filepath)
# label = data.iloc[:,[0]].values
# print(label)
data = data.iloc[:,1:]
# data = data.transpose()
data = data.values
print(data)
label = ['23Na','24Mg','25Mg','27Al','31P','39K','43Ca','44Ca','51V','52Cr','55Mn','56Fe','58Ni','60Ni','63Cu','65Cu','66Zn','68Zn','78Se','85Rb','88Sr','107Ag','137Ba','197Au','208Pb']

# dendrogram = sch.dendrogram(sch.linkage(data , method = 'ward'),labels=label) # 使用树状图找到最佳聚类数
Z = sch.linkage(data, method = 'ward')
f = sch.fcluster(Z, t=1.5, criterion="distance")
dendrogram = sch.dendrogram(Z,labels=label)  # 使用树状图找到最佳聚类数
print(list(f))
plt.axhline(y=1.5, color='r', linestyle = 'dashed',linewidth =2.0)

# plt.title('Dendrogram') # 标题
plt.xlabel('Elements') # 横标签
# plt.xticks(fontsize = 15)
plt.ylabel('Euclidean distances') # 纵标签
# plt.yticks(fontsize = 15)

TK = plt.gca()
TK.spines['bottom'].set_linewidth(2)
TK.spines['top'].set_linewidth(2)
TK.spines['left'].set_linewidth(2)
TK.spines['right'].set_linewidth(2)
# labels = TK.get_xticklabels() + TK.get_yticklabels()
# [label.set_fontname('Arial') for label in labels]#设置刻度横线的长度与粗细
plt.tick_params(axis='both',width=2,length=5)
plt.rcParams['figure.dpi'] = 600 #分辨率

plt.show()

