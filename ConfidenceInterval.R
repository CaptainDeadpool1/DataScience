#Normal
M  = 50
xx = rnorm(M, 175, 2.5)
head(xx)

#Estimate of all CDF
fhat <- ecdf(xx)
plot(fhat)

#Fix x0
x0 = 175
theta_hat = fhat(x0)
theta_hat
abline(v=x0, lwd = 5, lty=3)
curve(pnorm(x,175,2.5), 
      add = TRUE,
      col = "orange",
      lwd = 4)

# This is a simulation, we know the truth
theta = pnorm(x0, mean=175, sd=2.5)
theta

# 1 METHOD: Asymptotic/Approximated Normal CI
alpha = 0.05
se.hat = (theta_hat*(1-theta_hat))/M
zq = qnorm(1-alpha/2)

l.n = theta_hat - zq*sqrt(se.hat) #Lower bound
u.n = theta_hat + zq*sqrt(se.hat) #Upper bound
round(c(l.n,u.n),4) # Realization of our normal CI

abline(h=c(l.n,u.n), col="purple", lwd = 2) # PLOT OF NORMAL Confidence Interval

#TEST: If true the value is inside confidence interval
(theta<=u.n) & (theta >= l.n)

# 2 METHOD: Finite sample / exact Hoeffding based Confidence Interval
thr = sqrt((1/(2*M))*log(2/alpha))
l.h = theta_hat - thr
u.h = theta_hat + thr
round(c(l.h,u.h),4)
abline(h=c(l.h,u.h), col="red", lwd = 2, lty = 2)

### Real Coverage vs Nominal Coverage

n.sim = 1000
alpha = 0.05
result.mat = matrix(NA, nrow = n.sim , ncol = 7)
colnames(result.mat) <- c("est","ln","un","lh","uh","chkN","chkH")
for (i in 1:n.sim){
  # Simulate data
  xx = rnorm(M, mean=175, sd = 2.5)
  
  # Get the ECDF estimate
  fhat = ecdf(xx)
  theta_hat = fhat(x0)
  
  # Build Normal-CI
  se.hat = (theta_hat*(1-theta_hat))/M
  zq = qnorm(1-alpha/2)
  l.n = theta_hat - zq*sqrt(se.hat)
  u.n = theta_hat + zq*sqrt(se.hat)
  
  # Build Hoeff-CI
  thr = sqrt((1/(2*M))*log(2/alpha))
  l.h = theta_hat - thr
  u.h = theta_hat + thr
  
  # Check
  chkN = (theta<=u.n) & (theta >= l.n)
  chkH = (theta<=u.h) & (theta >= l.h)
  
  #SAVE
  result.mat[i,1] = theta_hat
  result.mat[i,2] = l.n
  result.mat[i,3] = u.n
  result.mat[i,4] = l.h
  result.mat[i,5] = u.h
  result.mat[i,6] = chkN*1
  result.mat[i,7] = chkH*1 # Perchè sono true o false perchè False*1 = 0 , True*1 = 1
}

head(result.mat)

# Actual coverage
round(c(mean(result.mat[,6]),
  mean(result.mat[,7])), 3)

# Increasing the sample size (M), the Normal Intervals will keep up with the nominale coverage (95%)
# Increasing the simulazione size (n.size), you get better higher resolution results.
# In general, for a given coverage (1-alpha), we prefer shorter intervals... and we could also check this by Montecarlo

# AVG lenght / Normal
head(result.mat[,"un"]- result.mat[,"ln"])
round( mean(result.mat[,"un"]- result.mat[,"ln"]),3)

# AVG lenght / Hoeff
head(result.mat[,"uh"]- result.mat[,"lh"])
round( mean(result.mat[,"uh"]- result.mat[,"lh"]),3)
