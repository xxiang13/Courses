#his book
#3.4
attach(EmSalaries);

levels(Gender) #check levels of variable
NewGender = factor(Gender, c("Male","Female"));
NewDept = factor(Dept, c("Sales","Purchase","Advertse","Engineer"));
levels(NewGender);
levels(NewDept);

reg<-lm(log.Salary.~YrsEm+PriorYr+Education+Super+Female+Advertising+Engineering+Sales)
summary(reg)
#b
reg<-lm(log.Salary.~YrsEm+PriorYr+Education+Super+Male+Advertising+Engineering+Marketing)

#b


#c


#d
summary(reg<-lm(log.Salary.~YrsEm+Education+Advertising+Engineering+Sales))

#Textbook
#5.6
attach(Text5.6)
cor(Y, Horsepower);


levels(Country);
NewCountry = factor(Country, c("Other","USA","Japan","Germany"));
NewCountry = gsub("Germany", "Other", NewCountry);
levels(NewCountry)
NewCountry = factor(Country, c("Other","USA","Japan"));
summary(lm(Y~Horsepower+NewCountry,data=Text5.6))

#5.9
attach(text.5.9)
NewD = factor(D, c(0,1,-1));
levels(NewD)
levels(factor(D))
Z= G*I;

summary(lm(V~I+D+W+Z+P+N));

summary(lm(V~+D+Z+I:P));




#after reg, I and Z not significant, don't include in model
summary(lm(V~NewD+Z+N)); #delet I & Z, run reg, but NewD1 becomes non-significant
A=D*W #check if there is a interaction between D & W
summary(lm(V~NewD+A+P+N)) #NewD1 becomes significant and A is significnat, shows there is a interaction
B= D*P
summary(lm(V~NewD+B+P+N)) # can't include B since NewD1, NewD-2 A B all non-significant
C=D*N
summary(lm(V~NewD+factor(W)+C+N)) #C is non-significant, there is no interaction
E = W*G
summary(lm(V~NewD+factor(W)+A+E+P+N)) # E significant, NewD1 become more significant
H <- N*P;B= D*N;C=I*G;E = I*P; X=I*N;

summary(lm(V~Z+NewD+E)) #H significant, P-value of other terms decreases

#5.10
attach(text.5.9)
str(D2);
D1<-c(1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1);
D1;
summary(lm(V~I+D1+D2+W+Z+P+N));

anova(lm(V~I+D+W+G:I+P+N), lm(V~I+D1+D2+W+G:I+P+N))