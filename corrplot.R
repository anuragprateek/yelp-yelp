#Input: cuisine_sim_matirx.csv, cuisine_indices.txt
#Output: cuisine similarity map
library(corrplot)
<<<<<<< HEAD
sim = read.csv("cuisine_sim_matrix.csv", header=FALSE)
cuisines <- scan("cuisine_indices.txt", what="", sep='\n')
simmatrix = as.matrix(sim)
colnames(simmatrix) <- cuisines
rownames(simmatrix) <- cuisines
png(filename="cuisine_similarity_map.png")
corrplot(simmatrix, as.corr=FALSE)
dev.off()
=======
sim = read.csv("../cuisine_sim_matrix.csv", header=FALSE)
cuisines <- scan("../cuisine_indices.txt", what="", sep='\n')
simmatrix = as.matrix(sim)
colnames(simmatrix) <- cuisines
rownames(simmatrix) <- cuisines
jpeg(filename="../cuisine_similarity_map_alphabet.jpeg", width=1024, height=1024, units="px", quality=100, res=150)
#corrplot(simmatrix, as.corr=FALSE)
corrplot(simmatrix,method="shade",tl.cex=0.6,order="alphabet",is.cor=FALSE,type="lower")
dev.off()
jpeg(filename="../cuisine_similarity_map_cluster.jpeg", width=1024, height=1024, units="px", quality=100, res=150)
#corrplot(simmatrix, as.corr=FALSE)
corrplot(simmatrix,method="shade",tl.cex=0.6,order="hclust",is.cor=FALSE,type="lower")
dev.off()
>>>>>>> 3b230357b689a22c769e73b045ff2d849ace209d
