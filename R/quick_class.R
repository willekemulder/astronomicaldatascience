setwd("~/Documents/MSc Astronomy/2018-2019/Astronomical Data Science/mandatory_tasks/project/data")
data <- read.csv(file="oii_3729.csv", header=TRUE, sep=',')
data_name = 'oii_29'

library(klaR)

# Get the data from somewhere and specify number of folds
nrFolds <- 10

# Create equally size folds of the data
folds <- cut(seq(1,nrow(data)),breaks=nrFolds,labels=FALSE)

# Create data storage
storage_l = 0
storage_q = 0
storage_k1 = 0
storage_k3 = 0

# Perform 10 fold cross validation
for(i in 1:nrFolds){
  # Segement your data by fold using the which() function 
  data.indexes <- which(folds==i,arr.ind=TRUE)
  data.test <- data[data.indexes, ]
  data.train <- data[-data.indexes, ]
  
  # Define a new training and test data frame in order to be able to use R methods
  newtrain <-data.frame(data.train$x_ratio ,data.train$y_ratio)
  newtest <-data.frame(data.test$x_ratio ,data.test$y_ratio)
  
  # Define the same names for the parameters in the 'input' dataset, being emission line ratios
  names(newtrain)<-c("x_ratio","y_ratio")
  names(newtest)<-c("x_ratio","y_ratio")
  
  # Applying Linear Discriminant Analysis CLassification
  lcl=lda(newtrain , data.train$classification )
  cl=predict(lcl ,newtest)
  lin <- cl$class
  print(i)
  print(data.indexes)
  print('lin')
  print(lin)
#  print(data.test$classification)
  lin.correct = 0
  lin.wrong = 0

  # Applying Linear Discriminant Analysis CLassification
  lcl=qda(newtrain , data.train$classification)
  cl=predict(lcl ,newtest)
  qua <- cl$class
  print('qda')
  print(qua)
  
  qua.correct = 0
  qua.wrong = 0

  # Applying K-nearest neighbors for K=1 and K=3
  lcl =sknn(newtrain , data.train$classification, kn=1)
  cl=predict(lcl ,newtest)
  knn_1 <- cl$class 
  print('knn_1')
  print(knn_1)
  
  lcl =sknn(newtrain , data.train$classification, kn=3)
  cl=predict(lcl ,newtest)
  knn_3 <- cl$class 
  print('knn_3')
  print(knn_3)  

  knn_1.correct = 0
  knn_1.wrong = 0  
  knn_3.correct = 0
  knn_3.wrong = 0
  
  for(i in 1:length(newtest[,1])){
    if (identical(lin[i], data.test$classification[i]) == TRUE){
      lin.correct = lin.correct + 1
    } else {
      lin.wrong = lin.wrong + 1
    }
    if (identical(qua[i], data.test$classification[i]) == TRUE){
      qua.correct = qua.correct + 1
    } else {
      qua.wrong = qua.wrong + 1
    }
    if (identical(knn_1[i], data.test$classification[i]) == TRUE){
      knn_1.correct = knn_1.correct + 1
    } else {
      knn_1.wrong = knn_1.wrong + 1
    }
    if (identical(knn_3[i], data.test$classification[i]) == TRUE){
      knn_3.correct = knn_3.correct + 1
    } else {
      knn_3.wrong = knn_3.wrong + 1
    }
  }
  
  # recall = #true positives/(#true positives + #false negatives)
  # precision =  #true positives / (#true positives + #false positives)
  
  rc_lin <- lin.correct/(lin.correct+lin.wrong)
  rc_qda <- qua.correct/(qua.correct+qua.wrong)
  rc_knn1 <- knn_1.correct/(knn_1.correct+knn_1.wrong)
  rc_knn3 <- knn_3.correct/(knn_3.correct+knn_3.wrong) 
  
  storage_l = storage_l + rc_lin
  storage_q = storage_q + rc_qda
  storage_k1 = storage_k1 + rc_knn1
  storage_k3 = storage_k3 + rc_knn3
}
class_rate <- data.frame(storage_l/nrFolds, storage_q/nrFolds, storage_k1/nrFolds, storage_k3/nrFolds)
write.table(class_rate, file=paste0('classrates_', data_name ,'_fold=', nrFolds ,'.csv'), row.names=FALSE, sep=',')