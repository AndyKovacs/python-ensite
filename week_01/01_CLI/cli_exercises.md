# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
- Move into the CodingNomads folder
- Create new folder cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    c. list the contents of the folder
    d. rename one of the files
- Inside of folder cli_testing, create a new folder
- Copy a file from cli_testing to the new folder
- Move a different file from cli_testing to the new folder
- Demonstrate removing:
    a. A file
    b. A folder


## vim

- Use `$ vim` to write some text inside a file
- Use `$ cat` print contents of file
- Use `$ grep` to search for a word inside file


## explore advanced CLI

- What is the difference between the two commands > and >>?
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
- Overwrite the content of my_file.txt with "tell me"

```bash
week_01 git:(master) ✗ ~
➜  ~ mkdir codingnomads
➜  ~ cd codingnomads 
➜  codingnomads mkdir cli_testing
➜  codingnomads cd cli_testing 
➜  cli_testing pwd
/Users/whitecoffee/codingnomads/cli_testing
➜  cli_testing touch file1.txt
➜  cli_testing touch file2.txt
➜  cli_testing touch file3.txt
➜  cli_testing ls -al
total 0
drwxr-xr-x  5 whitecoffee  staff  160 Feb 22 15:46 .
drwxr-xr-x  3 whitecoffee  staff   96 Feb 22 15:38 ..
-rw-r--r--  1 whitecoffee  staff    0 Feb 22 15:45 file1.txt
-rw-r--r--  1 whitecoffee  staff    0 Feb 22 15:46 file2.txt
-rw-r--r--  1 whitecoffee  staff    0 Feb 22 15:46 file3.txt
➜  cli_testing mv file3.txt file4.txt
➜  cli_testing ls
file1.txt file2.txt file4.txt
➜  cli_testing mkdir newfolder
➜  cli_testing ls
file1.txt file2.txt file4.txt newfolder
➜  cli_testing cp file4.txt
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
➜  cli_testing ls
file1.txt file2.txt file4.txt newfolder
➜  cli_testing cp file4.txt new folder
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvXc] source_file ... target_directory
➜  cli_testing cd newfolder 
➜  newfolder ls
➜  newfolder cd ..
➜  cli_testing cp file1.txt newfolder 
➜  cli_testing ls
file1.txt file2.txt file4.txt newfolder
➜  cli_testing ls newfolder 
file1.txt
➜  cli_testing mv file2.txt newfolder 
➜  cli_testing ls
file1.txt file4.txt newfolder
➜  cli_testing ls newfolder 
file1.txt file2.txt
➜  cli_testing rm file1.txt 
➜  cli_testing rm newfolder 
rm: newfolder: is a directory
➜  cli_testing rm -rf newfolder 
➜  cli_testing man rm       
➜  cli_testing vim
➜  cli_testing vim file5.txt
➜  cli_testing cat file5.txt 
adaskdjakjadn
➜  cli_testing grep file5.txt "adas"
grep: adas: No such file or directory
➜  cli_testing grep "adas" file5.txt 
adaskdjakjadn
➜  cli_testing touch hello.txt
➜  cli_testing cat hello.txt 
➜  cli_testing echo "how?!"   
dquote> q
dquote> 
➜  cli_testing echo "how?" hello.txt
q
how? hello.txt
zsh: command not found: q
➜  cli_testing echo "how"
how
➜  cli_testing echo "how?" >> hello.txt 
q
zsh: command not found: q
➜  cli_testing echo "how" >> hello.txt  
➜  cli_testing cat hello.txt 
how?
how
➜  cli_testing echo "how" > hello.txt 
➜  cli_testing cat hello.txt         
how
➜  cli_testing touch my_file.txt    
➜  cli_testing ls    
file4.txt   file5.txt   hello.txt   my_file.txt
➜  cli_testing hello.txt >> my_file.txt 
zsh: command not found: hello.txt
➜  cli_testing echo hello.txt >> my_file.txt
➜  cli_testing echo "tellme" > my_file.txt
➜  cli_testing cat my_file.txt 
tellme
➜  cli_testing 
```