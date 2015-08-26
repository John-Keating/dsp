# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. `pushd` + path  - Hurtle down a path

2. `popd` - back to where you pushed from

3. `cp -r` - copy a directory with firles

4. `rm -rf` - recursivly delete files from a directory

5. `find . -name *.txt -print` - finds and prints all text file names in the current directory
> save the above filenames to a file: add `add > textfiles.txt`

6. `cat > newfile.txt` - start typing and text will be saved to the newfile
> NB: CTRL-d will get you out of typing mode

7. `man` + command - find the manual entry on that command

8. `grep -i` - will search for string within files ignoring case

9. `less + FILENAME` - page through file

10. `cat + FILENAME` - print whole file

11. `export` - set a new environment variable

pipes and redirection |what happens
--------------------- | -----------
$|$ | output left to right command
$<$ | input right to program left
$>$ | output left to file on right
$>>$ | output left then appends to the file on the right 


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

`ls` lists all the files and folders in a directory

`ls -a' includes hidden files in that folder

`ls -l` will provide a long form list of files and folders in a directory
> The long form list states: permissions, owner, group, file size last modified,  

---

