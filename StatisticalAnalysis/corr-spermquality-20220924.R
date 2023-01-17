#�������ͼ

library(ggcorrplot)
library(ggthemes)
data = read.csv(file.choose(),header=T,sep=",")
#data = mtcars
corr = round(cor(data,use = "pairwise"),3)
mat = round(cor_pmat(data),3)#3λС��


ggcorrplot(corr,hc.method = "ward.D",method = "square",
           outline.color = "white",ggtheme = theme_bw(),
           type = "lower",#upper
           colors = c("#6D9EC1","whitesmoke","red") , #�ı���ɫ
           lab = TRUE,lab_size = 2 , #��ʾ���ϵ����ǩ
           p.mat = mat,insig = "blank") 


library(corrplot)
corrplot(corr)