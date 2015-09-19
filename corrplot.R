#Input: cuisine_sim_matirx.csv, cuisine_indices.txt
#Output: cuisine similarity map
library(corrplot)
sim = read.csv("../cuisine_sim_matrix.csv", header=FALSE)
cuisines <- scan("../cuisine_indices.txt", what="", sep='\n')
simmatrix = as.matrix(sim)
colnames(simmatrix) <- cuisines
rownames(simmatrix) <- cuisines
jpeg(filename="../cuisine_similarity_map.jpeg", width=2048, height=2048, units="px", quality=100, res=150)
#corrplot(simmatrix, as.corr=FALSE)
corrplot(simmatrix,method="shade",tl.cex=0.5,order="hclust",is.cor=FALSE,type="lower")
dev.off()