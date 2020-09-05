# Feature Development Process

Please see the [code of conduct](https://app.gitbook.com/@projectpanoptes/s/panoptes-tom/~/drafts/-MEYlQRt38StGT9e-lzj/code-of-conduct) for our playground rules and follow them during all your contributions.

##  **Getting Started**

We prefer that all changes to `panoptes-tom` have an associated GitHub Issue in the project that explains why it is needed. This allows us to debate the best approach to address the issue before folks spend a lot of time writing code. If you are unsure about a possible contribution to the project, please contact the project owners about your idea; of course, an issue is a good way to do this.

## PANOPTES Feature Development

A feature can be a code enhancement, a bug fix, or anything that changes code in the repository.

The basic approach is referred to as a triangular workflow, with 3 git repositories \("repos"\):

* `upstream`: This is the "official" copy of the code. Located at `https://github.com/panoptes/panoptes-tom`. This exists on GitHub.
* `origin`: This is your clone \(fork\) of the upstream repo, typically `https://github.com/<YOUR_GITHUB_USERNAME>/panoptes-tom`. This exists on GitHub.
* `local`: This is a clone of your origin repo, residing on your computer, where you will actually do development work.

It is called triangular because changes flow in one direction around the triangle:

* `upstream -> local`: Pull \(or merge\) changes from the "official" PANOPTES repo into your local.
* `local -> origin`: Push your local changes into your copy of the code on github.
* `origin -> upstream`: Create a Pull Request \(PR\) to ask that your `origin` be merged into the official `upstream`.

### Start Work on a Feature

Make sure you have followed the One Time Setup instructions below first.

By feature we mean a new capability, test, bug fix, or documentation update. Ideally the feature is kept as small as possible \(i.e. one feature, not a couple of features that were convenient to develop together\); it may be code that is tested but otherwise dormant because there are not yet any callers, as changing the callers is another feature.

For any feature you work on there should be a corresponding [Issue](https://github.com/panoptes/panoptes-tom/issues). If one doesn't exist you should create one.

Please also read and adhere to the suggestions in the article [In-Praise-of-Small-Pull-Requests](https://github.com/panoptes/POCS/wiki/In-Praise-of-Small-Pull-Requests-%28PRs%29).

### Create feature development branch

For each feature, you'll want to start with the latest commit \(change\) on the the develop branch in the upstream repo, so make sure you have that in your repo:

```text
git fetch upstream
```

Next create a branch for working on this feature... and only this feature... based on the latest commit on the upstream repo's develop. Use a descriptive name for the branch and include the Issue number at the end \(`nnn` below\).

```text
git checkout -b name-of-feature-branch-nnn upstream/develop
```

> NOTE: The important part here is the `-b` to create a new branch and the `upstream/develop` to have that new branch tied to the official upstream automatically.

### Develop your change

Edit whatever files you need to in `panoptes-tom`, and run tests \(`cd $path-to-dir/panoptes-tom; ./manage.py test`\). Whenever you have code that you want to save, commit it to your local repository:

```text
# Get a list of the files that have been changed.
git status

# Add your changed file(s) to the "staging" area for git.
git add dir-to-commit file1/to/commit file2/to/commit

# Commit those changes.
git commit
```

This last command will bring up an editor into which you need to add a comment describing your change. If you're just committing a small portion of your overall change, it is common to make it a very brief comment about your WIP \(work in progress\). For example: "wip - Test is working"

### Pickup changes from upstream

**Note: This only applies before you `git push` upstream. Don't do this once you've published your change.**

While you're developing your change, other changes may be merged into upstream/develop. At appropriate times, you'll pull those changes into your feature development branch:

```text
# Check for clean working area. Should say "nothing to commit, working directory clean".
git status

# Now pull commits from upstream "official" repo into your local repo
git fetch upstream

# Apply your changes on top of the changes made to upstream/develop.
git merge upstream/develop

# Manually merge conflicts that can't resolve and commit if necessary.
git commit
```

Good times to do this are when you have your code compiling and passing tests, and always immediately before you first publish \(push\) your feature branch to your origin repo, and from there to the upstream repo.

### First push to origin

Push your local changes to your github `origin`:

```text
# Make sure to use the name of the actual branch you are working on.
git push origin name-of-feature-branch-nnn
```

This should show you a URL that you can click on to open a new Pull Request, otherwise see below.

### Create Pull Request

If you didn't click on the URL from the original push \(see previous step\), then open [https://github.com/yourame/panoptes-tom](https://github.com/yourname/panoptes-tom). 

GitHub should tell you that you have a recently pushed branch from which you can create a Pull Request \(PR\). Click the **Compare & pull request** button, write a description of the change. This should include the `nnn` identifier of the `panoptes-tom` Issue with a number sign in front \(e.g. \#1234 for issue number 1234\) so that the PR will be linked to a justification for the change.

### Respond to feedback and make fixes

### Push Fixes

After you've made the requested changes and checked that tests are still passing, re-push your changes to your origin repo. This will automatically update your Pull Request and trigger the execution of tests.

```text
git push
```

### Merge upstream changes \(if required\)

If there are conflicts between your change and other changes that have been merged into upstream/develop \(e.g. there are changes to the files that you too are changing\), you'll need to merge those upstream changes into your feature branch and resolve the conflicts.

```text
git fetch upstream

git merge upstream/develop
```

##  **Code Formatting**

* All Python should use [PEP 8 Standards](https://www.python.org/dev/peps/pep-0008/)
* Line length is set at 100 characters instead of 80.
* It is recommended to have your editor auto-format code whenever you save a file rather than attempt to go back and change an entire file all at once. There are many plugins that exist for this.
*  You can also use [yapf \(Yet Another Python Formatter\)](https://github.com/google/yapf) for which `panoptes-tom` includes a style file \(.style.yapf\). For example:

```text
# cd to the root of your workspace. 
cd $(git rev-parse --show-toplevel) 
# Format the modified python files in your workspace. 
yapf -i $(git diff --name-only | egrep '\.py$')``
```

*  Do not leave in commented-out code or unnecessary whitespace.
* Variable/function/class and file names should be meaningful and descriptive.
* File names should be lower case and underscored, not contain spaces. For example, `my_file.py` instead of `My File.py`.
* Define any project specific terminology or abbreviations you use in the file you use them.

