# Git and Git Workflow

## Install Git and Create a GitHub account.
- Linux 
    ```bash
    $ sudo apt-get install git
    ```
    ```bash
    $ sudo yum install git
    ```
- Windows and Mac
    - https://git-scm.com/downloads

### GitHub account
- www.github.com

## What is Git?
- Git is a free and open source version control system
- It's system that keeps records of your changes 
- Allows collaboration and lets you see who made what changes as well as when those changes were made
- **Git lets you revert any changes and go back to a previous version of a project**

## What's so special about Git?
- Distributed version control system
    - Git doesn't rely on a central server to store all versions of a project
    - Every developer gets and full history of the project when they "clone"
- Users can make any changes without an internet connection
- An internet connection is required only to push and pull from a remote server

## Key Concepts
- Snapshot: The way git tracks changes to the code
    - At a given time you can create a snapshot of the current version of the code
- Commit: The act of creating a snapshot. (Commits also keeps track of the previous commit that came before it)
    - So an open source project is just made up of a bunch of commits
- Repository: Usually a collection of the project along with its full history (usually on a remote server, GitHub)
- Cloning: The act of copying a repository from a remote server
- Pulling: Downloading new changes from a remote repository that doesn't exist in your local repository
- Pushing: Adding your local changes to a remote repository
- Branches: All commits on git exists on a branch
    - The main branch in a project is called the **master** branch

<a href="https://www.atlassian.com/git/tutorials/using-branches">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:746be214-eb99-462c-9319-04a4d2eeebfa/01.svg?cdnVersion=kz" width="auto" height="auto">
</a>

(https://www.atlassian.com/git/tutorials/using-branches)

(https://nvie.com/posts/a-successful-git-branching-model/)

## Typical Git project
<a href="https://git-scm.com">
  <img src="https://git-scm.com/book/en/v2/images/branch-and-history.png" width="auto" height="auto">
</a>

(https://git-scm.com/book/en/v2/images/branch-and-history.png)
- Head: reference to the current branch in the workspace (in this case we are working in the master branch)
    - It is also a reference to most recent commit (most of the time)
    
## Branching
- Typically it is best to not directly work on master 
    - The master branch is the main branch, so it must be your most stable branch
    - All developers who will work on a project will initially branch off of the master branch
- Branching off: is the concept of making a new branch using the latest commit of another branch
<a href="https://www.atlassian.com/git/tutorials/using-branches">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:2bef0bef-22bc-4485-94b9-a9422f70f11c/02%20(2).svg?cdnVersion=kw" width="auto" height="auto">
</a>
- Merge: Once you feature is complete, merge the changes in the branch back in to master
<a href="https://www.atlassian.com/git/tutorials/using-branches/git-merge">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=kz" width="auto" height="auto">
</a>

(https://www.atlassian.com/git/tutorials/using-branches)

## Git cheat sheet
(https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

## Typical Git workflow
1. **Pull** latest code from the remote server
2. Write some new code or edit some existing code
3. **Add** file to the staging area
4. **Commit** changes with readable commit message
5. **Push** the commit
6. Repeat
<a href="https://www.atlassian.com/git/tutorials/using-branches/git-merge">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:b5259cce-6245-49f2-b89b-9871f9ee3fa4/03%20(2).svg?cdnVersion=kz" width="auto" height="auto">
</a>

(https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## So now, What is GitHub?
- The largest git repository hosting service
- Allows code collaboration with anyone and has some handy UI tools to easily manage your repository

## Open Source and GitHub
- There are hundreds of thousands of project available for developers to contribute

## Typical open source Git workflow 
1. **Fork** or **Pull** latest code from the remote server
2. Write some new code or edit some existing code
3. **Add** file to the staging area
4. **Commit** changes with readable commit message
5. **Push** the commit
6. Create a **Pull request** to the original repository
6. Repeat
<a href="https://guides.github.com/introduction/flow/">
  <img src="https://cdn-images-1.medium.com/max/1600/1*iHPPa72N11sBI_JSDEGxEA.png" width="auto" height="auto">
</a>

(https://guides.github.com/introduction/flow/)

    - The master branch is the main branch, so it must be your most stable branch
    - All developers who will work on a project will initially branch off of the master branch
- Branching off: is the concept of making a new branch using the latest commit of another branch
<a href="https://www.atlassian.com/git/tutorials/using-branches">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:2bef0bef-22bc-4485-94b9-a9422f70f11c/02%20(2).svg?cdnVersion=kw" width="auto" height="auto">
</a>
- Merge: Once you feature is complete, merge the changes in the branch back in to master
<a href="https://www.atlassian.com/git/tutorials/using-branches/git-merge">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=kz" width="auto" height="auto">
</a>

(https://www.atlassian.com/git/tutorials/using-branches)

## Git cheat sheet
(https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

## Typical Git workflow
1. **Pull** latest code from the remote server
2. Write some new code or edit some existing code
3. **Add** file to the staging area
4. **Commit** changes with readable commit message
5. **Push** the commit
6. Repeat
<a href="https://www.atlassian.com/git/tutorials/using-branches/git-merge">
  <img src="https://wac-cdn.atlassian.com/dam/jcr:b5259cce-6245-49f2-b89b-9871f9ee3fa4/03%20(2).svg?cdnVersion=kz" width="auto" height="auto">
</a>

(https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

## So now, what is GitHub?
- The largest git repository hosting service
- Allows code collaboration with anyone and has some handy UI tools to easily manage your repository

## Open Source and GitHub
- There are hundreds of thousands of project available for developers to contribute

## Typical open source Git workflow 
1. **Fork** or **Pull** latest code from the remote server
2. Write some new code or edit some existing code
3. **Add** file to the staging area
4. **Commit** changes with readable commit message
5. **Push** the commit
6. Create a **Pull request** to the original repository
6. Repeat
<a href="https://guides.github.com/introduction/flow/">
  <img src="https://cdn-images-1.medium.com/max/1600/1*iHPPa72N11sBI_JSDEGxEA.png" width="auto" height="auto">
</a>

(https://guides.github.com/introduction/flow/)
