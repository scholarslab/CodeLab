# Structured Data

## The Limitations of Unstructured Text

When we use virtually any natural language, we don't just use words. We also use a rich array of punctuation marks, spacing, pauses, intonations, and all the accompanying accoutrement of language. Think about the stereotypical telegram message in a movie: there's a lot of use of the word "stop", meaning a period, as in "full stop." Which is interesting, since Morse code actually encodes punctuation, including the period symbol. But instead of using it, the general convention was to spell out the word "stop" in order to have more redundancy because punctuation was so important to the understanding of messages.

![Morse code in The Addams Family (1991)](assets/TheAddamsFamily_morse.webm)

Punctuation and spacing are pretty important for most natural languages. The standard joke about comma usage is the difference between "Let's eat, Grandpa!" and "Let's eat Grandpa!" When we use them, it's often a way to add _structure_ to the linear flow of words, in the most basic sense to help break up clauses so that semantically proximate words are also physically or temporally proximate. Without this structure, we have a stream that must mostly be understood ambiguously through interpretation.

**What are other ways that we structure text? Think about different kinds of documents.**

## Lists

One of the simpliest ways we can structure text is using lists, which is just an ordered, linear collection of items. Let's break that down. Collection, as in there's a set of zero or more items. Ordered, as in there's an order to the elements; the second item comes after the first and before the third. Linear, as in like a line, so there's a single dimension to that order. This one's pretty straightforward, but there's a few wrinkles.

**How do we write out a list? How do we distinguish between different elements?**

We have *elements*, which are the items of a list, and we have what's called *delimiters* which separate them. We can define special characters to act only as delimiters, which are not allowed to be used inside of elements, but in practice we'd rather not define the whole system of our text around the particular implementations. We want to create a *text file*, that is to say a way to structure data using the characters in a text character encoding without having to resort to special data outside of it. This is important because text files are readable by software that implement the particular character encoding without having to know the special, specific rules that we would need to define if we e.g. wanted to have a special marking for delimiters. Text files are also useful because they're also typically much easier to read for humans directly. Files which are only readable with those special rules that put them outside of a standard character encoding (i.e. not text files) are called "binary files." For now and maybe forever, it's more useful to know what those are abstractly than to know how those are constructed. Let's continue with text files.

Since we're making all of this out of the same set of characters, we run into the problem that we'd like to also use the characters we're using as delimiters in our elements. So we have to think of ways to tell people (and computers) when to and when not to take a particular character literally. One way to do this is to treat certain characters, like commas or quotation marks, as special unless we "escape" them (indicate that they're actually just mundane text) by using an **escape character**.

So, for example, maybe we can enclose all our elements with quotation marks:

`"Bofur", "Maple","Rocky"`

And if we need to use quotation marks inside of our elements, we can just double them up:

`"Bofur ""the brave""", "Maple ""the kind""", "Rocky ""the anxious"""`

## CSVs

Now that we have a way to do lists, which are one-dimensional. **How would we turn it into two dimensions? What would that look like?**

Let's make a list of lists by putting each one on a new line:

```
"Dog", "Breed", "Owner"
"Bofur", "corgi", "Ronda"
"Maple", "hound", "Amanda"
"Rocky", "cattle dog", "Shane"
```

So now we have tabular data, data in tables. Which is probably pretty familiar as spreadsheet data. This format, the list of lists, with double quotation mark escape characters, is actually the text file format called Comma Separated Values (CSV). There's also a similar, but less common format called Tab Separated Values (TSV).

These are most often used to move spreadsheet data around outside of the more proprietary and specialized spreadsheet software formats like XLS/XLSX (Excel), so that it can be exchanged between people who use different software or want to read and parse it with code more easily. CSV is a very popular way to exchange [public datasets](https://catalog.data.gov/dataset/?res_format=CSV).

**What are the limitations of CSVs and tabular data in general?**

## XML

Tabular data is useful when we have fixed columns and more rigidly consistent data. There are properties that most dogs or bags of coffee or countries share that we can build columns around. But how do we express more data more flexibly? How could we better express arbitrary length lists or "contains"/"child" relationships?

XML is useful for **serialization**, allowing it to serve as an intermediary between arbitrary formats, like a *lingua franca*.
