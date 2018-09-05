## Practice for Mac 

1. Create the following directory structure in your `workspace` directory.
    ```sh
    workspace
    +-- cli
        +-- practice
            +-- create
    ```
1. `cd` to the `create` directory with one command `cd ~/workspace/cli/practice/create`. Remember to use tab completion.
1. While in this directory, create a new file named `code_lab` in the `cli` directory. Do not `cd` to `cli`, but rather use your navigation abilities. 
    ```sh
    touch ../../code_lab
    ```
1. Put some simple content in the file using the `echo` command.
    ```sh
    echo 'Digital Humanities is ...' > ../../code_lab
    ```
1. Now use the `cat` command to read those contents.
    ```sh
    cat ../../code_lab
    ```
1. Do not change directories, and create a file named `scholars_lab` in the `practice` directory.
1. Remove the `code_lab` file you created earlier with the `rm` command.
1. `cd` back up to the `cli` directory.
1. Remove the `practice` directory and all of its contents.


