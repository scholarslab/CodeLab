# Week 03 Lesson: Structured Data

## The Limitations of Unstructured Text

When we use virtually any natural language, we don't just use words. We also use a rich array of punctuation marks, spacing, pauses, intonations, and all the accompanying accoutrement of language. Think about the stereotypical telegram message in a movie: there's a lot of use of the word "stop", meaning a period, as in "full stop." Which is interesting, since Morse code actually encodes punctuation, including the period symbol. But instead of using it, the general convention was to spell out the word "stop" in order to have more redundancy because punctuation was so important to the understanding of messages.

[TheAddamsFamily_morse.webm](https://github.com/scholarslab/CodeLab/assets/2342131/b699d2b9-c03c-4340-b30d-f1a3b7f2cc5e)

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

Let's consider a CSV or spreadsheet representing data for job candidates. One candidate to a row, with columns representing common data such as name, contact information, etc. What happens if we add a section for education or work experience? How many columns should we add to represent degrees or previous positions? We can add new columns whenever we have to add a candidate with more degrees or positions than any prior one, but this makes the data more difficult to parse, either as a human or by computer. Each degree or position also has a number of subsidiary fields: the years and place for an educational program or job are properties of those programs and jobs, but every column is functionally a top level field of the candidate.

For more complex data, we need a more robust, and somewhat more verbose form of structured data.

## XML

Tabular data is useful when we have fixed columns and more rigidly consistent data. There are properties that most dogs or bags of coffee or countries share that we can build columns around. But how do we express more data more flexibly? How could we better express arbitrary length lists or "contains"/"child" relationships? XML, eXtensible Markup Language, was created as a means of **serialization**, allowing it to serve as an intermediary between different applications like a *lingua franca*. This has made it a popular basis for many different softwares that need to represent complex data.

XML comprises a set of nested **elements** that comprise opening and closing **tags** that contain a mix zero or more of: **attributes**, text, and child elements.

Let's look at some example XML. I made up the structure and content of this snippet, but the syntax that it follows can be used to describe many different kinds of other structures. The line breaks and spacing/tabs are optional, but they make it easier for humans to read.

```xml
<person id="ssl2ab">
    <name>
        <last>Lin</last>
        <first>Shane</first>
    </name>
    <title>Senior Developer</title>
    <pets>
        <dog name="Rocket">
            <alias>Rocky</alias>
            <alias>Rock Ness Monster</alias>
            <alias>Dimitri Rockmaninoff</alias>
            <alias>Rockminster Fuller</alias>
            <breed>Australian Cattle Dog</breed>
            <breed>Australian Shepherd</breed>
        </dog>
        <dog name="Hazel">
            <alias>Hazelnut</alias>
            <breed>Australian Cattledog</breed>
            <breed>Beagle</breed>
        </dog>
    </pets>
</person>
```

In this XML, "person", "name", "first", "last", etc are all elements. They start with an opening tag (e.g. '<person>') and end with a closing tag (e.g. '</person>'). Here, we can see that the Person element encompasses all the other elements.

"id" is an attribute of the person element. Attributes are defined inside of the opening tag and describe some metadata about the element.

Between the opening and closing tags, we have the element content. Here, we see that "name" is a _child_ element of the person element. Child elements are used to provide subsidiary information about its parent element and are useful for describing more complex structures. Element content can also have simple text, useful for when there isn't a need to further structure its data using children. The "last" and "first" elements inside of "name" contain just text content.

Sometimes, we don't actually need to have any content at all, only attributes or even just the tag itself. In those cases, we can use the convention of the self-closing tag: `<dog name="Rocket"/>`.

We can use multiple elements of the same type inside of an element (e.g. "dog", "alias") but not multiple attributes of the same name in the same tag.

After you've parsed this example XML, you might think to yourself: "this isn't the only way to describe this information!" And you'd be right!

Let's take a look at four different XML structures:

```xml
<person>
    <name>
        <last>Lin</last>
        <first>Shane</first>
    </name>
</person>
```

```xml
<person>
    <lastname>Lin</lastname>    
    <firstname>Shane</firstname>
</person>
```

```xml
<person>
    <name lastname="Lin" firstname="Shane"/>
</person>
```

```xml
<person lastname="Lin" firstname="Shane"/>
```

These four elements all describe the same basic data. Whether you use attributes or child elements or text is often a matter of personal preference. It's not a good idea to cram data into attributes or text where we might benefit from the additional structure provided by child elements. It's also not a good idea to use attributes where the number of attributes may be uncertain or which contains too much data; the "dog" elements in the original example XML is better suited to be elemental children.

## Validation / Parsing

The point of having these well-defined and consistent formats is that computers can both produce and read them back in. We will usually define the structures of these documents manually (e.g. the columns of a CSV or the order and definitions of the elements in XML), but more frequently the actual documents that conform to those structures are produced by computer programs.

The process of reading a text file of a particular format into a way that is legible to a computer (which we might anthropomorphize as "understanding" the file) is called parsing and the software that does this is a parser. We can write our own parsers for some of these formats easily enough, but there are enough edge cases and this is a common enough of a problem that we should use one of the many parsers available to us. In Python, there are CSV and XML parsers built into the language (and also for some other formats).

When we write formatted text by hand, it's easy to make mistakes. When we have to keep track of nested tags or complex arrangements of escape characters, it helps to have mechanical assistance. Validators and linters are related software tools to help check the syntax and, in some cases, the style of formats. When we use these tools, they help us ensure that our documents are *well-formed*, meaning that they conform to the basic rules of the format (e.g. every XML element is closed). But well-formedness only ensures that a computer can unambiguously read the document, not that it'll make sense to a human.
