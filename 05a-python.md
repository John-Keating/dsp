# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

> Both lists and tuples are ordered sequences of variables ordered by integers, but tuples are immutable and lists are mutable.

> Lists are created by angular brackets that can contain comma separated variables, while tuples are created by comma separated variables that values that can, but do not need to be, placed within parentheses.

> Tuples can be used as keys for a dictionary because the keys to a dictionary must be immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

> Lists are ordered sequences of variables ordered by integers, while sets are unordered collections of unique elements. Lists can have multiple instances of an element. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

> `lambda` calls an anonymous function. It is normally used as means to create a simple function as an argument to another function. Although it is possible to create a named function for this, `lambda` is a quicker and more concise method.

```
# The test scores of a class is arranged in a list of tuples 
# that each contain the students' name, grade, and gpa.
# The school principle wishes to see the list of students ranked by grade then gpa.

test_results = [('john doe', 'B', 3.01), ...]

print sorted(test_results, key = lambda test_results: (test_results[1], test_results[2]), resverse=True)
```


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

> List comprehension is a concise means for defining the elements of a list by setting the definition within brackets.
> List comprehensions are considered more readible.
```
words = "List comprehension is a concise means for defining the elements of a list by setting the definition within brackets".split

``` python
info = [[w.lower(), w.upper(), len(w)] for w in words]
for i in info:
    print i
['list', 'LIST', 4]
['comprehension', 'COMPREHENSION', 13]
['is', 'IS', 2]
['a', 'A', 1]
['concise', 'CONCISE', 7]
['means', 'MEANS', 5]
['for', 'FOR', 3]
['defining', 'DEFINING', 8]
['the', 'THE', 3]
['elements', 'ELEMENTS', 8]
['of', 'OF', 2]
['a', 'A', 1]
['list', 'LIST', 4]
['by', 'BY', 2]
['setting', 'SETTING', 7]
['the', 'THE', 3]
['definition', 'DEFINITION', 10]
['within', 'WITHIN', 6]
['brackets', 'BRACKETS', 8]
```

``` python
alt_info = map(lambda w: [w.lower(), w.upper(), len(w)], words)
for t in alt_info:
    print t
['list', 'LIST', 4]
['comprehension', 'COMPREHENSION', 13]
['is', 'IS', 2]
['a', 'A', 1]
['concise', 'CONCISE', 7]
['means', 'MEANS', 5]
['for', 'FOR', 3]
['defining', 'DEFINING', 8]
['the', 'THE', 3]
['elements', 'ELEMENTS', 8]
['of', 'OF', 2]
['a', 'A', 1]
['list', 'LIST', 4]
['by', 'BY', 2]
['setting', 'SETTING', 7]
['the', 'THE', 3]
['definition', 'DEFINITION', 10]
['within', 'WITHIN', 6]
['brackets', 'BRACKETS', 8]
```
``` python
info_filter = [w for w in words if w.startswith("c")]
print info_filter
['comprehension', 'concise']
``` 
```python
alt_info_filter = filter(lambda w: w.startswith("c"), words)
print alt_info_filter
['comprehension', 'concise']
```


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





