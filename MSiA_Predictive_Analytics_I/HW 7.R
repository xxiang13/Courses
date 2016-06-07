##12.3
#a
attach(text12.3)
text12.3$failure<-ifelse(text12.3$Damaged==0,0,1)
fit.12.3 <- glm(failure~Temperature,binomial,text12.3)
summary(fit.12.3)

# b
text12.3<-text12.3[-18,]
fit.12.3.b <- glm(failure~Temperature,binomial,text12.3)
summary(fit.12.3.b)
#c
predict(fit.12.3.b,data.frame(Temperature=31),type="resp")


##########12.4##############################################
#a
text12.4$Failure = text12.4$Attempts - text12.4$Success
NFL<-subset(text12.4,text12.4$Z==0)
AFL<-subset(text12.4,text12.4$Z==1)

fit.NFL<-glm( cbind( Success, Failure ) ~ Distance+I(Distance^2), data = NFL, family = "binomial" )
summary(fit.NFL)

fit.AFL<-glm( cbind( Success, Failure ) ~ Distance+I(Distance^2), data = AFL, family = "binomial" )
summary(fit.AFL)

#b
fit.12.4.b<-glm( cbind( Success, Failure ) ~ Distance+I(Distance^2)+Z, data = text12.4, family = "binomial" )
summary(fit.12.4.b)


######12.5#####################################################################
#a
fit.12.5.a <- glm(RURAL~BED+MCDAYS+TDAYS+PCREV+NSAL+FEXP+NETREV,binomial,text12.5)
summary(fit.12.5.a )
fit.12.5.a2<-step(fit.12.5.a)
summary(fit.12.5.a2 )
fit.12.5.a3 <- glm(RURAL~NSAL,binomial,text12.5)
summary(fit.12.5.a3 )

#b
fit.12.5.b<-lm(PCREV~RURAL+BED+MCDAYS+TDAYS+NSAL+FEXP,text12.5)
summary(fit.12.5.b)
fit.12.5.b2<-step(fit.12.5.b)
summary(fit.12.5.b2)


#######12.6#####################################################################
library(mlogit);
diab = mlogit.data(data = diabetes, choice="CC", shape="wide",varying=NULL);
fit12.6 = mlogit(CC~0|IR+SSPG, data = diab, reflevel="3"); 
summary(fit12.6);

Y.prob = fitted(fit12.6, outcome= FALSE);
head(Y.prob);

n = dim(diabetes)[1];
Y.hat = rep(0,n);
for(i in 1:n){
  if(max(Y.prob[i,]) == Y.prob[i,1]){
    Y.hat[i]=3;
  }else if(max(Y.prob[i,]) == Y.prob[i,2]){
    Y.hat[i]=1;
  }else if(max(Y.prob[i,]) == Y.prob[i,3]){
    Y.hat[i]=2;
  }
}
Y.hat;

ctable = table(diabetes$CC, Y.hat);
ctable = addmargins(ctable);
ctable;
sum(diag(ctable)[-4])/diag(ctable)[4]
######
fit12.6.a = mlogit(CC~0|IR+SSPG+RW, data = diab, reflevel="3"); 
summary(fit12.6.a);

Y.prob = fitted(fit12.6.a, outcome= FALSE);
head(Y.prob);

n = dim(diabetes)[1];
Y.hat = rep(0,n);
for(i in 1:n){
  if(max(Y.prob[i,]) == Y.prob[i,1]){
    Y.hat[i]=3;
  }else if(max(Y.prob[i,]) == Y.prob[i,2]){
    Y.hat[i]=1;
  }else if(max(Y.prob[i,]) == Y.prob[i,3]){
    Y.hat[i]=2;
  }
}
Y.hat;

ctable = table(diabetes$CC, Y.hat);
ctable = addmargins(ctable);
ctable;
sum(diag(ctable)[-4])/diag(ctable)[4]

#b
library(ordinal)
diabetes$CC.ordered = as.ordered(diabetes$CC);
fit.12.6 <- clm(CC.ordered~IR+SSPG, data = diabetes)
summary(fit.12.6);

Y.hat2 = predict(fit.12.6, data = diabetes, type="class")$fit;
ctable2 = table(diabetes$CC, Y.hat2);
ctable2 = addmargins(ctable2);
ctable2;
sum(diag(ctable2)[-4])/diag(ctable2)[4]

#####
fit.12.6.b <- clm(CC.ordered~IR+SSPG+RW, data = diabetes)
summary(fit.12.6.b);

Y.hat2 = predict(fit.12.6.b, data = diabetes, type="class")$fit;
ctable2 = table(diabetes$CC, Y.hat2);
ctable2 = addmargins(ctable2);
ctable2;
sum(diag(ctable2)[-4])/diag(ctable2)[4]

anova(fit.12.6,fit.12.6.b)




##problem 5###############################################

#put odd-numbered obs into training set
train<-c()
for (i in seq(1,412,2)) {train<-rbind(train,mammography[i,])}
#put even-numbered obs into training set
test<-c()
for (i in seq(2,412,2)) {test<-rbind(test,mammography[i,])}



#######a
library(mlogit)
prob5.train = mlogit.data(data = train, choice="ME", shape="wide",varying=NULL);
fit.prob5.a = mlogit(ME~0|HIST+PB, data = prob5.train, reflevel="2"); 
summary(fit.prob5.a);

prob5.test = mlogit.data(data = test, choice="ME", shape="wide",varying=NULL);
Y.prob= predict(fit.prob5.a,prob5.test,type="resp")
head(Y.prob);

# classify to the category for which it has the highest estimated probabilities
n = dim(train)[1];
Y.hat = rep(0,n);
for(i in 1:n){
  if(max(Y.prob[i,]) == Y.prob[i,1]){
    Y.hat[i]=2;
  }else if(max(Y.prob[i,]) == Y.prob[i,2]){
    Y.hat[i]=0;
  }else if(max(Y.prob[i,]) == Y.prob[i,3]){
    Y.hat[i]=1;
  }
}
Y.hat;

ctable = table(test$ME, Y.hat);
ctable = addmargins(ctable);
ctable;
1-(106+7+0)/(206) #misclassification rate


#############b
library(ordinal)
train$ME.ordered = factor(train$ME,levels=c(0,2,1));
pro5.b <- clm(ME.ordered~HIST+PB, data = train)
summary(pro5.b)

Y.hat2 = predict(pro5.b, newdata = test, type="class")$fit;
ctable2 = table(test$ME, Y.hat2);
ctable2 = addmargins(ctable2);
ctable2;
1-(106+7+0)/206 #misclassification rate

