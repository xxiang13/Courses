#8.1
#a
reg<-lm(H~P,data=text8.1)
library(car)
dwt(reg)
#b
res = resid(reg)
n1<-0
n2<-0
for (i in (1:25)) {if (res[i] > 0) {n1=n1+1} else {n2=n2+1}}
E_R <- (2*n1*n2)/(n1+n2) + 1
E_R
var_R <-(2*n1*n2*(2*n1*n2-n1-n2))/((n1+n2-1)*(n1+n2)^2)
var_R
R<-6
Z<- (R-E_R)/sqrt(var_R)
Z









#########################################8.4#########################################
#a
attach(text8.4)
reg1<-lm(DJIA~Time, data=text8.4)
res1<-resid(reg1)
plot(Time,res1)
#b
djia<-text8.4$DJIA
djia<-djia[-1]
djia_lag<-text8.4$DJIA
djia_lag<-djia_lag[-262]
reg2<-lm(djia~djia_lag)
summary(reg2)
time<-Time
time<-time[-262]
res2<-resid(reg2)
plot(time,res2)
library(car)
dwt(reg2)
#c
log_djia <- log(djia)
reg3<-lm(log_djia~djia_lag)
summary(reg3)
res3<-resid(reg3)
res.sign = res3;
res.sign[which(res3>0)] = 1;
res.sign[which(res3<0)] = -1;
res.index = seq(1:length(res.sign));
plot(res.index, res.sign)

plot(time,res3)
library(car)
dwt(reg3)

#####################################8.5#################################
#a
attach(text8.4)
data_130<- subset(text8.4,Time<=130)
reg4<-lm(djia~djia_lag, data = data_130)
summary(reg4)
res4<-resid(reg4)
anova(reg4) #get residual mean square
#b
data_15<-subset(text8.4,Time<=145)
data_15<-subset(data_15,Time>=131)
for (i in 1:15 ) {data_15$predict[i] = 239.96956 + 0.95732*data_15$djia_lag[i]}
#c
for (i in 1:15) {data_15$pre_error[i]<-data_15$djia[i]-data_15$predict[i]}
SSE =0
for (i in 1:15) {SSE<-SSE+(data_15$pre_error[i])^2}
SSE
ave_SSE<-SSE/15
ave_SSE

#d
data_132<-subset(text8.4,Time>130)
for (i in 1:132 ) {data_132$predict[i] = 239.96956 + 0.95732*data_132$djia_lag[i]}
for (i in 1:132) {data_132$pre_error[i]<-data_132$djia[i]-data_132$predict[i]}
SSE =0
for (i in 1:132) {SSE<-SSE+(data_132$pre_error[i])^2}
SSE
ave_SSE<-SSE/132
ave_SSE

#e
plot(Time,djia)





###############################11.5############################################
#a
reg<-lm(Y~X1+X2+X3+X4+X5+X6+X7+X8+X9, data = text11.5)
summary(reg)
#b
reg1<-lm(Y~X1+X6+X8,data = text11.5)
summary(reg1)
#c
data<-data.frame(X1,X2,X3,X4,X5,X6,X7,X8,X9)
cor(data)
plot(data)
library(car)
vif(reg)

reg2<-lm(Y~X1+X2+X5+X2:X7, data = text11.5)
summary(reg2)

reg3<-lm(Y~X1)
summary(reg3)

#11.6
#a
reg<-lm(Y~X1+X2+X3+X4+X5+X6+X7+X8+X9+X10+factor(X11), data = text9.3)
summary(reg)
#b
reg1<-lm(Y~X1)
summary(reg1)

reg2<-lm(Y~X10)
summary(reg2)

reg3<-lm(Y~X1+X10)
summary(reg3)

reg4<-lm(Y~X2+X10)
summary(reg4)

reg5<-lm(Y~X8+X10)
summary(reg5)

reg6<-lm(Y~X8+X5+X10)
summary(reg6)

reg7<-lm(Y~X8+X5+X10+X1:X3+X1:X7)
summary(reg7)
#c
data<-data.frame(Y,X1,X2,X8,X10)
plot(data)

#d
W<-100/Y
data1<-data.frame(W,X1,X2,X8,X10)
plot(data1)

#e
reg1<-lm(W~X1)
summary(reg1)

reg2<-lm(W~X10)
summary(reg2)

reg3<-lm(W~X1+X10)
summary(reg3)

reg4<-lm(W~X2+X10)
summary(reg4)

reg5<-lm(W~X8+X10)
summary(reg5)

reg6<-lm(W~X8+X5+X10)
summary(reg6)

reg7<-lm(W~X8+X10+X2:X8)
summary(reg7)
#f
X13<-X8/X10
reg7<-lm(Y~X13)
summary(reg7)
