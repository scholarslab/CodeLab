# Basic Data Types Review

### Variables
A variable is simply a way to put a label on a piece of data in Python. You assign a value to a variable using the `=` sumbol.

```python
var = 'Hello world'
```
What happens if you try and use a number for your variable?
```python
1 = 'Hello world'
```
You'll get a syntax error 😅! That's because Python has rules for how to name variables.

- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume) | 
- A variable name must start with a letter or the underscore character |
- A variable name cannot start with a number |
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ) |
- Variable names are case-sensitive (age, Age and AGE are three different variables)| 


So our previous example could work if we changed the variable name to:
```python
one_1 = 'Hello World'
```

### Data Types
These variables above all hold *strings*. Strings are sequences of characters that are marked by being in single or double quotations.

Strings are just one of many data types accepted in Python. 

There's also numbers, called *integers*. We can take our variables that we assigned before and assign them their actual numbers.
```python
one = 1
two = 2
```
Once we do this though, our strings that were stored in these variables will be erased!



Python also has a special name for decimal numbers, called *floats*.
```python
one = 1.0
```

What if we decided that we wanted to combine variable one and two? We could use a Python *method* for manipulating variables and data.

1. To join variables together use the `+` symbol, this is called concatenation.

```python
one + two
```
You should see `3.0` as your answer. We just added the data in variable one and two together. 
What would happend if we added variables `var` and `one_1` togther?
```python

var + one_1
```
You should see `Hello worldHello world` as your answer because the strings were concatenated together!


2. Other methods that you can use on integers and floats:
division:
```python
one / two
```

multiplication:
```python
one * two
```

We can also assign a truth value to a variable, called a *boolean*.
```python
var_true = True
var_false = False
```
We can then check if these two variables contain the same truth value.
```python
var_true == var_false
```

In Python `=` is used to assign values to a variable, and `==` is used to check if two variables contain the same value.