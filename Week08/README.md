# Week 8
![https://media.giphy.com/media/3otOKBLWSUYaOlxe12/giphy.gif](https://media.giphy.com/media/3otOKBLWSUYaOlxe12/giphy.gif)

## Agenda
- Review homework.
- [Imports and modules](lesson.md) 
- pip, pipenv

## Assignment

### Part 0.A:

Once upon a time, we talked about different ways to sort a list of numbers. There were good ways and bad ways. And some really, really bad ways. One really, really bad way is to just kind of throw all the numbers up in the air, figure out whether or not the resulting scramble is sorted, and then just redo it if it isn't. Now that you guys are all random number masters, let's try to implement that sorting algorithm outselves.

Write a function to receive a list of integers and sort them in this inefficient way using Python's random module. `import` statements can technically go anywhere, but it's usually a good practice to keep them at the top of the file, so you have access to it anywhere in your code.

Remember that since we're mixing up the list *randomly*, it can potentially run an infinite number of times. We should construct our loops accordingly and use statements like `continue` and `break` wisely.

```python
#import statement goes here
def random_sort(nums):
  #your code here

random_sort([7,4,2,7,8,1])
```

This algorithm is actually one variation of the famous ["bogosort"](https://en.wikipedia.org/wiki/Bogosort) (AKA stupidsort, shotgunsort, monkeysort) sorting algorithm.

### Part 0.B

Is that a bad way to sort? How do we prove it? Write the same kind of sort function using one of [Python's built-in sorting mechanisms](https://docs.python.org/3/howto/sorting.html).

```python
def good_sort(nums):
  #python sort
  return sorted_nums
```

Now, save both sorts as different .py files and run both sorts through the command line tool `time`. Instead of running something like `python3 random_sort.py`, you can run `time python3 random_sort.py` and it'll tell you how long it took to run. For example, running our dog names script took me 0.075 total seconds to start up Python, load the script, and then perform the dog name generation.

```
~/projects/sandbox > time python dog_names.py
['Sammy', 'Thor', 'Bear', 'Lulu', 'Rex', 'Sparky']
python dog_names.py  0.04s user 0.01s system 74% cpu 0.075 total
```

Most of this time is spent loading Python and the script and printing the output to the screen. So if I generate 600 names instead of 6, it still only takes a little bit longer (0.104 seconds).

Let's see how fast the good and bad sorts are by using `time` from the command line to run each script. Make sure that your scripts run correctly for a small list (say, with 3 or 4 numbers) before trying it for larger ones. Now, try the scripts with lists of 9, 10, and 11 numbers. The random sort can... take a while to do this. How much longer  will vary depending on sheer luck, because we're depending on random chance, after all. The times for the good sort will vary much less, because the people who wrote Python are pretty smart.

#### slight bit of really unnecessary math detail ahead ####

If we want to be real big (and, for DHers, really unnecessarily big) nerds, we can see that every additional number in a list that we try to sort using a bogosort increases the average number of random shuffles by a multiple of that length. So, the average number of shuffles for a list of `n` length is the factorial of `n`: `n!`. As the length of the list increased from 9 to 10, we had to do, on average, 10 times more sorts. This is a curve that goes up *real* quick.

A computer scientist would say that this algorithm has an average *time complexity* of `O(n!)`, a best-case of O(n) (because if might already be sorted and we can verify it by reading through the list once), and a worst-case of the never, because if we're *really* unlucky, we'll just never shuffle into the right order. To compare, the built-in Python sort, which uses the [timsort](https://en.wikipedia.org/wiki/Timsort) algorithm, has an average time complexity of `O(n log n)`, which is about as good as it gets for a generalized sorting algorithm.

Here's how `n!` diverges from `n log n` for even small values of n:

![factorial vs n log n](assets/efficiency.png)

(thanks, [Wolfram Alpha](https://www.wolframalpha.com/input/?i=plot+y+%3D+x%21%3B+y+%3D+x+log+x+from+x+%3D+0+to+7))

The blue line is the bogosort's `n!` performance, the red is Python's `n log n` performance. They both start out small, but the blue line quickly splits off from the red and just zooms up into the stratosphere. This is why we can easily sort large (length 10000+) lists of numbers using Python's built-in sort, but bogosort just completely chokes much beyond a dozen or so.

Congratulations on still reading this. You basically have a named chair in computer science at this point.
