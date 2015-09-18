[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# The Paradox of Class Size
The paradox of class size occurs when a random sample of respondents in a
population report membership of a group that disproportionally favor large
groups over smaller ones. Members of larger groups, e.g.,
students in large classes at a school, tend to be overrepresented in the sample
relative to fellow students in smaller classes. This occurs because the members
of larger groups within a population have a greater chance of appearing within
the sample.

## Creating Bias
The NSFG pregnancy data can illustrate this paradox. Although the survey
produces an unbiased number of children per household, because pregnancy
determines the sample, not self reporting by children, we can imagine a survey
produced by asking children to report their family size using the function below.

``` python
# This code is taken from Downy, Alen, Think Stats, 2nd edition

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```

By multiplying the number of children in a family by the size of children by the size of
the family, BiasPmf simulates the paradox of class size; i.e., it will give the
same probabilities as if we had asked children at random to report their family
size.

## The Distributions
Below is a graph of the probabilities of each family size as reported in the
NSFG data:

[<img src="img/2_unbiased_children.png" title="Unbiased No. of Children"/>]

``` python
import thinkstats2 as ts

children_PMF = ts.Pmf(resp.numkdhh)
import thinkplot as tp

tp.Pmf(children_PMF, label='numkdhh')
tp.Show()
```


``` python
import thinkstats2 as ts

children_PMF = ts.Pmf(resp.numkdhh)
import thinkplot as tp

tp.Pmf(children_PMF, label='numkdhh')
tp.Show()
```

The graph below compares the NSFG probability distribution with one the same
data passed through the `BiasPmf()` functions.

[<img src="img/2_biased_children.png" title="Unbiased and Biased No. of Children"/>]

It is clear that the central tendency of the biased distribution has shifted to the
right of graph favoring larger families.

## The Means
The means of the two graphs also make this clear.
Number of children: 1.02
Biased number of children: 2.4

