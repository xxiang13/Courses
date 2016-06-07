#problem1 (text4.7)
attach(text3.15)
str(text3.15)
cigarette_sale<- data.frame(Age,HS,Income,Black,Female,Price,Sales)
cor(cigarette_sale)
plot(cigarette_sale)
detach(text3.15)

attach(cigarette_sale)
summary(lm(Sales~Age+Black+Female+HS+Income+Price))

#problem2 (text4.12)
#a
attach(text4.12)
plot(Y,X1) #check assumption 1

reg = lm(Y~X1+X2+X3+X4+X5+X6)

fitted<-fitted(reg) #find the fitted values from reg

reg.res = resid(reg)
plot(X6, reg.res, ylab="Residuals", xlab="X1", main="Residual vs. X6") 
abline(0, 0)

#check assumption 2
reg.stdres = rstandard(reg)
qqnorm(reg.stdres, ylab="Standardized Residuals", xlab="Normal Scores", main="Normal Probability Plot of Residuals") 
qqline(reg.stdres)
hist(reg.stdres)

m<-mean(reg.stdres)
std<-sqrt(var(reg.stdres))
hist(reg.stdres, density=20, breaks=10, prob=TRUE, 
     xlab="reg.stdres", ylim=c(0, 0.7), 
     main="normal curve over histogram")

xfit<-seq(min(reg.stdres),max(reg.stdres),length=40)
yfit<-dnorm(xfit)
lines(xfit,yfit)


#check Var(error) == constant
sqrt((reg.res)^2)
plot(fitted, sqrt((reg.res)^2), ylab="Residuals", xlab="Fitted Values", main="Residual Fitted Plot") 
abline(0, 0)

#check outliers + leverages
outlierTest(reg)
influencePlot(reg)
leveragePlots(reg)

#problem 3 (4.13)
reg1<-lm(Y~X1+X2+X3)


reg2<-(lm(Y~X1+X2+X3+X4))
summary(reg2)

reg3<-lm(Y~X1+X2+X3+X4+X5)
summary(reg3)

reg4<-lm(Y~X1+X2+X3+X4+X6)
summary(reg4)

#Problem 4
str(used_car)
attach(used_car)
log_reg<-lm(log.Price.~Mileage+Liter+Cadillac+Chevrolet+Pontiac+SAAB+Saturn+Convertible+Hatchback+Sedan)
log_reg.stdres = rstandard(log_reg)
log_reg.fitted<-fitted(log_reg)
plot(log_reg.fitted, log_reg.stdres, ylab="Residuals", xlab="Fitted values of log(price)", main="Residual Fitted Plot") 
abline(0, 0)

price_reg<-lm(Price~Mileage+Liter+Cadillac+Chevrolet+Pontiac+SAAB+Saturn+Convertible+Hatchback+Sedan)
price_reg.stdres = rstandard(price_reg)
price_reg.fitted<-fitted(price_reg)
plot(price_reg.fitted, price_reg.stdres, ylab="Residuals", xlab="Fitted values of price", main="Residual Fitted Plot") 
abline(0, 0)

#Problem 5
X1<-c(0.499,0.558,0.604,0.441,0.550,0.528,0.418,0.480,0.406,0.467)
X2<-c(11.1,8.9,8.8,8.9,8.8,9.9,10.7,10.5,10.5,10.7)
Y<-c(11.14,12.74,13.13,11.51,12.38,12.60,11.13,11.70,11.02,11.41)
prob5<-data.frame(Y,X1,X2)
#a
plot(X1,X2)
fit<-lm(Y~X1+X2)
influencePlot(fit)

#(c)

x=prob5
x=x[-c(1,4),]
fit1<-lm(x$Y~x$X1+x$X2)
summary(fit)
summary(fit1)
outlier(prob5)
