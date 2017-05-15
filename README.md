# gwc-survey

This repository is a collection of the code you need to run the Girls Who Code survey for recruitment purposes. 

This survey is written in python and YAML languages. Currently, the survey is meant to be taken in a command line terminal (such as cygwin). Users will simply run the program and enter in their letter choices directly into the terminal, and will recieve an output at the end after all of the answers are computed.

Eventually, this survey can be integrated online, using more complicated programming techniques and languages. 

## Here's what you need to get started: 
 (note: These instructions are for windows OS only. Mac OS instructions coming soon)

There are a lot of things you will need to download and set up onto your computer in order to run this code efficiently.

First, make sure you have downloading permissions on the computer you are using. 
(Avondale's school computers do not have this permission. Consider using a personal computer or asking your club advisor for more assistance with this.)

Next, you will need to download an interactive terminal. Here, I will instruct you in how to download and use Cygwin. 

Use [this website](https://cygwin.com/install.html) in order to install Cygwin. It walks you through the process of setting it up on your PC. 

Note that according to this [FAQ answer](https://cygwin.com/faq.html#faq.setup.what-packages) you will want to add additional packages including the python, pip, and git packages. These will be used to get and run the code. [Here's a video](https://youtu.be/hh-V6el8Oxk) that walks through the whole setup process and how to get packages. Make sure you get the package `git-2.12.2-1`, all python packages, and pip packages.

Once you have cywin installed on your computer, you will have a home directory set up. To get the code, you will need to clone the github repository. If you want to make additions to the repository, you will need to make a github account. If you just want to get the code, there's no need to get an account.

To get the code, type `git clone https://github.com/riya99gupta/gwc-survey.git` in cygwin. This will create the folder `gwc-survey` on your computer with the code for the project. You can see it by typing `ls` in cygwin. This will display all the files and folders in your current folder.

To go into the `gwc-folder`, type `cd` in Cygwin. Now type `ls` again. This should show you the files in the project. You should see the names `survey.py`, `fun.yaml`, `LICENSE`, and `README.md`.

You will need a special library called `PyYAML` in order for python to understand yaml files. You can do this by typing `pip install PyYAML` in Cygwin.

Then, you can run the project by typing `python survey.py` in the terminal, which will start up a new survey. You can either take the whole survey or press `CTRL+C` to stop the program. (If you do this, you might get some weird output which you can ignore.)

To open and edit the files in the project, you will need to use a program called a text editor. This allows you to edit the code, which are basically just text files. Windows has a program notepad that's designed to do this, but you could use other ones such as [Sublime Text](https://www.sublimetext.com/3) which gives you helpful syntax highlighting. Click on the link to go to the download page. It includes instructions on how to download. 

You will find the files in the folder where Cygwin was installed. For me, this was in C://cygwin64/Users/Riya/gwc-survey/ . You can open up this path in Sublime or another text editor.

If you are interested in contributing the changes you make to the files and improve the code, you will need to get a github account as mentioned above. You can get the account for free. Then, use this [git tutorial](https://try.github.io/levels/1/challenges/1) to understand how you can upload your improved code to the "cloud" or the master copy of the code. 

Instructions on exactly how to make changes to the code, like how to write in YAML and python and what pieces to change, are included as comments directly in the code. 


If you need any additional help, Google is always a fantastic resource. It can clear up any questions you may have on how to use specific attributes or how to navigate. Also, if you still need additional assistance, you can contact me via email at riya99gupta@gmail.com. 