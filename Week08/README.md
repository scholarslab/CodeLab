# Week 8
![https://media.giphy.com/media/3otOKBLWSUYaOlxe12/giphy.gif](https://media.giphy.com/media/3otOKBLWSUYaOlxe12/giphy.gif)

## Agenda
- Review homework.
- [Imports and modules](lesson.md) 
- pip, pipenv

## Assignment

#### Part 0.A:

Once upon a time, we talked about different ways to sort a list of numbers. There were good ways and bad ways. And some really, really bad ways. One really, really bad way is to just kind of throw all the numbers up in the air, figure out whether or not the resulting scramble was sorted, and then just redo it if it isn't. Now that you guys are all random number masters, let's try to implement that sorting algorithm outselves.

Write a function to receive a list of integers and sort them using Python's random module. `import` statements can technically go anywhere, but it's usually a good practice to keep them at the top of the file, so you have access to it anywhere in your code.

Remember that since we're mixing up the list *randomly*, it can potentially run an infinite number of times. We should construct our loops accordingly and use statements like `continue` and `break` wisely.

```python
#import statement goes here
def random_sort(nums):
  #your code here
  return sorted_nums

random_sort([7,4,2,7,8,1])
```

This algorithm is actually one variation of the famous ["bogosort"](https://en.wikipedia.org/wiki/Bogosort) (AKA stupidsort, shotgunsort, monkeysort) sorting algorithm.

#### Part 0.B

Is that a bad way to sort? How do we prove it? Write the same kind of sort function using one of [Python's built-in sorting mechanisms](https://docs.python.org/3/howto/sorting.html).

```python
def good_sort(nums):
  #python sort
  return sorted_nums
```

Now, save both sorts as different .py files and run both sorts through the command line tool `time`. Instead of running something like `python3 random_sort.py`, you can run `time python3 random_sort.py` and it'll tell you how long it took to run. For example, running it took me 0.075 total seconds to start up Python, load the dog name script I wrote, and then perform the dog name generation.

```
~/projects/sandbox > time python dog_names.py
['Sammy', 'Thor', 'Bear', 'Lulu', 'Rex', 'Sparky']
python dog_names.py  0.04s user 0.01s system 74% cpu 0.075 total
```

Most of this time is spent loading Python and the script and printing the output to the screen. If I generate 600 names instead of 6, it still only takes 0.104 seconds in total.

Let's see how fast the good and bad sorts are by using `time` from the command line to run each script. Make sure that your scripts run correctly for a small list (5) before trying it for larger ones. The bad sort can... take a while. Now, try the scripts with lists of 9, 10, and 11 numbers. The times for the bad sort will vary depending on sheer luck, because we're depending on random chance. The times for the good sort will vary much less, because it's just up to the vagaries of your computer and whatever else is running on it.

