newiris <- iris
newiris$Species <- NULL
(kc <- kmeans(newiris, 3))
print(kc)
# Compare the Species label with the clustering result.
table(iris$Species, kc$cluster)
plot(newiris[, c("Sepal.Length", "Sepal.Width")], col = kc$cluster)
points(kc$centers[c("Sepal.Length", "Sepal.Width")],
col = 1:3, pch = 8, cex = 2)