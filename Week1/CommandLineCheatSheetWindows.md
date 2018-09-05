# Command Line Cheatsheet for Windows


## Aliases and Functions in Bash

### Aliases

Aliases are useful for accelerating your development workflow. You define aliases in your `.zshrc` file with the `alias` keyword. Let's look at an example.

When working with the Git/Github workflow, there are several commands that you type over, and over, and over again. One of those is `git push origin myBranchName`. It becomes tedious to constantly type `git push origin`. Let's create an alias for it.

Open the `.zshrc` initialization file in your favorite code editor, and enter in the following alias.

`alias gpo="git push origin "`

> **Pro tip:** Make sure there are no spaces before, or after, the equals sign in an alias.

Save the file, and reload your init file with the `source` command.

`source ~/.zshrc`

The next time you need to push a local branch to Github, you can use this alias to save yourself a lot of typing.

`gpo myBranchName`



## What is a Shell?

At its base, a shell is simply a macro processor that executes commands. The term macro processor means functionality where text and symbols are expanded to create larger expressions.

A bash shell is both a command interpreter and a programming language. As a command interpreter, the shell provides the user interface to the rich set of utilities for your operating system. The programming language features allow these utilities to be combined. Files containing commands can be created, and become commands themselves. These new commands have the same status as system commands in directories such as /bin, allowing users or groups to establish custom environments to automate their common tasks.

Shells may be used interactively or non-interactively. In interactive mode, they accept input typed from the keyboard. When executing non-interactively, shells execute commands read from a file.

Shells also provide a small set of built-in commands (builtins) implementing functionality impossible or inconvenient to obtain via separate utilities. For example, cd, break, continue, and exec cannot be implemented outside of the shell because they directly manipulate the shell itself. The history, getopts, kill, or pwd builtins, among others, could be implemented in separate utilities, but they are more convenient to use as builtin commands. All of the shell builtins are described in subsequent sections.

While executing commands is essential, most of the power (and complexity) of shells is due to their embedded programming languages. Like any high-level language, the shell provides variables, flow control constructs, quoting, and functions.

Shells offer features geared specifically for interactive use rather than to augment the programming language. These interactive features include job control, command line editing, command history and aliases.

## Videos to Watch

1. [Bash Basics Part 1 of 8 | Access and Navigation](https://youtu.be/eH8Z9zeywq0?t=885)
1. [Beginner's Guide to the Bash Terminal](https://www.youtube.com/watch?v=oxuRxtrO2Ag)
1. [The Most Important Thing You'll Learn in the Command Line](https://www.youtube.com/watch?v=q7-aEspwwEI)
1. Go through the CodeAcademy [command line course](https://www.codecademy.com/learn/learn-the-command-line).
1. [Shell Scripting Tutorial](https://www.youtube.com/watch?v=hwrnmQumtPw)

## Practice

1. Create the following directory structure in your `workspace` directory.
    ```sh
    workspace
    +-- cli
        +-- practice
            +-- create
    ```
1. `cd` to the `create` directory with one command `cd ~/workspace/cli/practice/create`. Remember to use tab completion.
1. While in this directory, create a new file named `foo` in the `cli` directory. Do not `cd` to `cli`, but rather use your navigation abilities. 
    ```sh
    touch ../../foo
    ```
1. Put some simple content in the file using the `echo` command.
    ```sh
    echo 'Foo, I am your father' > ../../foo
    ```
1. Now use the `cat` command to read those contents.
    ```sh
    cat ../../foo
    ```
1. Do not change directories, and create a file named `bar` in the `practice` directory.
1. Remove the `foo` file you created earlier with the `rm` command.
1. `cd` back up to the `cli` directory.
1. Remove the `practice` directory and all of its contents.

## Aliases

1. To make a new branch with git, you use the command `git checkout -b branchName`. Make an alias for yourself to save on typing.
1. Likely the most used git command is `git status`. Alias it as `gs`.

## Functions

1. Another process that is done many times during the course is initializing a new git repo on your machine.

    ```sh
    git init
    git remote add origin GithubRemoteURL
    touch .gitignore
    ```

    Make a function that automates this for you, where you simply type in the function name followed by the new repo URL.
1. Once you have that working, augment the function to autopopulate the `.gitignore` with standard files and functions that should be ignored with the `echo` command.

### SHORTCUTS

| Command | Description |
| ------------- | ------------- |
| `Tab` | Auto-complete files and folder names |
| `Up Arrow`| Scroll through previous commands |
| `Ctrl + A` | Go to the beginning of the line you are currently typing on |
| `Ctrl + E` | Go to the end of the line you are currently typing on |
| `Ctrl + R` | Lets you search through previously used commands |
| `Ctrl + C` | Kill whatever you are running |
| `exit` | Exit the current shell |


### SHELL COMMANDS

| Command | Description |
| ------------- | ------------- |
| `cd` | Print full working path |
| `dir` | List contents of a directory  |
| `chdir [folder]` | Change into a directory |
| `cd ..` | Go one directory up |
| `cls` | Clear the view |
| `open [file]` | Opens a file |
| `open .` | Opens the directory |
| `touch [file name]`| Creates a new file |
| `del [file name]`| Remove a single file |
| `mkdir [directory name]` | Make a new directory |
| `copy [file] [new file/new directory]` | Copy file to file or new directory |
| `move [file] [new file/new directory]` | Move file into new file or directory |
| `rmdir [directory]` | Remove directory ( only operates on empty directories ) |
| `rmdir /s [directory name]` | Force remove a directory and all its contents | 
| `help` | Prints all possible commands | 


### Advanced Commands
| Command | Description |
| ------------- | ------------- |
| `sudo [command]` | Run command with the security privileges of the superuser (Super User DO) |
| `cp *.js`| Use wildcards to get all files of a certain type when moving or copying|
| `edit [file]` | Opens file in Terminal editor |
| `exit` | Exit |

