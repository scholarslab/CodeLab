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

~Two assignments this week, each with bonus sections. Focus on completing the main part of each assignment before worrying about bonus functionality.~

For homework this week, complete the [whiteboard exercise](whiteboard_exercise.md) that we started in class. Finish writing out the logic and then try coding it. Remember to start out simple and then get more complex.

We also have two assignments this week. Assignment 2 is pretty close to whiteboard exercise so don't worry if you don't quick complete it. Each of the assignments also have bonus prompts that you should only try to complete if you complete both assignments and the whiteboard exercise.

##### Assignment 1
This is the first few lines from Project Gutenberg version of Jane Austen, which you can find [here](https://www.gutenberg.org/files/1342/1342-0.txt).

'The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 *** START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE *** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'


We want to use this text, but we need to get rid of some of the metadata at the beginning and we want to replace some of the data. Create a script called `jane_austen_data_munging.py`

1. First save this text into a variable called `jane`

1. Figure out how to get rid of everything before `Produced by Anonymous Volunteers` and save everything after in a variable called `jane_cleaned` (**hint: check out the string method [split()](https://www.w3schools.com/python/ref_string_split.asp), it splits strings on certain characters and returns a list *** )

1. Replace all instances of `man` with `person`, and `wife` with `parther` in `jane_cleaned` (**hint: check out the string method [replace()](https://www.w3schools.com/python/ref_string_replace.asp)**)

BONUS:
4. Change your script so that you can give an input, and replace any word in the text with any other word. Output the changed text. 

##### Assignment 2

Famous Canadians 🍁

As a Canadian, I like to talk a lot about famous Canadians. Here's a website with lots of Canadians [https://www.biography.com/people/groups/famous-canadians](https://www.biography.com/people/groups/famous-canadians)

But I have some favorites that I want to have on hand quickly. Here's my quickie list with their names, birth year, death year, and their professions (but not everyone has values for those attributes).

Celine Dion, 1968, performer, goddess

Drake, 1986, performer

Justin Trudeau, 1971, Prime Minister, snowboard instructor

Sandra Oh, 1971, actor, goddess

Nathan Fillion, 1971, actor

John A. Macdonald, 1815, 1891, Prime Minister


1. Create a script and find the best way to store my famous canadians. You've learned a few ways so far to store information like this so feel free to try a few, but remember go for whatever is easiest and works.

2. Figure out a way to output all the information for a person if you input their profession or name. Remember to use for loops and conditions!

3. Add `nationality` to each person's information and set the value to Canadian, just in case I decide I like people from other countries and want to add them to the dictionary.

**BONUS**
4. Create a way to input any value and return any person that has a match for that value in their information. If no one matches return `There's probably a Canadian that does this`
