# One Time Setup

### Create origin repo

1. Create an account on github if you don't already have one and log in as that user.
2. Navigate to `https://github.com/panoptes/panoptes-tom`
3. Click the fork button in the upper right of the page.

### Create local repo

_We assume here that you're using the git command line, and Unix like commands._

Pick a location where you'll create your clone of the panoptes-tom repo. You might want to create it somewhere under $HOME. For example, if you're working with multiple repos, you might use a naming scheme like:

`$HOME/git/github.com/`_upstream-user_`/`_upstream-repo-name_

If so, you'd have `PANDIR=$HOME/git/github.com/panoptes`. Next clone the `panoptes-tom` repo:

```text
# **Change yourname to your github user name.** 
git clone https://github.com/yourname/panoptes-tom.git
```

This will create directory `panoptes-tom` in the current directory, download the git repo into panoptes-tom/.git, and checkout the HEAD commit of the primary branch into directory panoptes-tom. 

See [Authenticating to GitHub](https://help.github.com/categories/authenticating-to-github/) for information about how to prove to GitHub who you are when pushing changes back to GitHub.\_

### Set upstream repo

You'll be fetching changes made by other contributors from the upstream repo, `https://github.com/panoptes/panoptes-tom`, so tell git about that:

```text
git remote add upstream https://github.com/panoptes/panoptes-tom.git
```

## \*\*\*\*

