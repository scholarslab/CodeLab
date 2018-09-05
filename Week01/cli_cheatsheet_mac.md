# Command Line Cheatsheet for MacOS

### SHORTCUTS

| Command | Description |
| ------------- | ------------- |
| `Tab` | Auto-complete files and folder names |
| `Up Arrow`| Scroll through previous commands |
| `Ctrl + A` | Go to the beginning of the line you are currently typing on |
| `Ctrl + E` | Go to the end of the line you are currently typing on |
| `Ctrl + R` | Lets you search through previously used commands |
| `Ctrl + C` | Kill whatever you are running |
| `Ctrl + D` | Exit the current shell |


### SHELL COMMANDS

| Command | Description |
| ------------- | ------------- |
| `pwd` | Print full working path |
| `.` | Current folder |
| `cd [folder]` | Change into a directory |
| `cd ..` | Change directory upwards |
| `ls` | List contents of a directory |
| `ls -la` | List all contents including hidden files |
| `clear` | Clear the view |
| `open [file]` | Opens a file |
| `open .` | Opens the directory |
| `touch [file name]`| Creates a new file |
| `rm [file name]`| Remove a single file |
| `mkdir [directory name]` | Make a new directory |
| `cp [file] [new file/new directory]` | Copy file to file or new directory |
| `mv [file] [new file/new directory]` | Move file into new file or directory |
| `rmdir [directory]` | Remove directory ( only operates on empty directories ) |
| `rm -rf [directory name]` | Force remove a directory and all its contents | 


### ADVANCED COMMANDS
| Command | Description |
| ------------- | ------------- |
| `sudo [command]` | Run command with the security privileges of the superuser (Super User DO) |
| `cp *.js`| Use wildcards to get all files of a certain type when moving or copying|
| `!!` | Use double bang to repeat last command |
| `nano [file]` | Opens file in Terminal editor |
| `q` | Exit |

___

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
