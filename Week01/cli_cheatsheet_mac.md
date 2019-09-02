# Command Line Cheatsheet for MacOS

### TERMINAL SHORTCUTS

| Command | Description |
| ------------- | ------------- |
| `Tab` | Auto-complete files and folder names |
| `Up Arrow`| Scroll through previous commands |
| `Ctrl + A` | Go to the beginning of the line you are currently typing on |
| `Ctrl + E` | Go to the end of the line you are currently typing on |
| `Ctrl + R` | Lets you search through previously used commands |
| `Ctrl + C` | Kill whatever you are running |
| `Ctrl + D` | Exit the current shell |

### PATHS

A [path](https://en.wikipedia.org/wiki/Path_(computing)) is a way to describe file and directory locations in a tree structure. MacOS uses Unix-style path notation, so directories and filenames are separated with a forward slash `/`. In this tree structure, directories can contain other directories or files; the path traverses this structure level by level. 

Paths that begin with a forward slash (e.g. `/usr/bin`) are absolute paths, which means that the first element is at the root (lowest level) of the tree. Paths that begin with a directory or filename are relative paths and will start in the current working directory.

Special path symbols:

| Symbol | Description |
| ------------- | ------------- |
| `.` | Current folder |
| `..` | One directory level up |
| `~` | home directory |

Any command that takes a filename will also allow you to specify the path to that file, e.g. `touch ../file.txt` or `rm /temp/error.log`.

### SHELL COMMANDS

| Command | Description |
| ------------- | ------------- |
| `pwd` | Print full working path |
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
