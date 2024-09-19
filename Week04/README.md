# Week 4: Version Control

![Rocky!](assets/rocky_popcorn.jpg)

## Lesson

[Git for Humanists](https://shane-et-al.github.io/git_slab/)

![Git workflow by Molly Nemerever: https://dev.to/mollynem/git-github--workflow-fundamentals-5496](assets/git_workflow.avif)

1. Review Codelab to this point
2. How to collaborate digitally?
3. Version Control Systems
4. Git and Github

* **Clone/Fork**: A version control operation to create a duplicate repository. In Git, "clone" is the command to duplicate a repository to your local computer; in Github, fork is the mechanism to duplicate a repository to your own Github account. These are functionally the same. Forking has a more permanent implication in traditional version control systems, but it can be much more transient in Git.
* **Commit**: A set of changes that can be referenced later (and reverted or reverted to). We can think of a commit as a milestone or version of a repository. It should be organized such that the change itself is legible (ideally, a specific and interrelated set of updates and not just a disordered mess of revisions) and the state of the repo it represents is sensible (in that the state is comprehensible if you ever have to go back to it).
* **Git**: The most popular version control system in use today and the software command (`git`) used to interact with it.
* **GitHub**: A website and web service that hosts and manages git repositories online. Often used as the canonical, remote repository to coordinate the work of individuals local repositories. Purchased by Microsoft in 2018, to much hand-wringing.
* **Merge**: An important version control function, which multiple, concurrent changes to the same file to be rectified. A file that cannot be automatically rectified is said to be in a "merge conflict."
* **Repository** ("repo"): The basic data store that contains all the files for a particular project.
* **Staging**: In Git and other similar version control systems that use changesets, we explicitly stage specific files that we intend to be part of a commit before committing them. In git, the command to stage a file is `git add <filename/directory>`. Wildcards are allowed (e.g. `git add *`). We can stage all updated files that git is tracking already (i.e. older versions of the files are already in git) using the -p flag: `git add -p`).
* **Version Control**: A software system that allows programmers (and other people who work with digital files) to track their work and collaborate with others by providing Concurrency (maintaining consistancy despite multiple editors), Reservibility (keeping track of changes and allowing work to be undone), and Annotation (describing changes through labels, timestamps, and author information).

---
## Homework for Week 4

## Do:

1. Sometime during the week, add another question to the [icebreaker git practice document](https://github.com/scholarslab/gitpractice/blob/master/Praxis2023.md) and answer all the previous, unanswered questions.