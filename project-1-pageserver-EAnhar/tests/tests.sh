#! /bin/bash
# 
# Test the trivial web server.  
# Usage:  ./tests.sh localhost:<port-num>
# Example: tests.sh localhost:5000
#
# Get the directory where the script is located

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Build the path to credentials.ini relative to the script directory
#credentials_path="$script_dir/../credentials.ini"

source $script_dir/../credentials.ini

#source ../credentials.ini

# Combine URL and PORT to create URLbase
URLbase="localhost:${PORT}"

# Check if $1 is empty, and if so, assign a default value
if [ -z "$1" ]; then
    URLbase="localhost:${PORT}"
else
    URLbase="$1"
fi


#URLbase=$1

# Test cases for the body
function expect_body() {
    # Args
    path=$1
    expect=$2
    curl --silent ${URLbase}/${path} >/tmp/,$$
    if grep -q ${expect} /tmp/,$$ ; then
      echo "Pass --  found ${expect} in ${path}"
    else
      echo "*** FAIL *** expecting ${expect} in  ${URLbase}/${path}"
    fi
}

# test case for the status
function expect_status() {
    # Args
    path=$1
    expect=$2
    curl --silent ${URLbase}/${path} -D /tmp/,,$$ >/tmp/,$$
    if grep -q ${expect} /tmp/,,$$ ; then
      echo "Pass --  found ${expect} in ${URLbase}/${path} "
    else
      echo "*** FAIL *** expecting status ${expect} in ${URLbase}/${path} "
    fi
}

# test case for the status (looking into header)
function real_status() {
    # Args
    path=$1
    expect=$2
    curl --silent -i ${URLbase}/${path} -D /tmp/,,$$ >/tmp/,$$
    if grep -m1 ^ /tmp/,,$$ | grep -q ${expect} ; then
      echo "Pass --  found ${expect} in ${URLbase}/${path} "
    else
      echo "*** FAIL *** expecting status ${expect} in ${URLbase}/${path} "
    fi
}

expect_body trivia.html  "Seriously?"
expect_status trivia.html "200"
expect_status nosuch.html "404"
expect_status there/theybe.html 404
expect_status there//theybe.html "403"
real_status nosuch.html "404"
real_status there/theybe.html 404
real_status there//theybe.html "403"
