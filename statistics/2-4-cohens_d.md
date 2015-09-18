#Question 1 Cohen's D

[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```  markdown
Exercise 4   Using the variable totalwgt_lb, investigate whether first babies
are lighter or heavier than others. Compute Cohen’s d to quantify the difference
between the groups. How does it compare to the difference in pregnancy length?
``` 

From the chapter we see that the difference in pregnancy length, as measured by
Cohen's D, is *0.028. Downey concludes correctly that this is such a slight
difference as to have no practical effect, assuming that such a difference
actually exists.  

I ran the code below comparing the weight of first-born children and children who were not first-born using Cohen's D as a measure of effect size.

```import nsfg
import thinkstats2 as ts
import pandas as pd

# Read in the pregnancy data, select live births,
# create series of first babies and others

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

first = live[live.birthord == 1]
other = live[live.birthord != 1]

first_wgt = first.totalwgt_lb.dropna()
other_wgt = other.totalwgt_lb.dropna()

CohenD = ts.CohenEffectSize(first_wgt, other_wgt)

print 'The Cohen\'s d between the weight of first born and later births is\
    %.3f' % CohenDpython
```
The result was *-0.089*, which, though greater than the effect size we saw
comparing pregnancy length, is so small as to lack any significance in the real
world. Normally, we expect a Cohen's D of *0.5* before there is an obvious
difference between two means. 

All of this is assumes that the difference exists. Cohen's D is a measure of
effect size but it does not determine whether the difference we are looking at
is significant. The Cohen's D of pregnancy length and birth weight observed in
this data could well be the results of chance. Other tests, such as student's t
test are needed to determine whether it is significant or not.
