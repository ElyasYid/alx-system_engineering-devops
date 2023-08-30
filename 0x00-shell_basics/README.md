0, prints the absolute path name of the current working directory
#!/bin/bash
pwd

1, Display the contents list of your current directory
#!/bin/bash
ls

2, Changes the working directory to the user’s home directory.
#!/bin/bash
cd ~

3, Display current directory contents in a long format
#!/bin/bash
ls -l

4, Display current directory contents, including hidden files (starting with .)
#!/bin/bash
ls -al

5,Display current directory contents
#!/bin/bash
ls -al

6,Create script that creates a directory named my_first_directory in the /tmp/ directory.
#!/bin/bash
mkdir /tmp/my_first_directory/

7,Move the file betty from /tmp/ to /tmp/my_first_directory.
#!/bin/bash
mv /tmp/betty /tmp/my_first_directory/betty

8,Delete the file betty.
#!/bin/bash
rm /tmp/my_first_directory/betty

9, Delete the directory my_first_directory that is in the /tmp directory.
#!/bin/bash
rm -rf /tmp/my_first_directory

10,Write a script that changes the working directory to the previous one.
#!/bin/bash
cd -

11,Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
#!/bin/bash
ls -la . .. /boot 

12,Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
#!/bin/bash
file /tmp/iamafile

13,Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
#!/bin/bash
ln -s /bin/ls __ls__

14,Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
#!/bin/bash
cp -u *.html ..

15,Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
#!/bin/bash
mv [[:upper:]]* /tmp/u

16,Create a script that deletes all files in the current working directory that end with the character ~.
#!/bin/bash
rm *~

17,Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
#!/bin/bash
mkdir -p welcome/to/school

18,Write a command that lists all the files and directories of the current directory, separated by commas (,).
#!/bin/bash
ls -xamp

19, Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
0 SCHOOL School data
!:mime School
