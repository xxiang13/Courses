#Textbook 2.10
#(a)
colnames(height)[1]<-"Y"; #rename the column
colnames(height)[2]<-"X";

corXY<-cor(height[,1],height[,2]);
corXY;
varY<-var(height[,1]);
varY;
varX<-var(height[,2]);
varX;
covXY = corXY * sqrt(varX*varY);
covXY;
#(b)
newY <- height[,1]*0.393701;
newX<-height[,2]*0.393701;

corXY1<-cor(newY,newX);
corXY1;
varY1<-var(newY);
varY1;
varX1<-var(newX);
varX1;
covXY1 = corXY1 * sqrt(varX1*varY1);
covXY1;

#(e)

wife1<- height[,1]-5;
wife1;
cor(wife1,height[,1]);

#(g)
plot(height[,1],height[,2]);
myreg<-lm(height[,1]~height[,2]);
summary(myreg);

newdaily<- data.frame(c(500000));
newdaily;
                      
predict(myreg,newdaily,interval="predict");

#Textbook 2.12
#(a)
daily<-newspaper[,2];
sunday<-newspaper[,3];
plot(sunday,daily); #scatter plot
#(b)
myreg1<-lm(sunday~daily);
summary(myreg1);
#(c)
confint(myreg1);
#(e)
summary(myreg1);
#(f)
predict(lm(sunday~daily));
new <- data.frame(daily=500);
predict(lm(sunday~daily), new, se.fit = TRUE)
pred.w.clim <- predict(lm(sunday~daily), new, interval = "confidence");
pred.w.clim;
#(g) 
pred.w.clim1 <- predict(lm(sunday~daily), new, interval = "prediction");
pred.w.clim1;

#(h)
predict(lm(sunday~daily));
new <- data.frame(daily=2000);
predict(lm(sunday~daily), new, se.fit = TRUE)
pred.w.clim <- predict(lm(sunday~daily), new, interval = "confidence");
pred.w.clim;

pred.w.clim <- predict(lm(sunday~daily), new, interval = "prediction");
pred.w.clim;
####################################Prof Book
#2.1

y<-prime[,1];
x<-prime[,2];
y1<- log(y);
x1<- log(x);
plot(x1,y1);
abline(myreg2);
qplot(x1,y1)
myreg2<-lm(y1~x1);
summary(myreg2);
confint(myreg2);
#2.2
#a
attach stock;
SP500<-stock[,1];
IBM<-stock[,2];
apple<-stock[,3];
pairs(stock);

#b
myreg3<-lm(SP500~apple);
summary(myreg3);
myreg4<-lm(SP500~IBM);
summary(myreg4);

#c
sd(apple); #standard deviation
sd(IBM);
sd(SP500);

cor(stock); #correlation matrix

#2.3
demand_chuck <- log(MeatPrices[,1]);
price_chuck <- log(MeatPrices[,2]);
demand_porter <- log(MeatPrices[,3]);
price_porter <- log(MeatPrices[,4]);
demand_ribeye <- log(MeatPrices[,5]);
price_ribeye <- log(MeatPrices[,6]);

myreg5<-lm(demand_chuck~price_chuck);
myreg6<-lm(demand_porter~price_porter);
myreg7<-lm(demand_ribeye~price_ribeye);
summary(myreg5);
summary(myreg6);
summary(myreg7);

#2.4
cor(smoking.cancer);
plot(smoking.cancer);

