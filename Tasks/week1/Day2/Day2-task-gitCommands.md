
                                                                                            Day2 - Task
                                                                                         __________________


  Exercise 2:  Exercise 2: Git Basic Commands
 
  1. Create your `xware-bootcamp` repository on Github.
  2. Clone `xware-bootcamp` repo to your Desktop.
  3. Create a new folder `week1` using command kine `mkdir`.
  4. Create new file inside `week1` called `README.md` using `touch`.
  5. Add this line `# Hello World From My New Shiny Repository xware-bootcamp` to the file `README.md` using `echo "" > README.md`
  6. add the folder `week1` to the staging area.
  7. Commit the staged files.
  8. See your tracking status using `git status` to make sure all files are committed.
  9. Push your changes to Github using `git push`.
  _____________________

  839  ssh-keygenssh-keygen
  840  ssh-keygen -t rsa 
  841  cd .ssh
  842  cd ~
  843  ssh-keygen -t rsa 
  844  cd .ssh
  845  ls
  846  cat id_rsa.pub 
  847  git clone git@github.com:ibrahimshaabann/xWare-BootCamp-Tasks.git
  848  ls
  849  cd xWare-BootCamp-Tasks/
  850  git status
  851  git add .
  852  git commit -m "initinal commit"
  853  git push
  854  ls
  855  cd Days
  856  cd ..
  857  ls
  858  cd Tasks
  859  ls
  860  cd week
  861  cd week1
  862  ls
  863  nano Day1-task-LinuxTerminal.txt 
  864  git add .
  865  cd ..
  866  ls\
  867  ls
  868  git add .
  869  git commit -m "First task Commit"
  870  git diff
  871  git push
  872  git status
  873 


___________________________________________________________________________________________________________________________________________________________________________________________________



  Exercise 3:  Create Branch

  1. Delete your local repo.
  2. clone your repo locally.
  3. create new branch called `feature-add-new-week` from `main` branch.
  4. create new folder called `week2` using command kine `mkdir`.
  5. Create new file inside `week2` called `README.md` using `touch`.
  6. Add this line `# Hello From Week 2` to the file `README.md` using `echo "" > README.md`
  7. add the folder `week1` to the staging area.
  8. Commit the staged files.
  9. See your tracking status using `git status` to make sure all files are committed.
  10. merge your branch to `main` branch. 
  11. Delete your branch.
  12. See all your commits.
  _____________________


  cd ..
  874  git init
  875  ls -a
  876  rm -r .git/
  877  LS -a
  878  ls -a
  879  clear
  880  ls
  881  cd xWare-BootCamp-Tasks/
  882  git checkout -b feature-add-new-week master
  883  ls
  884  cd Tasks
  885  ls
  886  mkdir week2
  887  cd week2
  888  nano README.md
  889  touch README.md
  890  echo "Hello From Week" 2 > README.md
  891  nano README.md 
  892  ls
  893  cd..
  894  cd ..
  895  ls
  896  cd Tasks
  897  ls
  898  touch /week1/README.md
  899  touch week1/README.md
  900  echo "Hello, My first week tasks xware-bootcamp" > week1/README.md
  901  git add .
  902  git commit - m "Second week commit"
  903  git commit -m "Second week commit"
  904  git status
  905  git checkout master
  906  git merge feature-add-new-week
  907  git checkout -r feature-add-new-week
  908  git branch
  909  git checkout -d feature-add-new-week
  910  git branch
  911  git checkout -D feature-add-new-week
  912  git checkout -d feature-add-new-week
  913  git checkout master
  914  git branch
  915  git checkout -d feature-add-new-week
  916  git branch
  917  git checkout master
  918  git branch
  919  git branch  -d feature-add-new-week
  920  git branch
  921  git push

