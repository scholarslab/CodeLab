# Week 2
![Git merge dot gif](assets/gitmerge.gif)

## Outline
1. Discuss working with the command line (recent [twitter thread](https://twitter.com/sam___tsao/status/1563828152714924032))
2. [Git for Humanists](https://shane-et-al.github.io/git_slab/)
3. Introduction to programming (offline edition)

## New Terms
* **Algorithm**: An unambiguous and well-defined set of instructions. A computer program is an algorithm, but so is a cookbook recipe. There's really nothing special about algorithms, nothing inherently mysterious or sinister. The algorithm is a simple idea, but computers have allowed them to grow to incomprehensible levels of complexity.
* **Clone/Fork**: A version control operation to create a duplicate repository. In Git, "clone" is the command to duplicate a repository to your local computer; in Github, fork is the mechanism to duplicate a repository to your own Github account. These are functionally the same. Forking has a more permanent implication in traditional version control systems, but it can be much more transient in Git.
* **Git**: The most popular version control system in use today and the software command (`git`) used to interact with it.
* **GitHub**: A website and web service that hosts and manages git repositories online. Often used as the canonical, remote repository to coordinate the work of individuals local repositories. Purchased by Microsoft in 2018, to much hand-wringing.
* **Merge**: An important version control function, which multiple, concurrent changes to the same file to be rectified. A file that cannot be automatically rectified is said to be in a "merge conflict."
* **Programming Language**: A particular kind of computer code in which programs are written. There are other kinds of computer languages (such as markup languages like HTML that are used to describe a document); programming languages instruct a computer to ingest input, produce output, manipulate data, calculate equations, and the such. Many thousands of programming languages exist, often tailored for specialized applications or types of computers.
* **Python**: One popular programming language originally released in 1991. Python is extremely common in digital humanities and adjacent fields like data science because it is easy for non-programmers to learn and has a large library (both built-in and third-party) to perform common tasks. Python 3 is the current major version, which is not completely backward-compatible with the long-running previous version, Python 2.
* **Repository**: The basic data store that contains all the files for a particular project.
* **Version Control**: A software system that allows programmers (and other people who work with digital files) to track their work and collaborate with others by providing Concurrency (maintaining consistancy despite multiple editors), Reservibility (keeping track of changes and allowing work to be undone), and Annotation (describing changes through labels, timestamps, and author information).


## Brandon's Corner
Digital humanities work is messy, both because of the scale at which it typically takes place and because of the state in which we find many of our materials. The foundational concepts covered in these early weeks regarding the command line will begin to make a range of materials available to you that would not otherwise be possible. And an array of tasks that might not otherwise be feasible to carry out by hand will become doable for your research. In particular, the command line lets you automate on a broad scale a variety of tasks that might otherwise require a special tool. James Baker and Thomas Padilla collected a variety of them useful for working with digital primary sources in a tool called the sourcecaster for use by humanists and archivists. Things like…

* extract all text from a series of images
* remove all punctuation from a document
* download a series of web-based documents from a list

These sorts of activities are foundational to all types of digital humanities work. While you might be able to find a specialized tool for some of them, knowing your way around the command line to help with them can help you design purpose-built things for your own needs. You'll be better to fit your research to the materials and tasks that actually interest you rather than only use the formats and datasets that others provide. 

---

!["Hazel!"](assets/hazel_porch.jpg)

## Homework for Week 2

### Assignment 1: Git Practice

##### Note to Current Shane from Past Shane: remember to give the new Praxis cohort GitHub team edit permissions for this repo.

I've created a git repository on the Scholars' Lab account that has a markdown text file for your Praxis cohort at [https://github.com/scholarslab/gitpractice/blob/master/Praxis2022.md](https://github.com/scholarslab/gitpractice/blob/master/Praxis2022.md). Hopefully, you should have access to this repository by now. Clone this file to your computer, answer the two original seed questions, then add a new question of your own for your fellows to answer. Check back later in the week for new questions and answer them so that, hopefully, by the time we meet again, we'll have a fully-filled-out and, let's say, quixotically personal questionaire for the entire cohort.

### Assignment 2: Create your own homework repo

Create a new repository on Github to hold your own homework assignments. Let's call it "codelab-assignments" for consistency. This should be under your account (rather than the Scholars' Lab's account). Click the Github cat on the top left, and then the green "New" button under the "Recent Repositories" menu on the left. It's easier to create a new repo on Github (the website), and then clone it to your computer, but you can also try doing an in-place `git init` if you're feeling adventurous.

### Assignment 3: 

Describe, in exacting detail, the algorithm to give exact change. You should only assume basic arithmetic functions like addition and subtraction, but be sure to describe how to figure out what notes and coins to give back. Write this down in a new markdown file with the file extension .md (don't worry about formatting) in a Week 2 directory in your homework repo and commit/push it.

### Read:
Raymond, Eric S. [The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/cathedral-bazaar/index.html): Introduction through "How Many Eyeballs Tame Complexity"

(I think Raymond is a bad person with bad views, but his software development work and this particular text were very influential in the Free Software community and useful to understand it in historical context.)
