# Project-3-Vocabulary

Vocabulary anagrams game for primary school Arabic language
learners.

## Objectives:

* Use Javascript as a front-end language. 
* Use AJAX to facilitate smooth interaction between the
  front-end and the back-end.
* Use unit test to validate the correctness of the code
  intended behaviour.

## Dependencies:

* Designed for Unix, mostly interoperable on Linux or macOS.
  May also work on Windows, but no promises. A Linux
  virtual machine may work. You may want to test on shared
  server (if available).
* You must install [docker](https://www.docker.com/products/docker-desktop/).

## Overview

A simple anagram game designed for Arabic-language learning
students in elementary school. Students are
presented with a list of vocabulary words (taken from a text
file) and an anagram. The anagram is a jumble of some number of
vocabulary words, randomly chosen. Students attempt to type words
that can be created from the jumble. When a matching word is typed,
it is added to a list of solved words. 

The vocabulary word list is fixed for one invocation of the server,
so multiple students connected to the same server will see the same
vocabulary list but may have different anagrams.

### Status

[flask_vocab.py](vocab/flask_vocab.py) and the template
[vocab.html](vocab/templates/vocab.html) are a 'skeleton'
version of the anagram game project. They use conventional
interaction through a form, interacting only when the user
submits the form. 

### Minijax? 

[flask_minijax.py](vocab/flask_minijax.py) and
[templates/minijax.html](vocab/templates/minijax.html) are a tiny example
of using JQuery with flask for an Ajax application. They should not
be included in the final version of the project. 

## Instructions:

* Familiarize yourself with `flask_vocab.py` and `flask_minijax.py` by
  running them separately. You need to understand them to work on this
  project. In order to run `flask_minijax.py` instead of default
  `flask_vocab.py`, you can specify it when spinning of a new container.
  e.g., 
  ```shell
  docker run -d -p <host-port>:<container-port> <image-name> flask_minijax.py 
  ```
* Your task is to replace the form interaction (in `flask_vocab.py`)
  with AJAX interaction on each keystroke using the techniques
  demonstrated in `flask_minijax.py`. Please note that the code in
  `minijax.html` is dealing with English letters (keystrokes).
  The behaviour of other language (Arabic in our case) might differ.
  Thus, understand the interaction between `flask_minijax.py` and `minijax.html`
  then think of what you need to change in order to make it work for Arabic
  letters/text.
* Not all error messages will be applicable after you switch to using AJAX. For example,
  the error message:
  * `الكلمة (شعور) ليست ضمن قائمة الكلمات!`
  * `الكلمة (أحمد) لا يمكن انشائها من قائمة الحروف المعطاة (ف خ ث س ج).`

  These error messages make sense when we asked the user to write a whole word then
  "submit" (click on `جرب`). The new design with AJAX should not even ask the user to
  submit anything. Therefore, these messages don't apply. 
* Think of as many error messages to show to the user as you can. Although we sayed
  above that some error messages should not be included, it does not mean there are no
  other ones! 
* You will submit your `credentials.ini` in
  [Blackboard](https://lms.qu.edu.sa/). 

## Grading Rubric

* **[30 Points]** Javascript/AJAX in the frontend (`vocab.html`)
* **[30 Points]** Logic in the backend (`flask_vocab.py`)
* **[20 Points]** Frontend to backend interaction (with correct
  requests/responses) between `vocab.html` and `flask_vocab.py`
* **[20 Points]** If the `Dockerfile` builds without any errors. 

## Bonus Points

* **[20 Points]** Dynamic highlighting of "partially built" words. 
* **[20 Points]** Grey-out used letters.
* **[20 Points]** "Disable" (immediately erase) letters that are
  not in the anagram. 