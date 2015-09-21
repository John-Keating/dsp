[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

## Scatter Plot
The scatter plot below shows the weight of birth weight against the age of the
mother. The data are taken from the NSFG dataset.


[<img src="img/5_scatterplot_wgt_age" title="Scatter Plot of Weight and Age"/>]

The data points show no linear relationship, or much of any relationship at all
for that matter. In his solution, Downey claims that it shows a weak
relationship, but I must confess that I don't see any (even in the hexplot he
creates).

## Correlation
The Pearson's and the Spearman's correlations are too low for any relationship.
```
Pearson's Corr 0.069
Spearman's Corr 0.095
```
Although, the Spearman's is higher than the Persons, which is weak to skewed
results or outliers, it is far too low for us to assume that there is any
relationship. 

## Percentiles
Perhaps breaking down the weights into interquartile percentiles will elucidate a pattern, as
both measures of correlation rely on a linear relationship. Maybe there is a
non-linear relationship hiding in the data.

[<img src="img/chap07scatter3.jpg" title="Percentiles"/>]

Downey says that the graph appears to show hints of a non-linear relationship.
He writes, "Birth weight increases more quickly
in the range of mother's age from 15 to 25.  After that, the effect
is weaker." I remain unconvinced without any further testing.
