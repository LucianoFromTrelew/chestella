# Chestella
A C-Projects "manager" made in Python

### Getting started
All you need to do is install it via pip:

    pip install chestella

Congratulations! You have installed chestella at its latest version

Now you can create your C-Project with the next command:

    chestella init <project-name>
It will create a directory tree with the next structure
```
project-name
│   Makefile
└───src
│   │   project-name.c
└───obj
└───bin
```

# Example

    chestella init my-project
    cd my-project
    make
    ./bin/my-project #OUTPUT: Hello World!

If you want to delete your project, you simply have to type:
	

    rm -rf my-project

And that's it!
