#Problem 1
diabetes <- read.table("~/Documents/MSiA/MSiA 401 stat/HW data/diabetes.csv", header=TRUE, quote="\"")

#Discriminant analysis
library(MASS)
n = dim(diabetes)[1];
fit.lda.prob1 = lda(CC~SSPG+IR+RW, data = diabetes)
fit.lda.prob1;
predict.lda.prob1 = predict(fit.lda.prob1)$class; 
classification.table.prob1= table(diabetes$CC, predict.lda.prob1); 
classification.table.prob1;
classification.rate.prob1 = sum(diag(classification.table.prob1)[1:3])/n;
classification.rate.prob1
miss_classification.rate.prob1 = 1-classification.rate.prob1;
miss_classification.rate.prob1

#Problem 2
systemAdmin <- read.csv("~/Documents/MSiA/MSiA 401 stat/HW data/SystemAdministrators.csv")
#a
library(ggplot2)
systemAdmin$row_num = 1:nrow(systemAdmin)
p <- ggplot(data=systemAdmin, aes(x=Experience,y=Training,col=Completed.task)) + 
  geom_point() + geom_text(aes(label = row_num))
print(p)

#b
fit.lda.prob2 = lda(Completed.task~Training+Experience, data = systemAdmin)
fit.lda.prob2;

#give predicted probabilities
pre.prob<-predict(fit.lda.prob2)$posterior
#give the discriminant function scores
dis.socres<-predict(fit.lda.prob2)$x

#classigy 75 observations
n = dim(systemAdmin)[1]
predict.lda.prob2 = predict(fit.lda.prob2)$class; 
classification.table.prob2= table(systemAdmin$Completed.task, predict.lda.prob2); 
classification.table.prob2;
classification.rate.prob2 = sum(diag(classification.table.prob2)[1:2])/n;
classification.rate.prob2
misclassification.rate.overall = 1-classification.rate.prob2;
misclassification.rate.overall
mislcassification.rate.YES = 5/n
mislcassification.rate.YES
mislcassification.rate.NO = 2/n
mislcassification.rate.NO


#c
predict(fit.lda.prob2,data.frame(Training=6,Experience=4),type="class");

#d
fit.lda.prob2.d = lda(Completed.task~Training+Experience, data = systemAdmin,prior=c(63/75,12/75))
fit.lda.prob2.d;

n = dim(systemAdmin)[1]
predict.lda.prob2.d = predict(fit.lda.prob2.d)$class; 
classification.table.prob2.d= table(systemAdmin$Completed.task, predict.lda.prob2.d); 
classification.table.prob2.d;

classification.rate.prob2.d = sum(diag(classification.table.prob2.d)[1:2])/n;
classification.rate.prob2.d
misclassification.rate.overall.d = 1-classification.rate.prob2.d;
misclassification.rate.overall.d
mislcassification.rate.YES = 5/n
mislcassification.rate.YES
mislcassification.rate.NO = 2/n
mislcassification.rate.NO

#problem 3
injury <- read.delim("~/Documents/MSiA/MSiA 401 stat/HW data/Injury Incidents in Airlines.txt")

#poisson fit

fit.poisson = glm(Y~N, data=injury, family=poisson(log))
summary(fit.poisson)
SSE.poisson = sum((injury$Y-fit.poisson$fitted)^2)
SSE.poisson
#least square fit
fit.lq<-lm(Y~N, data = injury)
summary(fit.lq)
SSE.lq = sum((injury$Y-fit.lq$fitted)^2)
SSE.lq
#transformed least square fit
fit.tlq<-lm(sqrt(Y)~N, data = injury)
summary(fit.tlq)
SSE.tlq = sum((injury$Y-fit.tlq$fitted)^2)

SSE.poisson
SSE.lq
SSE.tlq
