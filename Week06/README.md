# Python FUNdamentals
 
Agenda:
- Welcome Back Zoe & Shane does a quick review of last week's homework (don't worry next week will be all about Classes)
- Review of data structures 
- Introduce a new data structure
- Whiteboard exercise
- Live code our whiteboard

Reminder:
- Ask questions
- Ask for help
- And write code as much as possible!

#### HOMEWORK
![https://media.giphy.com/media/3o7TKGMZHi73yzCumQ/giphy.gif](https://media.giphy.com/media/3o7TKGMZHi73yzCumQ/giphy.gif)

Two assignments this week, each with bonus sections. Focus on completing the main part of each assignment before worrying about bonus functionality.

##### Assignment 1
```python
jane = 'The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 [EBook #1342] Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
'
```
In the `jane` variable, is the first few lines from Project Gutenberg version of Jane Austen, which you can find [here](https://www.gutenberg.org/files/1342/1342-0.txt).

We want to use this text, but we need to get rid of some of the metadata at the beginning and we want to replace some of the data. Create a script called `jane_austen_data_munging.py`

1. Figure out how to get rid of everything before `Produced by Anonymous Volunteers` and save everything after in a variable called `jane_cleaned`
2. Create a variable called `jane_sort` and store the words in `jane_cleaned` in alphabetical order
3. Replace all instances of `man` with `person`, and `wife` with `parther` in `jane_cleaned`

BONUS:
4. Change your script so that you can replace any word in the text with any other word. 

##### Assignment 2

