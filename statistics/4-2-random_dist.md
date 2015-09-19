[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

## Create Random Numbers
I created a list of a thousand random numbers with the following code:
``` python
import random

thousand = [random.random() for x in range(1000)]
thousand_pmf = ts.Pmf(thousand, label = 'rando')
```

## Produce and graph the PMF of the random distribution
``` python
import random

thousand = [random.random() for x in range(1000)]
thousand_pmf = ts.Pmf(thousand, label = 'rando')
tp.Pmf(thousand_pmf, linewidth=0.1)
tp.Show()
```

[<img src="img/3_rando_cdf.png" title="Random PMF"/>]
## Produce and graph the CDF of the random distribution
``` python
thousand_cdf = ts.Cdf(thousand, label='rando')
tp.Cdf(thousand_cdf)
tp.Show()
```
[<img src="img/3_rando_cdf.png" title="Random CDF"/>]
