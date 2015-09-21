[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

## Standard Error and Confidence Intervals for Exponential Distributions

I used Downey's code for creating sample exponential distributions (Downey,
2015, p. 105). I renamed it _expo_estimate_ and ran it 3 times with a sample
size of 10, 30 and 80.

expo_estimate(10, 1000)
rmse L 0.793
rmse Lm 1.781
mean error L 0.218
mean error Lm 0.673
con intvs at 90% 1.436 to 3.157

expo_estimate(30, 1000)
rmse L 0.395
rmse Lm 0.619
mean error L 0.062
mean error Lm 0.19
con intvs at 90% 1.603 to 2.572

expo_estimate(80, 1000)
rmse L 0.229
rmse Lm 0.349
mean error L 0.029
mean error Lm 0.079
con intvs at 90% 1.757 to 2.325

These results clearly demonstrate how increasing sample size reduces the
standard error, which makes the predictions more accurate, and narrows the
confidence intervals, which means we have a narrower range for the true mean
of the population. 
