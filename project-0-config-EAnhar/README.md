# Project-0-Config

Trivial project to exercise version control, turn-in, and other
mechanisms.

## Instructions:

- By reading this README.md file, it means you have successfully
  accepted the assignment and forked our main repository.
- Make sure you **clone** this repository to your local machine. DO NOT WORK ON YOUR REPO from the cloud. 
- Before you edit a file, read the comments (inside that file) carefully.
- Copy the `credentials-skel.ini` file, rename it to `credentials.ini` and fill in
  appropriately.
- Modify the program "hello.py" so that it prints "Hello
  world". (Nothing more and nothing less.)  Note that you do NOT do
  this by changing the hello.py source file. Rather, the message is a
  configuration constant from the `credentials.ini` file; fix it there.
- Replace these instructions with a proper README including the 
  author, contact address, and a brief description of what the 
  software does.
- Test your program locally; revise and re-test as needed.
- Test your code with the Makefile. Use the command `make run` to execute. Revise and push changes
  as needed.
- Stage and Commit your changes. You will need to use `git add` on your file
  `README.md`, but *not* on `credentials.ini`, because that 
  file does not belong on GitHub.  (In later projects it will contain
  confidential information, like access keys and passwords for web
  services.).
- Your changes must be "**pushed**" to your private repository
  on GitHub so that the auto-checker can "**clone**" them back to the 
  grading machine.
- Turn in with [Blackboard](https://lms.qu.edu.sa/). The file you turn in is credentials.ini. We
  use the repository link in your `credentials.ini` to access the rest,
  just like the auto-checker.

## Sample `credential.ini`

1. Add your name to the credential file using the same skeleton given to you.
2. The default (`[default]`) tag should not be changed.
3. Add your name (e.g., `author=Ahmad Saleh`)
4. Add your forked repo SSH link (e.g., `repo=git@github.com:quit315/project-0-hello.git`). Be careful not to copy the git commands such as `git clone` from GitHub.
5. Add your QU ID (e.g., `quid=931100100`)
6. Edit the message key as instructed above. 

Here is a sample of the .ini file if I would submit it. 

```ini
#
#
# Credentials:
#
#    This is simply a key file to turn in your work.
# 	 Any missing or wrong information could lead to
#    a failure in the whole assignment. Please change
#    the filed below according to the examples provided.
#
[DEFAULT] 
author=Ziyad Alsaeed
repo=git@github.com:it492/project-0-config.git
quid=931100100
message=The message I need to add
```

## Grading Rubric
- **[40 Points]** For submitting your `credentials.ini` file to [Blackboard](https://lms.qu.edu.sa/).
  You get 10 points for each correctly provided field.
- **[30 Points]** if you the `hello.py` prints the correct message given your `credentials.ini`.
- **[30 Points]** for not including any `.ini` file within your GitHub repo. This includes our
  `.ini` file (i.e., you have to delete `credentials-skel.ini` from the repo).

# All Rights Reserved
This is the work of Ziyad Alsaeed. Any copy or distribution of this
repository or a fork of it in a way other than the instruction provided
above will subject you to legal proceedings.