# Code Lab Week 1: Environment Setup

If you're using a Mac, you're most of the way there already. You almost certainly have the shell that we'll be using already (more on what that means later). Python, the programming language we'll be using is already built into your computer. But we'll want to set it up so it works just like we want it to. Follow the **MacOS** track below.

If you're using a Windows machine, there's a few more steps. Hopefully you're using Windows 10 (or later, if you're reading this far, far into the future), otherwise things might be a bit troublesome. If you are, we'll be installing the puzzlingly named Windows Subsystem for Linux (WSL), which is a Subsystem _in_ Windows that provides Linux functionality, not the other way around. It's basically a little Linux computer that runs inside of Windows. It's very cool. We'll be using WSL to run our code and do all our coding work. This isn't necessarily better than developing directly in Windows, but it lets us (Windows, Mac, and Linux users) all be on the same page. Follow the **Windows** track below.

If you're using Linux, I'm going to assume that you know what you're doing. Please let me know if this is a faulty assumption. Install Python 3, pip, and pipenv.

If you're using FreeBSD, MS-DOS, OS/2, Solaris, Sony Playstation 2, Amiga Research OS, Windows CE/Pocket PC, or other unusual or outmoded operating systems, there exist [legacy Python interpreters](https://legacy.python.org/download/other/) across a wide (typically dismal) range of contemporaneity. This paragraph is a funny joke that's just for computer historians; Scholars' Lab support for these platforms is limited.

After all the shell and Python setup is done, you'll install Microsoft Visual Studio Code, which is a free editor that we'll be using to write our code. It's pretty good, but it isn't mandatory.

## MacOS

### Step 0-M: Install Homebrew and Xcode Command Line Tools

* Install [Homebrew](https://brew.sh/) (should also install Xcode command line tools)

### Step 1-M: Install Python and Pip

Mac: [Python 3](https://docs.python-guide.org/starting/install3/osx/), including Pip.

The instructions say to add `export PATH="/usr/local/opt/python/libexec/bin:$PATH"` to `~/.profile`. However, you will probably want to add it instead to `~/.zshrc`. While you're at it, add `export PIPENV_VENV_IN_PROJECT=1` to your .zshrc as well, which will simplify some VS Code integration.

At the end of this step, you should be able to input the command `python3 --version` and have it not return an error.

### Step 2-M:  Install Pipenv

In the terminal, run: `brew install pipenv`

At the end of this step, you should be able to input the command `pipenv --version` and have it not return an error.

### Step 3-M: Visual Studio Code

Unless you have another preference, VSCode is a pretty good code editor.

* Install [VS Code](https://code.visualstudio.com/)
* Install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Step X-M: Customize Zsh (strictly optional)

MacOS has defaulted to Zsh for a while, which is good because I like some of its conveniences. To make it prettier, you can install Oh My Zsh and pick a theme (I rather like the agnoster theme highlighted in the installation instructions, though it will require installing a powerline font).

* [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh)

## Windows

### Step 0-W: Install WSL

* Install the confusingly name [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (WSL2), which is actually a Linux Subsystem *for* Windows.

These instructions walk you through the default installation of the Ubuntu Linux distribution, which is a good choice for us. When you choose a Linux user and password, don't forget what you put in. Now you have mostly-Linux.

The WSL installation processed probably required the use of Powershell. Forget about Powershell for now - whenever we use the command line, we should use a WSL Ubuntu shell, either through the Ubuntu terminal or the built-in VSCode terminal.

### Step 1-W: Install Python and Pip

* WSL comes with Python3, but you still need to install pip. In the Ubuntu terminal, run: `sudo apt-get install -y python3-pip`
   * At the end of this step, you should be able to input the command `pip3 --version` and have it not return an error.
* Install Debian development tools, openSSL, and Python extension headers, run: `sudo apt-get install build-essential libssl-dev libffi-dev python3-dev`

### Step 2-W:  Install Pipenv

In your terminal, run: `pip3 install --user pipenv` (if that doesn't work, try `pip install --user pipenv`)

At the end of this step, you should be able to input the command `pipenv --version` and have it not return an error.

### Step 3-W: Visual Studio Code

Unless you have another preference, VSCode is a pretty good code editor.

* Install [VS Code](https://code.visualstudio.com/)
* Install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Install the [Remote WSL extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
* Install the [Remote Development Pack for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

### Step 4-W: The WSL file system

WSL is like a separate computer inside of Windows. Which means that it has its own little corner of your hard drive that's a little hard for other Windows software to access. Makes it difficult to, for example, download a meme gif from your browser and add it to your codelab working directory. For this reason, I suggest going the other way and accessing the Windows file system through WSL. Hard drives in Windows are mounted in WSL at `/mnt/c/` where "c" can be any drive letter. For CodeLab, I recommend setting up a directory in Windows to store your files and then creating what's called a symbolic link (basically a shortcut) in WSL to more easily access it.

For example, if you create a `codelab` directory on your root C drive, it will show up in WSL under `/mnt/c/codelab/`. We can enter this commend in the WSL terminal under your home directory (`~/`) to create the link: `ln -s /mnt/c/codelab codelab`. After this, you'll be able to access your code directory from your home directory with a simple `cd codelab`.

### Step X-W: Switch from Bash to Zsh (strictly optional)

This isn't really necessary and the process is more convoluted than anything we've done so far, but it results in a much prettier terminal that has some nice conveniences.

* Follow [these instructions](https://pascalnaber.wordpress.com/2019/10/05/have-a-great-looking-terminal-and-a-more-effective-shell-with-oh-my-zsh-on-wsl-2-using-windows/).
* I recommend setting up [Windows Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701) or just the VSCode integrated terminal instead of using the default Ubuntu Terminal.
