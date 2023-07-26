
1. `git init`
   - **Explanation:** Initializes a new Git repository in the current directory.
   - **Example:**
     
     ```bash
     git init
     ```

2. `git clone [repository_url]`
   - **Explanation:** Clones an existing Git repository from a remote server to your local machine.
   - **Example:**
     ```bash
     git clone https://github.com/user/repo.git
     ```

3. `git add [file(s)]`
   - **Explanation:** Adds changes of specified file(s) to the staging area to be ready for committing.
   - **Example:**
     ```bash
     git add file.txt
     ```

4. `git commit -m "[commit_message]"`
   - **Explanation:** Commits the staged changes with a descriptive commit message.
   - **Example:**
     ```bash
     git commit -m "Add new feature"
     ```

5. `git status`
   - **Explanation:** Shows the status of the working directory and the staged changes.
   - **Example:**
     ```bash
     git status
     ```

6. `git push [remote] [branch]`
   - **Explanation:** Uploads your local branch commits to the remote repository.
   - **Example:**
     ```bash
     git push origin main
     ```

7. `git pull [remote] [branch]`
   - **Explanation:** Fetches and merges changes from the remote repository to your local branch.
   - **Example:**
     ```bash
     git pull origin main
     ```

8. `git branch`
   - **Explanation:** Lists all the branches in the repository and highlights the current branch.
   - **Example:**
     ```bash
     git branch
     ```

9. `git checkout [branch_name]`
   - **Explanation:** Switches to the specified branch to work on that branch.
   - **Example:**
     ```bash
     git checkout feature-branch
     ```

10. `git merge [branch_name]`
    - **Explanation:** Merges the specified branch into the current branch.
    - **Example:**
      ```bash
      git merge feature-branch
      ```

11. `git log`
    - **Explanation:** Displays the commit history and the changes made in each commit.
    - **Example:**
      ```bash
      git log
      ```

12. `git remote -v`
    - **Explanation:** Lists the remote repositories associated with the current repository.
    - **Example:**
      ```bash
      git remote -v
      ```

13. `git fetch`
    - **Explanation:** Downloads objects and refs from another repository without merging.
    - **Example:**
      ```bash
      git fetch
      ```

14. `git config`
    - **Explanation:** Allows you to set or view configuration options for Git.
    - **Example:**
      ```bash
      git config --global user.name "Your Name"
      git config --global user.email "youremail@example.com"
      ```

These are some of the fundamental Git terminal commands that you'll commonly use while working with Git repositories. Remember that Git offers many more commands and functionalities, so feel free to explore further as you gain more experience with Git.
