setwd("~/Documents/MSc Astronomy/2018-2019/Astronomical Data Science/mandatory_tasks/project/data")
data <- read.csv(file="oii_3729.csv", header=TRUE, sep=',')

# plot data to see the classification according to the dataset
#png("data_overview_class_plot.png")
#plot(data$x_ratio[data$classification=='AGN'] ,data$y_ratio[data$classification=='AGN'], col='black', xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xlab="log(O[ii]3726 / Hbeta)",  ylab="log(O[iii]5007 / Hbeta)")
#points(data$x_ratio[data$classification=='SBG'] ,data$y_ratio[data$classification=='SBG'], col='red')
#dev.off()


# get the data from somewhere and specify number of folds
nrFolds <- 3

# generate array containing fold-number for each sample (row)
folds <- rep_len(1:nrFolds, nrow(data))

# actual cross validation
for(k in 1:nrFolds) {
  # actual split of the data
  fold <- which(folds == k)
  data.train <- data[-fold,]
  data.test <- data[fold,]
  
  # train and test your model with data.train and data.test
}

# plot your train and test data, where train data is plotted in blue and test data in red

#png("data_overview_plot.png")
#plot(data.train$x_ratio ,data.train$y_ratio, col='black', xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xlab="log(O[ii]3726 / Hbeta)",  ylab="log(O[iii]5007 / Hbeta)")
#points(data.test$x_ratio ,data.test$y_ratio, col='red')
#dev.off()


# apply knn to the data set in order to see possibilities for classification using knn 
library(class)
k_res=knn(as.matrix(data.frame(data.$x_ratio ,data.train$y_ratio)), as.matrix(data.frame(data.test$x_ratio ,data.test$y_ratio)), as.matrix(data.train$classification ),k=1)
k_t=knn(as.matrix(data.frame(data.$x_ratio ,data.train$y_ratio)), as.matrix(data.frame(data.train$x_ratio ,data.train$y_ratio)), as.matrix(data.train$classification ),k=1)
comp=as.numeric(as.matrix(k_t))-as.numeric( data.train$classification )
i_wrong=length(abs(comp[comp !=0]))/ length(comp)

# apply linear discrimination
newtrain <-data.frame(data.train$x_ratio ,data.train$y_ratio)
names(newtrain)<-c("x","y")

newtest <-data.frame(data.test$x_ratio ,data.test$y_ratio)
names(newtest)<-c("x","y")

library(MASS)
lcl=lda(newtrain , data.train$classification )
cl=predict(lcl ,newtest)
#cl$class

# plot data to see the classification according to the classification of the test dataset
#png("data_lds_plot.png")
#plot(newtest$x[cl$class=='AGN'] ,newtest$y[cl$class=='AGN'], col='black', xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xlab="log(O[ii]3726 / Hbeta)",  ylab="log(O[iii]5007 / Hbeta)")
#par(new=TRUE)
#plot(newtest$x[cl$class=='SBG'] ,newtest$y[cl$class=='SBG'], xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xaxt = "n", yaxt = "n", ann=FALSE, col='red')
#dev.off()


library(klaR)

lcl=lda(newtrain , data.train$classification )
cl=predict(lcl ,newtest)
cl$class

# 3726
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG AGN SBG SBG AGN SBG SBG AGN SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN AGN AGN AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG

# 3729
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN AGN AGN SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG


#png("data_lda_dp_plot.png")
#drawparti(cl$class ,data.test$x_ratio ,data.test$y_ratio ,method ="lda", xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xlab="log(O[ii]3726 / Hbeta)",  ylab="log(O[iii]5007 / Hbeta)")
#dev.off()

lcl=qda(newtrain , data.train$classification)
cl=predict(lcl ,newtest)

cl$class
# 3726
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG AGN SBG SBG AGN SBG SBG AGN SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN AGN AGN AGN SBG AGN SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG

# 3729
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN AGN AGN SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG

#png("data_qda_dp_plot.png")
#drawparti(cl$class ,data.test$x_ratio ,data.test$y_ratio ,method ="qda", xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xlab="log(O[ii]3726 / Hbeta)",  ylab="log(O[iii]5007 / Hbeta)")
#dev.off()

lcl =sknn(newtrain , data.train$classification, kn=3)
cl=predict(lcl ,newtest)

cl$class 
# 3726
# k=1
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG AGN SBG SBG AGN SBG SBG AGN SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN AGN AGN AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG SBG
# k=3
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG AGN SBG SBG AGN SBG SBG AGN SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG SBG

# 3729
# k=1
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN AGN AGN SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG
# k=3
# AGN SBG AGN AGN SBG SBG SBG AGN AGN SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG AGN AGN SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG


data.test$classification
# 3726
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG AGN SBG SBG SBG SBG SBG AGN SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN SBG AGN AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG SBG

# 3729
# AGN SBG SBG AGN SBG SBG SBG AGN AGN SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN SBG SBG SBG AGN SBG AGN SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG SBG SBG SBG AGN AGN SBG AGN SBG AGN SBG SBG SBG SBG AGN SBG SBG SBG SBG SBG SBG

#png("data_skn_dp_plot.png")
#drawparti(cl$class ,data.test$x_ratio ,data.test$y_ratio ,method ="sknn", xlim=c(-2.5, 2.5),  ylim=c(-1.4, 2.5), xlab="log(O[ii]3726 / Hbeta)",  ylab="log(O[iii]5007 / Hbeta)")
#dev.off()

