# Code Lab Week 1: Environment Setup

## Fundamentals:

**Windows**:
* Activate [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) (WSL)
* Install [Ubuntu 18.04](https://aka.ms/wsl-ubuntu-1804)
Now you have sorta-Linux 

**Mac**:
* Install [Homebrew](https://docs.brew.sh/Installation)

* Install Xcode Command Line Tools, by typing:
```sh
xcode-select --install
```

## Shell
* Install [ZShell (zsh)](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH)
* Install [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh)

## Python
* **Mac**: [Python 3](https://docs.python-guide.org/starting/install3/osx/)
* **WSL**: Comes with Python3, but need to install pip: `sudo apt-get install -y python3-pip` and Debian development tools, openSSL, and Python extension headers: `sudo apt-get install build-essential libssl-dev libffi-dev python3-dev`

* Update Pip: `pip install --upgrade pip`
* Install Pipenv: `pip install --user pipenv`

## Text/Code Editor
* Install [VS Code](https://code.visualstudio.com/)
