#prob 1 9.3
attach(gas_con)
cor(gas_con)
plot(X1,X2)
plot(gas_con)
fitted<-lm(Y~X1+X2+X3+X4+X5+X6+X7+X8+X9+X10+X11)
summary(fitted)
library(car)
vif(fitted)
kappa(fitted)

#prob 9.4
attach(text.5.9)
str(text.5.9)

a = data.frame(Year,I,D,W,G,P,N)
cor(a)
fitted1<-lm(V~Year+I+D+W+G:I+P+N+I:D+P:N+W:D)
kappa(cor(a),exact=TRUE)
kappa(cor(a),exact=TRUE)
vif(fitted1)

b = data.frame(I,W,P,N,D1,D2,G*I)
cor(b)
fitted2<-lm(V~I+D1+D2+W+G:I+P+N)
library(perturb)
collidiag(fitted2)$condindx
kappa(cor(b), exact = TRUE)
library(car)
vif(fitted2)

#4
attach(prob4)
c<-data.frame(prob4$x1,prob4$x2,prob4$x3)
plot(c)
cor(c)
library(car)
fitted3<-lm(y~x1+x2+x3+x1*x2+x1*x3+x2*x3+I(x1^2)+I(x2^2)+I(x3^2))
vif(fitted3)
meanx1 = mean(x1)
x1center<-x1-meanx1
x1center

meanx2 = mean(x2)
x2center<-x2-meanx2
x2center
meanx3 = mean(x3)
x3center<-x3-meanx3
x3center

fitted4<-lm(y~x1center+x2center+x3center+x1center*x2center+x1center*x3center+
              x2center*x3center+I(x1center^2)+I(x2center^2)+I(x3center^2))
summary(fitted4)
vif(fitted4)
