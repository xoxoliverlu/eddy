#!/bin/dash

# Test for the quit command with regex
output=$(seq 500 600 | ./eddy.py '/^.+5$/q')
expect=$(seq 500 600 | 2041 eddy '/^.+5$/q')

if [ "$output" = "$expect" ]; 
then
    exit 0
else
    exit 1
fi