#相关性热图

library(ggcorrplot)
library(ggthemes)
data = read.csv(file.choose(),header=T,sep=",")
#data = mtcars
corr = round(cor(data,use = "pairwise"),3)
mat = round(cor_pmat(data),3)#3位小数


ggcorrplot(corr,hc.method = "ward.D",method = "square",
           outline.color = "white",ggtheme = theme_bw(),
           type = "lower",#upper
           colors = c("#6D9EC1","whitesmoke","red") , #改变颜色
           lab = TRUE,lab_size = 2 , #显示相关系数标签
           p.mat = mat,insig = "blank") 


library(corrplot)
corrplot(corr)
