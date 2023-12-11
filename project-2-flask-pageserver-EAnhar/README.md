# Project-2-Flask-Pageserver

A project to demonstrate the power of docker and web frameworks
compared to the previous projects. 

## Objectives:

* Use Containers (Docker to be specific) to manage software
  dependencies and shipping.
* Use web frameworks (flask in this case) to handle essential
  web services. 

## Dependencies:

* Designed for Unix, mostly interoperable on Linux or macOS.
  May also work on Windows, but no promises. A Linux
  virtual machine may work. You may want to test on shared
  server (if available).
* You must install [docker](https://www.docker.com/products/docker-desktop/).

## Instructions:

* The goal of this project is to implement the same file checking logic
  that you implemented in project 1 using flask. 
* Like project 1, if a file `<file_name>.html` exists, transmit "200/OK"
  header followed by that file html. If the file does not exist, transmit
  an error code in the header along with the appropriate page html in the
  body. You'll do this by creating error handlers (refer to the slides).
  Additionally, you will check the url for any malicious characters just
  like what we did in project-1. This can be made easier with Flask. You just
  need. to figure out how to do it.
* You'll need to create the following two html files with the error messages.
  Each file will be returned as a content if the user reach one of these cases. 
    * `404.html` will display "File not found!"
    * `403.html` will display "File is forbidden!"
* Update your name and email in the Dockerfile.
* You will submit your `credentials.ini` in
  [Blackboard](https://lms.qu.edu.sa/) (a skeleton is not provided).
  Note it __must__ follow the same setup we provided in the past
  (e.g., similar to Project-1 where it has the section `[DEFAULT]`, then
  all the essential keys and values). The port should refer to the docker container
  port you would like to use.

## Getting Started on the Flask Project

The best reference for understanding how Docker and its commands works is
[Docker Documentation](https://docs.docker.com/engine/reference/builder/).
It will always be up-to-date. We also provide a [Docker 101](web/Docker-101.md)
file that could help with the essentials.

Below, we describe commands that are related to this project. 

* Go to the web folder in the repository. Read every line of the
  docker file and the simple flask app.
* Build the simple flask app image using
  ```shell
  docker build -t it492-flask-demo .
  ```
  * What does `-t` mean?
  * What does the `it492-flask-demo` mean?
  * What does the `.` at the end of the file means?

* Run the container using
  ```shell
  docker run -d -p 5000:5000 it492-flask-demo
  ```
  * What does `-d` means?
  * What does `-p 5000:5000` means?
  * What does having the name `it492-flask-demo` at the end of this command mean?

* Launch http://127.0.0.1:5000 (or http://localhost:5000) using web
  browser and check the output "IT492 docker demo!"

# Grading Rubric

* **[60 Points]**: You will get 20 points for every working
  functionality (i.e., (a), (b), and (c) from project 1). 
* **[20 Points]**: If the `Dockerfile` builds without any errors.
* **[20 Points]**: if the two html files (`404.html` and `403.html`)
  are created in the appropriate location.

# All Rights Reserved

This is the work of Ziyad Alsaeed. Any copy or distribution of this
repository or a fork of it in a way other than the instruction provided
above will subject you to legal proceedings. 