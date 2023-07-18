#Day3-Terminal Exercises



####Q1 - Use the cat command to display the contents of a file named "data.txt" and pipe the output to the grep command to search for the word "hello".

  $ cat data.txt | grep "hello" -i


_________________________________________________________________________________________________________________________________________________________________

Q2 - Use the sort command to alphabetically order the lines of a file named "words.txt" and redirect the sorted output to a new file named "sorted_words.txt".

  $ sort words.txt > sorted_words.txt


________________________________________________________________________________________________________________________________________________________________

Q3 - Use the uniq command to filter out duplicate lines from a file named "numbers.txt" and redirect the unique lines to a new file named "unique_numbers.txt".

  $ cat numbers.txt
  
  5
  5
  4
  4
  66
  66
  1
  2
  8
  74
  9 5
  6 5

  $ uniq numbers.txt > uniq_numbers.txt

  $ cat uniq_numbers.txt 
 
  5
  4
  66
  1
  2
  8
  74
  9 5
  6 5

______________________________________________________________________________________________________________________________________________________________

Q4 - Create an alias named "xware" that executes the command ls -l every time it is invoked.

  $ alias xware="ls -l"

  $ xware  
  
  total 44
  -rw-rw-r-- 1 new new   25 Jul 18 11:35 data.txt
  -rw-rw-r-- 1 new new 1552 Jul 16 18:36 Day1-task.txt
  -rw-rw-r-- 1 new new  738 Jul 18 11:41 Day3-Task-Terminal.txt
  -rw-rw-r-- 1 new new   26 Jul 16 18:12 error.txt
  -rw------- 1 new new   19 Jul 17 17:49 notes.txt.save
  -rw-rw-r-- 1 new new   31 Jul 18 11:42 numbers.txt
  -rw-rw-r-- 1 new new   36 Jul 18 11:39 sorted_words.txt
  -rw-rw-r-- 1 new new   38 Jul 16 18:14 system.log
  -rw-rw-r-- 1 new new   24 Jul 16 17:59 text.txt
  -rw-rw-r-- 1 new new   24 Jul 18 11:43 uniq_numbers.txt
  -rw-rw-r-- 1 new new   36 Jul 18 11:39 words.txt


___________________________________________________________________________________________________________________________________________________________________

Q5 - display the list of environmental variables in the terminal.


  $ env | grep "USER"

  USERNAME=new
  USER=new

__________________________________________________________________________________________________________________________________________________

Q6 - list the previously executed commands.

  $ history


___________________________________________________________________________________________________________________________

Q7 - display the network interfaces and their configurations.

  $ ip addr


