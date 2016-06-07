#Testbook
#3.15
attach(cigratte_consume);
cigratte_consume$State<- NULL;  #drop column
str(cigratte_consume);   #check data type
#(a)
Full<-lm(Sales~Age+HS+Income+Black+Female+Price);

Reduce<-lm(Sales~Age+Income+Black+Price);
anova(myreg3,myreg1);

#(b)
var(HS);
var(Female);
cor(HS,Female);
cov(HS,Female);
(-0.06159+1.05286)/sqrt(var(HS)+var(Female))-2*cov(HS,Female);

#(c)
confint(myreg3, df=49);

#(d)
myreg2<-lm(Sales~Age+HS+Black+Female+Price);
summary(myreg2);

#(e)
myreg3<-lm(Sales~Age+Income+Price);
summary(myreg3);

#(f) 
myreg4<-lm(Sales~Income);
summary(myreg4);

#Professor book
#3.1
mat1<- matrix(c(1,1,1,1,1,1,2,3,4,5),nrow=5);
mat1;
tmat<-t(mat1);
tmat;
mat2<-mat1*tmat;
1+4+9+16+25;
55*5-15*15;
2+6+7+9+10;
1*2+2*6+7*3+9*4+50;
11*34-3*34;
121-3*34
sqrt(257477)
Z<-c(1,1,12,10,15);
Z;
zt<-t(Z);
z_t<-t(zt);
z_t;
z_t*Z;

#3.2
mat2<-matrix(c(1,1,1,1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1),nrow=4);
mat2;
tmat2<-t(mat2);
tmat2*mat2;
y<-c(110,120,130,140);
tmat2*y;
mulmat2<-tmat2*mat2;
invmat2<-solve(mulmat2);


#3.3
attach Cobb.D;
attach(Cobb.D);
#(a)
output1<-log(output);
capital1<-log(capital);
labor1<-log(labor);
myreg<-lm(output1~capital1+labor1);
summary(myreg);
anova(update(myreg,~1),myreg);
#(c)
newY<-output1-labor1;
newX<-capital1-labor1;
reg=lm(newY~newX);
summary(reg);
anova(reg);


