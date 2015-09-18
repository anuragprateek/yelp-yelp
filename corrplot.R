#Input: cuisine_sim_matirx.csv, cuisine_indices.txt
#Output: cuisine similarity map
library(corrplot)
sim = read.csv("../cuisine_sim_matrix.csv", header=FALSE)
cuisines <- scan("../cuisine_indices.txt", what="", sep='\n')
simmatrix = as.matrix(sim)
colnames(simmatrix) <- cuisines
rownames(simmatrix) <- cuisines
png(filename="../cuisine_similarity_map.png")
corrplot(simmatrix, as.corr=FALSE)
dev.off()