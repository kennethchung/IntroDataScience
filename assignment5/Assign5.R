
seaflow=read.csv("seaflow_21min.csv",head=TRUE)
question1<-function(){
  
  summary(seaflow$pop=='synecho')
}



question3<-function(){
  set.seed(2)
  train = sample(1:nrow(seaflow), nrow(seaflow)/2)
  test = -train

  print(length(train))
  print(length(test))
  mean(seaflow[test,]$time)
  
}


question4<-function(){
  set.seed(2)
  train = sample(1:nrow(seaflow), nrow(seaflow)/2)
  test = -train
  set.seed(955)
  # Make some noisily increasing data
  dat <- data.frame(cond = rep(c("A", "B"), each=10),
                    xvar = 1:20 + rnorm(20,sd=3),
                    yvar = 1:20 + rnorm(20,sd=3))
  #ggplot(train, aes(x=xvar, y=yvar, color=cond)) + geom_point(shape=1)
  ggplot(as.data.frame(seaflow), aes(y=pe, x=chl_small, color=pop)) + geom_point(shape=1)
}
library("partykit")
question5<-function(){
  set.seed(2)
  train = sample(1:nrow(seaflow), nrow(seaflow)/2)
  test = -train

  fol <- formula(pop  ~  fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small )
  model <-rpart(formula=fol,data=(seaflow[train,]))
  print(model)
  print(as.party(model), header = FALSE)
  plot(as.party(model), type="simple")

  #plotcp(model)
  printcp(model)
  
}

question8<-function(){
  set.seed(2)
  train = sample(1:nrow(seaflow), nrow(seaflow)/2)
  test = -train
  
  fol <- formula(pop  ~  fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small )
  model <-rpart(formula=fol,data=(seaflow[train,]))
  predictions=predict(model, newdata = seaflow[test,],type="class" )
  pred.df <-as.data.frame(predictions)

  prob <- sum(pred.df[,1] == seaflow[test,]$pop) /nrow(seaflow[test,])
  str(predictions)
  
  
}
library(randomForest)
question9<-function(){
  set.seed(2)
  train = sample(1:nrow(seaflow), nrow(seaflow)/2)
  test = -train
  
  traindata = seaflow[train,]
  testdata = seaflow[test,]
  fol <- formula(pop  ~  fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small )
  model<-randomForest(fol, data=traindata,nodesize = 10,importance=TRUE);
  print(model$importance)
  importance(model, type=2)
  #predictions=predict(model, testdata,type="class" )
  #pred.df <-as.data.frame(predictions)
  
  #prob <- sum(pred.df[,1] == testdata$pop) /nrow(testdata)
  #print(prob)
  #print(model)
  
}
library("e1071")
question11<-function(){
  set.seed(2)
  print(nrow(seaflow))
  train = sample(1:nrow(seaflow), nrow(seaflow)/2)
  test = -train
  
  traindata = seaflow[train,]
  testdata = seaflow[test,]
  fol <- formula(pop  ~  fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small )
  model <- svm(fol, data=traindata)
  
  predictions <- predict(model,testdata)
  pred.df <-as.data.frame(predictions)
  prob <- sum(pred.df[,1] == testdata$pop) /nrow(testdata)
  print(prob)
  print(table(pred = predictions, true = testdata$pop))
  print(round(prop.table(table(pred = predictions, true = testdata$pop))))
}
question14<-function(){
  set.seed(2)
  filtered_seaflow_index = seaflow$file_id != 208
  filtered_seaflow = seaflow[filtered_seaflow_index,]
  print(nrow(filtered_seaflow))
  
  train = sample(1:nrow(filtered_seaflow), nrow(filtered_seaflow)/2)
  test = -train
  
  traindata = filtered_seaflow[train,]
  testdata = filtered_seaflow[test,]
  fol <- formula(pop  ~  fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small )
  model <- svm(fol, data=traindata)
  
  predictions <- predict(model,testdata)
  pred.df <-as.data.frame(predictions)
  prob <- sum(pred.df[,1] == testdata$pop) /nrow(testdata)
  print(prob)
  print(table(pred = predictions, true = testdata$pop))
}


library("ipred")
glau<-function()
{
  data("GlaucomaM", package="ipred")
  
}



